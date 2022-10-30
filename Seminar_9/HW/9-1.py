# 1. Прикрутить бота к игре "Крестики-нолики".

import logging

from telegram import ReplyKeyboardMarkup, Update
from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler,
    Filters,
    ConversationHandler,
)

from config import token

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)
logger = logging.getLogger(__name__)


field = list(range(1, 10))
win_coord = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
CHOICE, MENU = range(2)


def draw_board(board):
    f = ''
    f += f'{"-" * 40}\n'
    for i in range(3):
        f += f"| {board[0 + i * 3]:^10} | {board[1 + i * 3]:^10} | {board[2 + i * 3]:^10} |\n"
        f += f'{"-" * 40}\n'
    return f


def check_win(board):
    global win_coord
    n = [board[el[0]] for el in win_coord if board[el[0]] == board[el[1]] == board[el[2]]]
    return n[0] if n else n


def AI(board):
    step = 0

    # 1) если на какой-либо из победных линий 2 свои фигуры и 0 чужих
    step = check_line(2, 0, board)
    
    # 2) если на какой либо из победных линий 2 чужие фигуры и 0 своих
    if not step:
        step = check_line(0, 2, board)
    
    # 3) если 1 фигура своя и 0 чужих
    if not step:
        step = check_line(1, 0, board)
    
    # 4) если центр пуст, то занимаем центр
    if not step:
        if board[4] != chr(10060) and board[4] != chr(11093):
            step = 5
    
    # 5) если центр занят, то занимаем первую ячейку
    if not step:
        if board[0] != chr(10060) and board[0] != chr(11093):
            step = 1

    return step


def check_line(sum_O, sum_X, board):
    global win_coord
    step = 0

    for el in win_coord:
        x = 0
        o = 0

        for i in range(3):
            if board[el[i]] == chr(10060):
                x += 1
            elif board[el[i]] == chr(11093):
                o += 1
        
        if x == sum_X and o == sum_O:
            for j in range(3):
                if board[el[j]] != chr(10060) and board[el[j]] != chr(11093):
                    step = board[el[j]]
    
    return step


def start(update: Update, _):
    global field
    field = list(range(1, 10))
    update.message.reply_text(f"Hello {update.effective_user.first_name} {chr(128075)}!\n"
                            f"Let's play tic tac toe {chr(128521)}\n"
                            "If you want to exit, enter /cancel.")
    update.message.reply_text(draw_board(field))
    update.message.reply_text("You're first. Enter a number from 1 to 9.")
    return CHOICE


def choice(update: Update, _):
    reply_keyboard = [['Play'], ['Exit']]
    markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True, resize_keyboard=True)
    symbol = chr(10060)
    answer = update.message.text
    if answer.isdigit() and int(answer) in range(1, 10):
        step = int(answer)
        if field[step - 1] in (chr(10060), chr(11093)):
            update.message.reply_text(f"This cell is already occupied! {chr(9995)}\nPlease, choose another cell.")
            return CHOICE
        field.insert(field.index(step), symbol)
        field.remove(step)
        if check_win(field):
            update.message.reply_text(f"{symbol} - WIN! {chr(127942)}{chr(127881)}\n"
                                    "Let's play again?", reply_markup=markup)
            return MENU
        else:
            symbol = chr(11093)
            step = AI(field)
            if step:
                field.insert(field.index(step), symbol)
                field.remove(step)
                update.message.reply_text(draw_board(field))
                if check_win(field):
                    update.message.reply_text(f"You're lose... {chr(128532)}\n{symbol} - WIN.\n"
                                            "Let's play again?", reply_markup=markup)
                    return MENU
            else:
                update.message.reply_text(f"Drawn game! {chr(129309)}\n"
                                        "Let's play again?", reply_markup=markup)
                return MENU                 
    elif answer == '/cancel':
        update.message.reply_text(f'Goodbye {update.effective_user.first_name}! {chr(128521)}')
        return ConversationHandler.END
    else:
        update.message.reply_text(f"Incorrect input {chr(9940)}!\nPlease, enter a number from 1 to 9")
        return CHOICE          


def menu(update: Update, _):
    action = update.message.text
    if action == 'Play':
        global field
        field = list(range(1, 10))
        update.message.reply_text(draw_board(field))
        update.message.reply_text("You're first. Enter a number from 1 to 9.")
        return CHOICE
    elif action == 'Exit':
        update.message.reply_text(f'Goodbye {update.effective_user.first_name}! {chr(128521)}')
        return ConversationHandler.END


def exit(update: Update, _):
    update.message.reply_text(f'Goodbye {update.effective_user.first_name}! {chr(128521)}')
    return ConversationHandler.END


if __name__ == '__main__':
    updater = Updater(token)
    dispatcher = updater.dispatcher

    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],
        states={
            CHOICE: [MessageHandler(Filters.text, choice)],
            MENU: [MessageHandler(Filters.text, menu)]
        },
        fallbacks=[CommandHandler('cancel', exit)]
    )

    dispatcher.add_handler(conv_handler)

    print('Server start')

    updater.start_polling()
    updater.idle()

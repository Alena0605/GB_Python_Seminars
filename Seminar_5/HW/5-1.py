"""
1. Напишите программу, удаляющую из текста все слова, содержащие "абв". 
В тексте используется разделитель пробел.
"""

from random import sample


def fill_string(length, text):
    if length <= 0:
        return -1
    
    result = ''
    for i in range(length):
        el = sample(text, 3)
        result += f"{''.join(el)} "  
    
    return result


def delete_abv(string):
    if string == -1:
        return "The data is incorrect!"

    words_list = [word for word in string.split() if word != 'абв']

    return " ".join(words_list)


size = int(input("Enter number of words: "))
word = input("Enter a word: ")

words_string = fill_string(size, word)

print(words_string)
print(delete_abv(words_string))

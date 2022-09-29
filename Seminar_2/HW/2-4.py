"""
4. * Напишите программу, которая принимает на вход 2 числа. Задайте список из N элементов,
заполненных числами из промежутка [-N, N]. Найдите произведение элементов на указанных позициях (не индексах).
"""

pos_1 = int(input('Enter the first position: '))
pos_2 = int(input('Enter the second position: '))
n = int(input('Enter a number: '))
ls = list()

for i in range(-abs(n), abs(n) + 1):
    ls.append(i)

if pos_1 > 0 and pos_2 > 0:
    if pos_1 > len(ls) or pos_2 > len(ls):
        print('Position is out of range.')
    else:
        result = ls[pos_1 - 1] * ls[pos_2 - 1]
        print(ls)
        print(result)
elif pos_1 < 0 and pos_2 < 0:
    if pos_1 < -len(ls) or pos_2 < -len(ls):
        print('Position is out of range.')
    else:
        result = ls[pos_1] * ls[pos_2]
        print(ls)
        print(result)
elif pos_1 > 0 and pos_2 < 0:
    if pos_1 > len(ls) or pos_2 < -len(ls):
        print('Position is out of range.')
    else:
        result = ls[pos_1 - 1] * ls[pos_2]
        print(ls)
        print(result)
elif pos_1 < 0 and pos_2 > 0:
    if pos_1 < -len(ls) or pos_2 > len(ls):
        print('Position is out of range.')
    else:
        result = ls[pos_1] * ls[pos_2 - 1]
        print(ls)
        print(result)
else:
    print('Error, 0 entered!')

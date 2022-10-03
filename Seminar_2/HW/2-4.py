"""
4. * Напишите программу, которая принимает на вход 2 числа. Задайте список из N элементов,
заполненных числами из промежутка [-N, N]. Найдите произведение элементов на указанных позициях (не индексах).
"""

pos_1 = int(input('Enter the first position: '))
pos_2 = int(input('Enter the second position: '))
n = int(input('Enter a number: '))

ls = list(range(-abs(n), abs(n) + 1))

if len(ls) > pos_1 > 0 and len(ls)> pos_2 > 0:
    result = ls[pos_1 - 1] * ls[pos_2 - 1]
    print(ls)
    print(result)
elif -len(ls) < pos_1 < 0 and -len(ls) < pos_2 < 0:
    result = ls[pos_1] * ls[pos_2]
    print(ls)
    print(result)
elif len(ls) > pos_1 > 0 and -len(ls) < pos_2 < 0:
    result = ls[pos_1 - 1] * ls[pos_2]
    print(ls)
    print(result)
elif -len(ls) < pos_1 < 0 and len(ls) > pos_2 > 0:
    result = ls[pos_1] * ls[pos_2 - 1]
    print(ls)
    print(result)
else:
    print('There are no values for these indexes!')

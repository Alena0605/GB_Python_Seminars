"""
1. Напишите программу, которая принимает на вход число N и выдаёт последовательность из N членов.
"""

num = int(input('Введите число: '))
result = 1

for i in range(num):
    print(result, end=' ')
    result *= -3 

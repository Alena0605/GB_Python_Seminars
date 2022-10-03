"""
1. Задайте список, состоящий из произвольных чисел, количество задаёт пользователь. 
Напишите программу, определяющую присутствует ли в заданном списке число, полученное от пользователя.
"""

from random import sample


def find_num(length, number):
    if length <= 0:
        return "Error!"
    
    ls = sample(range(length * 2), length)
    print(ls)

    if number in ls:
        return "Yes"
    else:
        return "No"


num_1 = int(input('Enter length of the list: '))
num_2 = int(input("Enter a number: "))
print(find_num(num_1, num_2))

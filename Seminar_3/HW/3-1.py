"""
1. Задайте список, состоящий из произвольных чисел, количество задаёт пользователь.
Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётных позициях(не индексах).
"""

from random import sample


def make_list(length):
    if length <= 0:
        return []

    nums_list = sample(range(length * 2), length)
    return nums_list


def find_sum_odd_pos(nums_list):
    length = len(nums_list) 
    if length == 0:
        return "The list is empty!"

    nums_sum = 0
    for i in range(0, length, 2):
        nums_sum += nums_list[i]
    return nums_sum


size = int(input("Enter length of the list: "))
ls = make_list(size)

print(ls)
print(find_sum_odd_pos(ls))

"""
1. Представлен список чисел. Необходимо вывести элементы исходного списка, 
значения которых больше предыдущего элемента. Use comprehension.
"""

from random import sample


def fill_list(length):
    if length <= 0:
        return []

    result = sample(range(length * 3), length)
    return result


def more_than_previous(nums_list):
    length = len(nums_list)
    if length == 0:
        return "The list is empty!"

    result = [nums_list[i] for i in range(1, length) if nums_list[i] > nums_list[i - 1]]
    return result


size = int(input("Enter length of the list: "))
ls = fill_list(size)

print(ls)
print(more_than_previous(ls))

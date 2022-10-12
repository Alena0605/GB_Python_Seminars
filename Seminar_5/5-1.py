"""
1. Создайте список из N натуральных чисел (от 0 до N), упорядоченных по возрастанию.
Среди чисел не хватает одного, чтобы выполнялось условие A[i] - 1 = A[i-1]. Найдите это число.
"""

from random import choice


def fill_list(lenght):
    result = list(range(lenght + 1))
    result.remove(choice(result))
    return result


def check_number(nums_list):
    for i in range(1, len(nums_list)):
        if nums_list[i] - 1 != nums_list[i - 1]:
            return nums_list[i] - 1
    return -1


size = int(input("Enter length of the list: "))
ls = fill_list(size)

print(ls)
print(check_number(ls))

"""
3. Задайте последовательность чисел. 
Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности в том же порядке.
"""

from random import randrange


def make_list(length):
    if length <= 0:
        return[]

    result = []

    for i in range(length):
        result.append(randrange(1, 10))

    return result


def unique_elements(nums_list):
    length = len(nums_list)
    if length == 0:
        return "The list is empty!"
    
    unique_nums = []

    for num in nums_list:
        if nums_list.count(num) == 1:
            unique_nums.append(num)
    
    return unique_nums


size = int(input("Enter length of the list: "))
ls = make_list(size)

print(ls)
print(unique_elements(ls))

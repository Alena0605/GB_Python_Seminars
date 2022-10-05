"""
2. Напишите программу, которая найдёт произведение пар чисел списка.
Парой считаем первый и последний элемент, второй и предпоследний и т.д.
"""

from random import sample


def make_list(length):
    if length <= 0:
        return []

    nums_list = sample(range(length * 2), length)
    return nums_list 


def find_multiply_pairs(nums_list):
    length = len(nums_list) 
    if length == 0:
        return "The list is empty!"
    
    result = []
    half_len = length // 2
    max_index = length - 1

    for i in range(half_len):
        multiply = nums_list[i] * nums_list[max_index - i]
        result.append(multiply)
    
    if length % 2 != 0:
        result.append(nums_list[half_len])
    
    return result
    

size = int(input("Enter length of the list: "))
ls = make_list(size)

print(ls)
print(find_multiply_pairs(ls))

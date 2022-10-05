"""
4. * Задайте список из произвольных вещественных чисел, количество задаёт пользователь.
Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
"""

from random import uniform


def make_list(length):
    if length <= 0:
        return []
    
    float_nums_list = []
    for el in range(length):
        num = round(uniform(1, 10), 2)
        float_nums_list.append(num)
    
    return float_nums_list


def find_dif_frac(nums_list):
    length = len(nums_list) 
    if length == 0:
        return "The list is empty!"
    
    frac_list = []
    for num in nums_list:
        frac = round(num - int(num), 2)
        frac_list.append(frac)

    max_num = max(frac_list)
    min_num = min(frac_list)
    dif = max_num - min_num

    return f"Max: {max_num}, Min: {min_num}, Difference: {dif}"


size = int(input("Enter length of the list: "))
ls = make_list(size)

print(ls)
print(find_dif_frac(ls))

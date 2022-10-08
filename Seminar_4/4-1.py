"""
1. Задайте строку из набора чисел. Напишите программу, которая покажет большее и меньшее число.
В качестве разделителя используйте пробел.
"""


def check_list(string_ls):
    for i in string_ls:
        if not i.replace("-", "").isdigit():
            return []
    return string_ls


def max_min_num(nums_list):
    ls = check_list(nums_list)

    if ls:
        return min(ls, key=int), max(ls, key=int)
    else:
        return []


string = input("Enter some numbers: ").split()
print(max_min_num(string))

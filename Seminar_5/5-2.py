"""
2. Создайте список, в который попадают числа, описывающие возрастающую последовательность.
Порядок элементов менять нельзя.
"""

from random import choices


def fill_list(length):
    return choices(range(length * 2), k=length)


def increase_sequences(nums_list):
    result = []

    for i in range(len(nums_list)):
        cur_num = ls[i]
        seq = [cur_num]
        for j in range(i, len(nums_list)):
            if nums_list[j] > cur_num:
                seq.append(nums_list[j])
                cur_num = nums_list[j]
        if len(seq) > 1:
            result.append(seq)
    
    return result


size = int(input("Enter length of the list: "))
ls = fill_list(size)

print(ls)
print(increase_sequences(ls))

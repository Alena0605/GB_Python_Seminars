"""
5. ** Реализуйте алгоритм перемешивания списка. Без функции shuffle из модуля random.
"""

import random

num = int(input('Enter a number: '))

ls_1 = list()
for i in range(num):
    ls_1.append(i)

ls_2 = ls_1.copy()
for j in range(num):
    index = random.randint(0, num - 1)

    temp = ls_2[j]
    ls_2[j] = ls_2[index]
    ls_2[index] = temp

print(ls_1)
print(ls_2)

"""
5. ** Реализуйте алгоритм перемешивания списка. Без функции shuffle из модуля random.
"""

from random import randrange

num = int(input('Enter a number: '))

ls_1 = list(range(num))
ls_2 = ls_1.copy()

for i in range(num):
    num_1 = randrange(num)
    num_2 = randrange(num)
    ls_2[num_1], ls_2[num_2] = ls_2[num_2], ls_2[num_1]

print(ls_1)
print(ls_2)

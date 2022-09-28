"""
3. Задайте список из n чисел, заполненный по формуле (1 + 1/n) ** n и выведите на экран их сумму.
"""

num = int(input('Enter a number: '))
ls = list()

for i in range(1, num + 1):
    ls.append(round((1 + 1 / i) ** i, 2))

print(ls)
print(sum(ls))

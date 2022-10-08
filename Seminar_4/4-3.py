"""
3. Задайте два числа. Напишите программу, которая должна находить НОК (наименьшее общее кратное) этих двух чисел.
"""

from math import gcd


def nok(num_1, num_2):
    return (num_1 * num_2) // gcd(num_1, num_2)


a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

print(nok(a, b))

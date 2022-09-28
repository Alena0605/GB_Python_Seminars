"""
1. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
"""

float_num = float(input('Enter a float number: '))
len_of_number = len(str(float_num).replace('.', ''))
int_num = int(float_num * 10 ** (len_of_number - 1))
result = 0

while int_num > 0:
    remainder = int_num % 10
    result += remainder
    int_num //= 10

print(result)

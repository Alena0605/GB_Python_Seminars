"""
1. Напишите программу, которая принимает на вход цифру, обозначающую день недели,
и проверяет, является ли этот день выходным.
"""

num = int(input('Enter a number: '))

if 1 <= num <= 5:
    print("Workday")
elif num == 6 or num == 7:
    print("Weekend")
else:
    print("It's not a day of the week!")

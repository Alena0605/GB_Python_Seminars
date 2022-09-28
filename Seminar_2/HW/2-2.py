"""
2. Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
"""

num = int(input('Enter a number: '))
result = 1

for i in range(1, num + 1):
    result *= i
    print(result, end=' ')

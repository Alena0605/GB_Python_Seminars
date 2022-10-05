"""
3. Напишите программу, которая будет преобразовывать десятичное число в двоичное.
Без использования встроенной функции преобразования, без строк.
"""

def convert_to_binary(number):
    ls = []

    while number:
        remainder = number % 2
        ls.append(remainder)
        number //= 2
    
    print(*ls[::-1], sep="")


num = int(input("Enter a number: "))
convert_to_binary(num)

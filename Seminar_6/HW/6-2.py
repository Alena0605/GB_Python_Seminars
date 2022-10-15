"""
2. Для чисел в пределах от 20 до N найти числа, кратные 20 или 21. Use comprehension.
"""

def multiple(number):
    if number < 20:
        return "Error! Enter a number more than 20."
    
    result = [num for num in range(20, number + 1) if num % 20 == 0 or num % 21 == 0]
    return result


num = int(input("Enter a number: "))
print(multiple(num))

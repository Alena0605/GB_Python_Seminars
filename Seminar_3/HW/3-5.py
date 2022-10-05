"""
5. ** Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
"""

def fib_negafib_nums(number):
    fib_nums_list = [1, 0, 1]

    if number == 1 or num == 2:
        return fib_nums_list
    
    for i in range(2, number + 1):
        size = len(fib_nums_list) - 1
        fib = fib_nums_list[size - 1] + fib_nums_list[size]
        fib_nums_list.append(fib)
        fib_nums_list.insert(0, fib) if i % 2 != 0 else fib_nums_list.insert(0, -fib)

    return fib_nums_list


num = int(input("Enter a number: "))
func = fib_negafib_nums(num)

print(*func)

"""
5. Напишите программу, которая принимает на вход координаты двух точек
и находит расстояние между ними в 2D пространстве.
"""

x_1 = int(input('Enter X for A: '))
y_1 = int(input('Enter Y for A: '))
x_2 = int(input('Enter X for B: '))
y_2 = int(input('Enter Y for B: '))

distance = ((x_2 - x_1) ** 2 + (y_2 - y_1) ** 2) ** 0.5

print(f'A ({x_1}, {y_1}); B ({x_2}, {y_2}) = {round(distance, 3)}')

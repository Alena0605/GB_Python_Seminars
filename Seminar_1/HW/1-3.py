"""
3. Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0
и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).
"""

x = int(input('Enter X: '))
y = int(input('Enter Y: '))

if x > 0 and y > 0:
    print('1')
elif x < 0 < y:
    print('2')
elif x < 0 and y < 0:
    print('3')
elif y < 0 < x:
    print('4')
else:
    print('Error, 0 entered!')

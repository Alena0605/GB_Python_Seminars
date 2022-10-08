"""
2. Найдите корни квадратного уравнения Ax² + Bx + C = 0, с помощью модуля. Запросите значения А, В, С 3 раза. 
Уравнения и корни запишите в файл.
"""

from math import sqrt

a = int(input("Enter A: "))
b = int(input("Enter B: "))
c = int(input("Enter C: "))

d = b ** 2 - 4 * a * c

with open('quadratic.txt', "a", encoding="utf-8") as f:
    f.write(f"Квадратное уравнение: {a}*x^2 + {b}*x + {c}\n")
    if d > 0 and a:
        x1 = round((-b + sqrt(d)) / (2 * a), 2)
        x2 = round((-b - sqrt(d)) / (2 * a), 2)
        f.writelines(f"Корни уравнения: {x1}, {x2}\n")
    elif d == 0:
        x = round(-b / (2 * a), 2)
        f.writelines(f"Корень: {x}\n")
    else:
        f.writelines("Корней нет\n")

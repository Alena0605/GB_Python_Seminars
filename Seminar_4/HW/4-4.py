"""
4.* Задана натуральная степень k. Сформировать случайным образом список коэффициентов (от 0 до 10) многочлена, 
записать в файл полученный многочлен не менее 3-х раз.
"""

from random import choice


def make_equation(power):
    if power <= 0:
        return "Error! Enter a positive number."
    
    equation = ""
    nums_list = range(0, 10)

    with open("equations.txt", "a", encoding="utf-8") as f:
        while power > 0:
            coef = choice(nums_list)
            sign = choice(["+", "-"])
            
            if coef:
                equation += f"{coef}*x^{power} {sign} "

            power -= 1

        f.write(f"{equation}{choice(nums_list)} = 0\n")

    return "The equation is added in file equations.txt"

k = int(input("Enter a power: "))
print(make_equation(k))

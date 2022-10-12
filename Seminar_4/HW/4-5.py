"""
5. ** Даны два файла, в каждом из которых находится запись многочленов. 
Задача - сформировать файл, содержащий сумму многочленов.
"""

from random import choice


def equations_sum(name_1: str, name_2: str):
    with open(name_1, "r", encoding="utf-8") as f_1, \
            open(name_2, "r", encoding="utf-8") as f_2:
        first = f_1.readlines()
        second = f_2.readlines()

        if len(first) == len(second):
            with open("sum_equations.txt", "a", encoding="utf-8") as f_3:
                for i, v in enumerate(first):
                    f_3.write(f"{v[:-5]} + {second[i]}")
        else:
            print("The contents of the files do not match!")


equations_sum("equations.txt", "equations_2.txt")

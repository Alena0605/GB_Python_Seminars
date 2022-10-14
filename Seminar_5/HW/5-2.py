"""
2. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
Входные и выходные данные хранятся в отдельных текстовых файлах.
"""

from os import path


def file_compression(file_1: str, file_2: str):
    if path.exists(file_1):
        with open(file_1, "r", encoding="utf-8") as f_1, \
                open(file_2, "a", encoding="utf-8") as f_2:
            result = ''
            count = 1
            lines = f_1.readlines()
            for line in lines:
                for i in range(len(line) - 1):
                    if line[i] == line[i + 1]:
                        count += 1
                    else:
                        result += f"{count}{line[i]}"
                        count = 1
                result += "\n"
            f_2.write(result)
            return f"The data are written into the file '{file_2}'."
    else:
        return f"Error! File '{file_1}' does not exist."


def file_recovery(file: str):
    if path.exists(file):
        with open(file, "r", encoding="utf-8") as f:
            result = ''
            lines = f.readlines()
            for line in lines:
                for i in range(len(line)):
                    if line[i].isdigit() and line[i + 1].isalpha() and not line[i - 1].isdigit():
                        result += f"{int(line[i]) * line[i + 1]}"
                    elif line[i].isdigit() and line[i + 1].isdigit():
                        num = line[i] + line[i + 1]
                        result += f"{int(num) * line[i + 2]}"
                result += "\n"
            return result
    else:
        return f"Error! File '{file}' does not exist."


file1 = input("Enter the name of the file with the text: ")
file2 = input("Enter the file name to record: ")
file3 = input("Enter the name of the file to decode: ")

print(file_compression(file1, file2))
print(file_recovery(file3))

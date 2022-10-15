"""
3. Написать функцию: аргументы — имена сотрудников, возвращает словарь, 
ключи — первые буквы имён, значения — списки, содержащие имена, начинающиеся с соответствующей буквы.
"""

def get_names_dict(names):
    names_dict = {}

    for name in sorted(names):
        first_letter = name[0]
        if first_letter in names_dict.keys() and name not in names_dict[first_letter]:
            names_dict[first_letter] += [name]
        else:
            names_dict[first_letter] = [name]
    
    return names_dict


names_list = input("Enter some names separated by space: ").split()
print(get_names_dict(names_list))

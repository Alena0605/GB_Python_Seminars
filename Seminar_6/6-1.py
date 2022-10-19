"""
1. Напишите программу вычисления арифметического выражения заданного строкой.
Используйте операции +, -, /, *. Приоритет операций стандартный.
* Добавьте скобки, приоритет операций меняется.

(!!! Незаконченный вариант)
"""

def calc_equation(equation: str):
    ls = equation.split()
    prior = {"(": 1, ")": 1, "*": 2, "/": 2, "+": 3, "-": 3}
    actions = {
        "*": lambda x, y: float(x) * float(y),
        "/": lambda x, y: float(x) / float(y),
        "+": lambda x, y: float(x) + float(y),
        "-": lambda x, y: float(x) - float(y)
    }
    order = []
    
    for i in ls:
        if i in prior:
            order.append(prior[i])
        else:
            order.append("")
    
    cur = order[1]

    for k, l in enumerate(order):
        if isinstance(l, int) and l < cur:
            index = k
            cur = l
    
    cur_res = actions[ls[index]](ls[index - 1], ls[index + 1])
    del ls[index - 1:index + 2]
    ls.insert(index - 1, cur_res)
    print(ls)


eq = '2 + 6 * 5'
calc_equation(eq)

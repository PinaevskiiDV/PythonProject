import re

expr = input("Запишите арифметическое выражение: ")

math_actions = {"^": lambda x, y: str(float(x)**float(y)),
  "*": lambda x, y: str(float(x) * float(y)),
  "/": lambda x, y: str(float(x) / float(y)),
  "+": lambda x, y: str(float(x) + float(y)),
  "-": lambda x, y: str(float(x) - float(y))}

priority_reg_exp = r"\((.+?)\)"
action_reg_exp = r"(-?\d+(?:\.\d+)?)\s*\{}\s*(-?\d+(?:\.\d+)?)"



def calc(expresion: str) -> str:

    while (match := re.search(priority_reg_exp, expresion)):
        expresion: str = expresion.replace(match.group(0), calc(match.group(1)))

    for symbol, action in math_actions.items():
        while (match := re.search(action_reg_exp.format(symbol), expresion)):
            expresion: str = expresion.replace(match.group(0), action(*match.groups()))

    return expresion



print(f"Ответ: {calc(expr)}")
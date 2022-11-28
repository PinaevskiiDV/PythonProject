def Numbers(x):
    xyz = ["X", "Y", "Z"]
    a = []
    for i in range(x):
        a.append(input(f"Введите значение {xyz[i]}: "))
    return a


def result_predicate(x):
    left = not (x[0] or x[1] or x[2])
    right = not x[0] and not x[1] and not x[2]
    result = left == right
    return result


element = Numbers(3)

if result_predicate(element) == True:
    print(f"Утверждение истинно")
else:
    print(f"Утверждение ложно")
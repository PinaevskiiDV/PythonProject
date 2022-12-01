stroka = str(float(input("Введите вещественное число:")))
sum = 0
for i in stroka:
    if i == ".":
        i = 0
    sum += int(i)
print (sum)

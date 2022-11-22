x = int(input("Введите x:"))
y = int(input("Введите y:"))
if x == 0 or y == 0:
    print("точка находится на линии вектора")
elif x > 0 and y > 0:
    print ("1")
elif x > 0 and y < 0:
    print ("2")
elif x < 0 and y < 0:
    print ("3")
else:
    print ("4")
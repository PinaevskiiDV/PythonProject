quarter = int(input("Введите номер четверти:"))
if quarter < 1 or quarter > 4:
    print("Четверть отсутствует в системе координат")
elif quarter == 1:
    print ("x > 0; y > 0")
elif quarter == 2:
    print ("x < 0; y > 0")
elif quarter == 3:
    print ("x < 0; y < 0")
else:
    print ("x > 0; y < 0")
import time

a = int(input("Введите нижнюю границу:"))
b = int(input("Введите верхнюю границу:"))
random_num = int((time.time() % 1) *(b - a) + a)
print(random_num)

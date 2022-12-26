# print ("Игра 2021 конфета.")
# pool = 121

# count = 1
# while pool >= 0:
#     if count == 1:
#         move1 = int(input("Ход Игрока №1:"))
#         if move1 < 1 or move1 > 28:
#             print ("Возьмите от 1 до 28 конфет!")
#         elif move1 > pool:
#             print (f"Возьмите от 1 до {pool} конфет!")
#         else:
#             pool -= move1
#             print (f"Осталось {pool} конфет")
#             count -= 1
#     elif count == 0:
#         move2 = int(input("Ход Игрока №2:"))
#         if move2 < 1 or move2 > 28:
#             print ("Возьмите от 1 до 28 конфет!")
#         elif move2 > pool:
#             print (f"Возьмите от 1 до {pool} конфет!")
#         else:
#             pool -= move2
#             print (f"Осталось {pool} конфет")
#             count += 1
# if count == 0:
#     print ("Все конфеты достаются Игроку №1")
# else:
#     print ("Все конфеты достаются Игроку №2")









# import random

# print ("Игра 2021 конфета.")
# pool = 121

# count = 1
# while pool >= 1:
#     if count == 1:
#         move1 = int(input("Ход Игрока №1:"))
#         if move1 < 1 or move1 > 28:
#             print ("Возьмите от 1 до 28 конфет!")
#         elif move1 > pool:
#             print (f"Возьмите от 1 до {pool} конфет!")
#         else:
#             pool -= move1
#             print (f"Осталось {pool} конфет")
#             count -= 1
#     elif count == 0:
#         if 29 < pool <= 58:
#             move2 = pool - 29
#         elif pool >= 59 or pool == 29:
#             move2 = random.randint (1, 28)
#         else:
#             move2 = pool
#         print (f"Ход Компьютера: {move2}")
#         pool -= move2
#         print (f"Осталось {pool} конфет(а)")
#         count += 1
# if count == 0:
#     print ("Все конфеты достаются Игроку №1")
# else:
#     print ("Все конфеты достаются Компьютеру")



import random

print ("Игра 2021 конфета.")
pool = 121

count = 1
while pool >= 1:
    if count == 1:
        move1 = int(input("Ход Игрока №1:"))
        if move1 < 1 or move1 > 28:
            print ("Возьмите от 1 до 28 конфет!")
        elif move1 > pool:
            print (f"Возьмите от 1 до {pool} конфет!")
        else:
            pool -= move1
            print (f"Осталось {pool} конфет")
            count -= 1
    elif count == 0:
        if pool >= 28:
            if pool % 29 == 0:
                move2 = random.randint (1, 28)
            else:
                move2 = pool % 29
            print (f"Ход Компьютера: {move2}")
        else:
            move2 = pool
            print (f"Ход Компьютера: {move2}")
        pool -= move2
        print (f"Осталось {pool} конфет")
        count += 1
if count == 0:
    print ("Все конфеты достаются Игроку №1")
else:
    print ("Все конфеты достаются Компьютеру")



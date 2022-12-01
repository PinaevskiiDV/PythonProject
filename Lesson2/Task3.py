n = int(input("Введите число:"))
dictionary = {}
sum = 0
for i in range(1, n+1):
    dictionary[i] = (1 + (1/n))**n
    sum += dictionary[i]
print (round(sum, 2))
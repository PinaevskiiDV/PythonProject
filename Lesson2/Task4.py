
# with open('file.txt', 'a') as data:
#     data.write('1\n')
#     data.write('2\n')
#     data.write('3\n')

n = int(input("Введите число N:"))
number_list = []
for i in range (-n, n + 1):
    number_list.append(i)
print (number_list)
result = 1
path = 'file.txt'
data = open(path, 'r')
for i in data:
    result *= number_list[int(i)]
data.close()
print (result)
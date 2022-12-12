num = int(input())

bin_num = ''
while num > 0:
    bin_num = str(num % 2) + bin_num
    num = num // 2
print(bin_num)
num_list = [1.1, 1.2, 3.1, 5.1, 10.01]

for i in range(len(num_list)):
    num_list[i] %= 1

print (round (max(num_list) - min(num_list), 2))



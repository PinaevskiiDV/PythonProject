num_list = [2, 3, 5, 9, 3]
product_of_numbers = []
for i in range(int(len(num_list) / 2) + 1):
    product_of_numbers.append (num_list[i] * num_list[-i - 1])

print (product_of_numbers)
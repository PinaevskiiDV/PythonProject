def compression(file):
    count = 1
    code = ''
    for i in range(len(file)-1):
        if file[i] == file[i+1]:
            count += 1
        else:
            code = code + str(count) + file[i]
            count = 1
    if count >1 or (file[len(file) - 2] != file[-1]):
        code = code + str(count) + file[-1]
    return code

def inflation(file):
    num = ''
    result = ''
    for i in range(len(file)):
        if file[i].isdigit():
            num = file[i]
        else:
            result = result + file[i] * int(num)
    return result

txt = input("Введите текст: ")

print (f"Сжатый текст: {compression(txt)}")

print (f"Восстановленный текст: {inflation(compression(txt))}")
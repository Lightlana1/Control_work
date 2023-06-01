string = input('Введите элементы массива:')
txt = string.split()

print (txt)

result =[]

for words in txt:
    if len(words) > 3:
        continue
    result.append(words)

print(' '.join(result), ' - новый массив')
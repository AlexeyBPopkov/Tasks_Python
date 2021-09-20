# Создаем файл 'old.txt' с произвольным содержимым и закрываем его
with open('old.txt','w') as out:
    out.write('abcde\n12345\n67890')

# Считываем содержимое созданного файла 'old.txt' и выводим на экран
with open('old.txt','r') as input:
    data = input.read()
    print(data)

# Записываем в обратном порядке в файл 'new.txt'
with open('new.txt','w') as out:
    out.write(data[::-1])

# Считываем содержимое созданного файла 'new.txt' и выводим на экран
with open('new.txt','r') as input:
    print(input.read())
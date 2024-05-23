import random

link = 'https://discord.gift/'
chars = '+-abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
number = input('количество ссылок? / number of links?'+ "\n")
length = input('длина ссылок? / link length? (24 стандарт / 24 default)'+ "\n")
number = int(number)
length = int(length)
for n in range(number):
    password =''
    for i in range(length):
        password += random.choice(chars)
    write = link + password
    with open("nitrologs.txt", "a") as file:
        file.write( write + '\n')
 
print("Файл записан / file is recorded")

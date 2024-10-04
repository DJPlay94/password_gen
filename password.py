from random import choice

symbol = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
pass_len = int(input("Введите длину пароля\n"))
password = ''

for i in range(pass_len):
    password += choice(symbol)

print(f"Ваш пароль - {password}")
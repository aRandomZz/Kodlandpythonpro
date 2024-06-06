import random as r
password="+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
user_pwordl= input('Introduce la longitud de la contraseña\n')
while True:
    if user_pwordl.isdigit() == False:
        user_pwordl= input('Introduce un dígito\n')
    elif int(user_pwordl)<5:
        user_pwordl= input('Introduce un número más largo\n')
    else:
        break
user_pword=''
for i in range(int(user_pwordl)):
    x= r.choice(password)
    user_pword+= x

print(f'Esta es tu contraseña: {user_pword}')

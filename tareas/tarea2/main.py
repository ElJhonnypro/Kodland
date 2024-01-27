import random

characters = '+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'

try:
    num = int(input('Que tan larga quieras la contraseña? ->  '))
    if num is None:
        print('Error necesita poner un numero')
        exit(1)
except ValueError:
    print('Intruduzca un numero valido, Error:', ValueError)

print(characters[71])
def createpassword(longitud):
    password = ''
    for i in range(longitud):
        try:
            password += random.choice(characters)
        except IndexError as error:
            print('Error de longitud (bug)', error)
    return password

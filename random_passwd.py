import random
try:
    num = int(input("Introduce un número de 8 a 64: "))
except ValueError:
    print("Incorrect value introduced!")
    exit()
except:
    print("Something went wrong")
    exit()


def get_random(num):
    char = '!#$%&()*+,-./0123456789?@ABCDEFGHIJKLMNOPQRSTUVWXYZ_abcdefghijklmnopqrstuvwxyz'
    passwd = ''
    for n in range(num):
        passwd += char[random.randint(0, len(char)-1)]

    return passwd


print(get_random(num))

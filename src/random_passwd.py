import random

# Define user custom errors
# define Python user-defined exceptions


class Error(Exception):
    """Base class for other exceptions"""
    pass


class not_valid_num(Error):
    """Raised when the input number is not valid"""
    pass


def random_passwd(num):
    try:
        if num < 8 or num > 64:
            raise not_valid_num

        char = '!#$%&()*+,-./0123456789?@ABCDEFGHIJKLMNOPQRSTUVWXYZ_abcdefghijklmnopqrstuvwxyz'
        passwd = ''
        for n in range(num):
            passwd += char[random.randint(0, len(char)-1)]

        return passwd
    except not_valid_num:
        print("The input value is not valid. Please introduce a number between 8 and 64")
        # exit()
    except ValueError:
        print("Incorrect value introduced!")
        # exit()
    except:
        print("Something went wrong")
        # exit()


def random_pin(num):
    try:
        if num < 4 or num > 8:
            raise not_valid_num

        char = '0123456789'
        pin = ''
        for n in range(num):
            pin += char[random.randint(0, len(char)-1)]

        return pin
    except not_valid_num:
        print("The input value is not valid. Please introduce a number between 8 and 64")
        # exit()
    except ValueError:
        print("Incorrect value introduced!")
        # exit()
    except:
        print("Something went wrong")
        # exit()

# TODO: Write a program that generates a random number between 1 and 10 and lets the user guess what number was
#  generated. The result should be sent back to the user via a print statement.

import random

number_random = random.randint(1, 10)
number_user = input('Введите число от 1 до 10: ')
if number_user.isdigit():
    if number_random == int(number_user):
        print(f'Вы угадали число, которое загадал компьютер. Оно равняется {number_random}.')
    else:
        print(f'Вы не угадали число загаданное компьютером. Оно равняется {number_random}.')
else:
    print('Введите число.')

# TODO: Write a program that asks the answer for a mathematical expression, checks whether the user is right or
#  wrong, and then responds with a message accordingly.
import random
a = random.randint(1, 10)
b = random.randint(1, 10)
print(f'Число а равняется {a}')
print(f'Число b равняется {b}')
f_q = a + b  # first question
s_q = a - b  # second question
t_q = a * b  # third question
fo_q = a // b  # fourth question
f_a = (input("Введите сумму чисел a и b: "))  # first answer
s_a = (input("Введите разность чисел а и b: "))  # second answer
t_a = (input("Введите произведение чисел a и b: "))  # third answer
fo_a = (input("Введите целое число от деления a и b: "))  # fourth answer
if f_a.isdigit() and s_a.isdigit() and t_a.isdigit() and f_a.isdigit():
    f_a = int(f_a)
    s_a = int(s_a)
    t_a = int(t_a)
    fo_a = int(fo_a)
    if f_q == f_a and s_q == s_a and t_q == t_a and fo_q == fo_a:
        print('Правильные ответы на все вопросы. Вывод ответов будет в порядке: компьютер - пользователь.')
        print(f'Сумма - {f_q} и {f_a}, разность - {s_q} и {s_a}, произведение - {t_q} и {t_a},', end='')
        print(f' целое число от деления - {fo_q} и {fo_a}')
    elif f_q != f_a or s_q != s_a or t_q != t_a or fo_q != fo_a:
        print("Где-то есть ошибка. Вывод ответов будет в порядке: компьютер - пользователь.")
        print(f'Сумма - {f_q} и {f_a},разность - {s_q} и {s_a},произведение - {t_q} и {t_a},', end='')
        print(f' целое число от деления - {fo_q} и {fo_a}.')
else:
    print("Необходимо вводить только целые числа. Перезапустите программу и повторите попытку.")

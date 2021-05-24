# TODO: Write a program that takes your name as input, and then your age as input and greets you with the following:
#  “Hello <name>, on your next birthday you’ll be <age+1> years”

user_name = input("Введите ваше имя: ")
user_age = input("Введите ваш возраст: ")
if user_age.isdigit() and user_name.isalpha():
    print(f'Привет, {user_name}. В следующий день рождения тебе исполнится {int(user_age) + 1} лет.')
else:
    print('Введите возраст цифрами и повторите попытку.')

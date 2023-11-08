import random


def is_valid(num):
    if num.isdigit():
        return 100 >= int(num) >= 1
    else:
        return False


def main_circle(num):
    print('пиши до 100')
    new_num = input()
    if is_valid(new_num):
        if num == int(new_num):
            print('красава')
        elif num > int(new_num):
            print('больше пиши')
            main_circle(num)
        elif num < int(new_num):
            print('меньше пиши')
            main_circle(num)
    else:
        print('нормальено напиши')
        main_circle(num)


n = random.randint(1, 100)

print('Добро пожаловать в числовую угадайку')
main_circle(n)




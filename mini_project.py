# a = int(input('Введите первое число: '))
# b = int(input('Введите второе число: '))
# op = input('Введите тип операции: ')
# if op == '+':
#     print(a + b)
# if op == '-':
#     print(a - b)
# if op == '*':
#     print(a * b)
# if op == '/':
#     if b == 0:
#         print('На ноль делить нельзя')
#     else:
#         print(a / b)


import random

user_answer = input('Камень, ножницы или бумага?')
tool = ['камень', 'ножницы', 'бумага']
n = random.choice(tool)

while (user_answer != 'камень') and (user_answer != 'бумага') and (user_answer != 'ножницы'):
    user_answer = input('Камень, ножницы или бумага?')

if (n == 'камень' and user_answer == 'камень') or (n == 'ножницы' and user_answer == 'ножницы') or (n == 'бумага' and user_answer == 'бумага'):
    print(f'Ничья, компьютер тоже сходил {n}')
if (n == 'камень' and user_answer == 'ножницы') or (n == 'ножницы' and user_answer == 'бумага') or (n == 'бумага' and user_answer == 'камень'):
    print(f'Победил компьютер, он сходил {n}')
if (user_answer == 'камень' and n == 'ножницы') or (user_answer == 'ножницы' and n == 'бумага') or (user_answer == 'бумага' and n == 'камень'):
    print(f'Ты победил, компьютер сходил {n}')

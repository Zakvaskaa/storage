import random
number = random.randint(1, 100)
token = 0
num_guest = 0
attempt = 0
while True:
    print('Угадай число')
    num_guest = int(input('Выбери от 1 до 100: '))
    attempt += 1
    if num_guest == number:
        token += 10
        print('Вы угадали c', attempt, 'попытки, и получили 10 очков!')
        print('Ваш счет:', token)
        break
    if attempt > 9:
        print('Вы проиграли, я загадал число', number)
        break
    elif num_guest > number:
        print('Это число должно быть меньше!')
    elif num_guest < number:
        print('Это число должно быть больше!')
    else:

        break
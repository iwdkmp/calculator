print ('хай, это супер калькулятор☺')
count = 0
while count != 1:
    first_number = int(input('Введите первое число: '))
    second_number = int(input('Введите второе число: '))
    mathematical_action = input('Введите действие которое хотите выполнить (доступны + - * /) : ')
    if mathematical_action == '+':
        print('Ответ: ' "%.2f" % (first_number+second_number))
        count += 1
    elif mathematical_action == '-':
        print('Ответ: ' "%.2f" % (first_number-second_number))
        count += 1
    elif mathematical_action == '*':
        print('Ответ: ' "%.2f" % (first_number*second_number))
        count += 1
    elif mathematical_action == '/':
        print('Ответ: '"%.2f" % (first_number/second_number))
    else:
        print('Попробуйте еще раз. Возможно вы неправильно ввели операцию или число. ')

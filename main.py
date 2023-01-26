print ('хай, это супер калькулятор☺')
first_number = float(input('Введите первое число: '))
second_number = float(input('Введите второе число: '))
mathematical_action = input('Введите действие которое хотите выполнить (доступны + - * /) : ')
if mathematical_action == '+':
    print ('Ответ: ' "%.2f" % (first_number+second_number))
elif mathematical_action == '-':
    print ('Ответ: ' "%.2f" % (first_number-second_number))
elif mathematical_action == '*':
    print ('Ответ: ' "%.2f" % (first_number*second_number))
else:
    print ('Ответ: '"%.2f" % (first_number/second_number))
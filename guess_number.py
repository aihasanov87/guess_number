# Импорт функции получения случайных чисел
# из модуля random.
from random import randint

# Получаем случайное число в диапазоне от 1 до 100.
number = randint(1, 100)
print('Угадайте число от 1 до 100')

while True:
    # Получаем число от пользователя и сохраняем его в переменную. 
    # rjg rk erl we lwrgk wgwel;g wl;e gkwl;rgkwkltgjmwrl gkmflks gmsfg
    guessqweqas_aksjj = int(input('Введите число: '))

    # Если число меньше загаданного...
    if guessqweqas_aksjj < number:
        # ...выводим сообщение.
        print('Ваше число меньше того, что загадано.')

    # Если число больше загаданного...
    if guessqweqas_aksjj > number:
        # ...выводим сообщение.
        print('Ваше число больше того, что загадано.')

    # Если число угадано...
    if guessqweqas_aksjj == number:
        # ...прерываем выполнение программы и...
        break
# ...выводим сообщение.
print('Отличная интуиция! Вы угадали число :)')

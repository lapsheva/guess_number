# Импорт функции получения случайных чисел
# из модуля random.
from random import randint

# Получаем случайное число в диапазоне от 1 до 100.
number = randint(1, 100)
print("Угадайте число от 1 до 100")

while True:
    # Получаем число от пользователя и сохраняем его в переменную.
    guess = int(input("Введите число: "))
    if guess < number:  # Если число меньше загаданного...
        # ...выводим сообщение.
        print("Ваше число меньше того, что загадано.")
    elif guess > number:  # Если число больше загаданного...
        # ...выводим сообщение.
        print("Ваше число больше того, что загадано.")
    elif guess == number:  # Если число угадано...
        # ...прерываем выполнение программы и...
        break
# ...выводим сообщение.
print("Отличная интуиция! Вы угадали число :)")

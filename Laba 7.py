import random

numbers = random.sample(range(1, 100), 5)

user_input = input("Введите число от 1 до 100: ")

try:
    user_number = int(user_input)

    if user_number in numbers:
        message = "Поздравляю, Вы угадали число!"
    else:
        message = "Нет такого числа!"

    print("Список чисел:", numbers)
    print("Ваше число:", user_number)
    print(message)

except ValueError:
    print("Пожалуйста, введите корректное число.")
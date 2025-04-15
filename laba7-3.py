days = ("Пн", "Вт", "Ср", "Чт", "Пт", "Сб", "Вс")

vvod = input("Насколько сильно вы хотите умереть от переутомления? (от 0 до 7): ")

try:
    chill = int(vvod)

    if 0 <= chill <= 7:
        chilldays = list(days[-chill:]) if chill > 0 else []
        workdays = list(days[:-chill]) if chill > 0 else list(days)

        print("Ваши выходные дни:", chilldays , ", Босс")
        print("Ваши рабочие дни:", workdays , ", Босс")
    else:
        print("Пожалуйста, введите число от 0 до 7.")

except ValueError:
    print("Некорректный ввод. Введите целое число от 0 до 7.")
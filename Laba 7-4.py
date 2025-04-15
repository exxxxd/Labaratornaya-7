    gr1 = ["asd", "qwe", "zxc", "rty", "fgh", "vbn", "uio", "jkl", "mkl", "k"]
    g2gr2 = ["qaz", "wsx", "edc", "rvf", "tgb", "yhn", "ujm", "iop", "gkj", "wer"]
    team1 = tuple(random.sample(gr1, 5))
    team2 = tuple(random.sample(gr2, 5))
    team = team1 + team2

    print(f"Наша группа: {gr1}\nДругая группа: {gr2}\nКоманда: {team}\nДлина кортежа: {len(team)} ")

    alphteam = tuple(sorted(team))
    print("Отсортированная по алфавиту команда:", alphteam)

    a = team.count("a")
    if a > 0:
        print(f"Фамилия 'a' есть в команде, встречается {a} раз.")
    else:
        print("Фамилии 'a' нет в команде.")
while True:
    log = input("Введите логин: ")
    pas = input("Введите пароль: ")
    if log != "Murat.bg" or pas != "12234456good":
        print("Неверный логин или пароль!")
    else:
        print("Добро пожаловать, Богдан")
        break

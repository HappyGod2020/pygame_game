log = input("Введите логин: ")
pas = input("Введите пароль: ")
while True:
    if log != "Murat.bg" or pas != "12234456good":
        print("Неверный логин или пароль!")
        log = input("Введите логин: ")
        pas = input("Введите пароль: ")
    else:
        print("Добро пожаловать, Богдан")
    break

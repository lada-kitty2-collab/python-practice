# Gate Simulator
gate_open = False
while True:
    card = "Приложить карту"
    push = "Пройти"
    exit = "Выход"
    answer = input(f"{card}").upper()
    if answer == "OK":
        gate_open = True
        print(f"Турникет открыт, проходите")
    elif answer == "NO":
        gate_open = False
        print("Приложите карту")
    answer = input(f"{push}")
    if answer == "OK":
        print("Вы прошли, турникет закрыт")
        gate_open = False
        answer = input(f"{exit}?").upper()
        if answer == "OK":
            break

# ATM simulator
# Simple console program with while loop, conditions and input
while True:
    atm = "Банкомат"
    pin_code = "ПИН-код"
    try_again = "Попробуйте снова"
    balance = "Просмотр баланса"
    withdraw = "Снять деньги"
    insufficient_funds = "Недостаточно средств"
    successfully = "Снятие денег прошло успешно"
    exit = "Выход"
    answer = input(f"Введитe {pin_code}")
    if answer == "OK":
        pin_code = True
        options = input(f"Выберите опцию: {balance}, {withdraw}, {exit}")
        if options == exit:
            break
        elif options == balance:
            print("На Вашем балансе ... средств")
        elif options == withdraw:
            other = input(f"Сколько Вы хотите снять?")
            if other == successfully:
                withdraw = True
                decision = input(f"{successfully}, {exit}?")
                if decision == "OK":
                    break
                else:
                    print(f"Нажмите {exit}")
            if other == insufficient_funds:
                withdraw == False
                print(f"{insufficient_funds}, {try_again}")
    elif answer == "NO":
        pin_code = False
        print(f"Введите ПИН-код")

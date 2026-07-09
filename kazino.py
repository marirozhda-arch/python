import random

balance = 0
action = 0
replenish = 0
bet = -1
computer_number1 = 0
computer_number2 = 0
computer_number3 = 0
income = 0
current_income = 0
number_games = 0
number_wins = 0



print("вы зашли в игру 'Однорукий бандит'")
print(f"на вашем счету: {balance}")
print()

while action != 4:

    print("ГЛАВНОЕ МЕНЮ")
    print("выберите действие (от 1 до 4)")
    print("1 - показать баланс")
    print("2 - пополнить баланс")
    print("3 - сыграть")
    print("4 - вывести деньги и закончить игру")
    print()
    print()
    print()

    action = int(input())
    
    if action == 1:
        action = 0
        print(f"ваш баланс составляет {balance}")
        print( )
        print()
        print()
    elif action == 2:
        action = 0
        while replenish <= 0:
            replenish = int(input("введите сумму на которую вы хотите пополнить свой баланс(она должна превышать число 0): "))
            if replenish <= 0:
                print("а я всегда знал что бандиты тупые")
                print("ладно давай по новой")
            else:
                balance += replenish
                print(f"хорощо теперь ваш баланс равен: {balance}")
                print()
                print()
                print()
        replenish = 0
    elif action == 3:
        action = 0
        if balance <= 0:
            print("ваш баланс отрицательный или равен 0 его надо пополнить")
            while replenish <= 0:
                replenish = int(input("введите сумму на которую вы хотите пополнить свой баланс(она должна превышать число 0): "))
                if replenish <= 0:
                    print("а я всегда знал что бандиты тупые")
                    print("ладно давай по новой")
                else:
                    balance += replenish
                    print(f"хорошо теперь ваш баланс равен: {balance}")
                    print()
                    print()
                    print()
            replenish = 0
        else:
            while bet <= 0 or bet > balance :
                bet = int(input("введите сумму своей ставки(она не должна превышать значения вашего баланса а также не быть меньше или равной 0): "))
                print()
                print()
                if bet <= 0:
                    print("а я всегда знал что бандиты тупые")
                    print("твоя ставка меньше или равна 0 а такого не должно быть")
                    print("ладно давай по новой")
                    print()
                elif bet > balance:
                    print("а я всегда знал что бандиты тупые")
                    print("твоя ставка больше баланса а такого не должно быть")
                    print("ладно давай по новой")
                    print()
                else:
                    income = 0

                    computer_number1 = random.randint(1,9)
                    computer_number2 = random.randint(1,9)
                    computer_number3 = random.randint(1,9)

                    print(f"выпали числа: {computer_number1} {computer_number2} {computer_number3}")
                    print()
                    print()
                    if computer_number1 == computer_number2 == computer_number3:
                        print("ура в славили 3 одинаковых числа! ваша ставка умножилась на 5 и уже начислена на ваш баланс")
                        income = bet * 5
                        balance += income
                        number_wins += 1
                    elif computer_number1 == computer_number2 or computer_number1 == computer_number3 or computer_number3 == computer_number2:
                        print("ура в славили 2 одинаковых числа! ваша ставка умножилась на 2 и уже начислена на ваш баланс")
                        income = bet * 2
                        balance += income
                        number_wins += 1
                    elif computer_number1 == 7 and computer_number2 == 7 and computer_number3 == 7:
                        print("невероятный джек пот 'Хакари' ваша ставка умножилась на 100 и уже начислена на ваш баланс")
                        income = bet * 100
                        balance += income
                        number_wins += 1
                    else:
                        balance -= bet
                        income -= bet
                        print("ксожалению сегодна вам не повезло и из вашего баланса вычетается ваша ставка МУХАХА")
                        

                
                    current_income += income
                    print()
                    print()
                    if income < 0:
                        print(f"ты получил по ебалу а именно проеб {income * (-1)}")
                    else:
                        print(f"за эту игру вы получили {income}")
                
                    print()
                    print()

                    print(f"теперь ваш баланс составляет {balance}")
                    print()
                    print()
                    number_games += 1
                    income = 0
                break
            bet = 0
            

    elif action != 4:
        print("введи нормально")
 
print(f"вы вывели {balance}")
print(f"сегодня вы сыграли {number_games} раз")
print(f"сегодня вы выиграли {number_wins} раз")
print(f"а заработали {current_income}")
print("игра завершена приходите к нам еще")




            
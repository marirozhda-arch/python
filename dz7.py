player_name = 'player_name'
player_hp = 100
monstr_hp = 50
max_piayer_hp = 100
max_monstr_hp = 50
player_action = 0
monstr_damage = 10
player_damage = 20
heal_amount = 20
heals_left = 0
turn_number = 0
defending = 0
plaeyr_attacks_count = 0
plaeyr_heals_count = 0
winner = 'winner'

print("Привет ты попал в игру 'Бой с монстром'")
player_name = str(input("введи свое имя: "))
print(f"твои параметры: \n  здоровье - {max_piayer_hp} \n  сила урона - {player_damage} \n  сила восстановления - {heal_amount} \n")
print(f"параметры монстра: \n  здоровье - {max_monstr_hp} \n  сила урона - {monstr_damage} \n ")
print("а теперь В БОООЙ \n \n \n")

while player_hp > 0 and monstr_hp > 0:
    print("выберете действие:")
    print(" 1 - атака \n 2 - защита \n 3 - лечение")
    player_action = 0 
    
    while player_action != 1 and player_action != 2 and player_action != 3:
        player_action = int(input())
        if player_action != 1 and player_action != 2 and player_action != 3:
            print("ну мы же в прошлой игре это проходили \n давай вводи нормально")
        else:
            if player_action == 1:
                monstr_hp -= player_damage
                player_hp -= monstr_damage
                plaeyr_attacks_count += 1
                print(f"вы атаовли монстра и снесли ему {player_damage} xp")
                print(f"монстрор тоже атаковал тебя и снес тебе {monstr_damage}")
            elif player_action == 2:
                defending += 1
                print("монстор атаковал тебя но ты успел защитить себя щитом")
            else:
                player_hp += heal_amount
                player_hp -= monstr_damage
                plaeyr_heals_count += 1
                print(f"ты подлечился на {heal_amount}")
                print(f"монстрор тоже атаковал тебя и снес тебе {monstr_damage}")
            
            print(f"твое здоровье - {player_hp}")
            winner = "монстр"
            if monstr_hp < 0:
                print(f"здоровье монстра - 0")
                winner = player_name
            else:
                print(f"здоровье монстра - {monstr_hp}")
            
print(f"выиграл: {winner} ")       

        
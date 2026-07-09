import random

orig_word = ""
podskazka = ''
player_word = ''
name = ""
city = ""
ALPHABET = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
player_alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
pole = ['ключ',350,450,'*2',500,850,'п',600,1000,500,350,'+',1000,'б',750,350,600,"+",400,'п',800,350,450,500,600, 400,550,850,450,0,1000,500,'+',400,750,600]
rand = 0
shkatulka = 0
rand_shkatulka = 0
balance = 0
bukva = ''
q = ''

orig_word = str(input("введите слово: ")).lower()
podskazka = input("введите подсказку: ")


print()
print("Якубович: Здравствуйте дорогие гости и телезрители! Это программа 'Поле чудес'. Встречаем нашего сегодневшего игрока!")

name = input("Вы: Здравствуйте меня зовут ")
city = input("Вы: Я из города ")

print("Якубович: И так, начинаем игру ")
print(f"Якубович:  И сегодня у нас слово из {(len(orig_word))} букв")

player_word = "_" * (len(orig_word))
print(player_word)

print(f"Якубович: А вот и подсказка: {podskazka}")


while player_word != orig_word:
    print("Якубович: ВРАЩАЙТЕ БАРАБАН!!!")

    rand = random.randint(0, len(pole))
    print(rand)

    if rand == 0 or rand == 3 or rand == 11 or rand == 17 or rand == 32:
        print(f"Якубович: Сектор {pole[rand]} на барабане!")

        if rand == 0:
            shkatulka = int(input("Якубович: Выбираем шкатулку. 1 или 2?       "))
            rand_shkatulka = random.randint(1, 1000)

            if rand_shkatulka > 500:
                print("Якубович: Ха-ха-ха! Ничего нет!")
                print(f"ваш баланс: {balance}")
            else:
                print("Якубович: Ого! 1000 баллов!")
                balance += 1000
                print(f"ваш баланс: {balance}")

        elif rand == 3:
            print("Якубович: Ваши баллы умножаются на два")
            balance = balance * 2
            print(f"ваш баланс: {balance}")
        
        else:# узнать что такое сектор +
            print()

    elif rand == 6 or rand == 13 or rand == 19:
        print(f"Якубович: Буква '{pole[rand]}'")

        for i in range(0, len(orig_word) + 1):
            if pole[rand] == orig_word[i]:
                #узнать метот который изменяет значение по индексу(для слова) и по значению(для алфавита)
                
                print()

    else:
        print(f"Якубович: {pole[rand]} очков на барабане!")
        print("Якубович: Буква")
        bukva = input("Вы: Буква ")
        for i in range(0, len(orig_word) + 1):
            if orig_word[i] == bukva:
                print()
                #узнать метот который изменяет значение по индексу(для слова) и по значению(для алфавита)

        print('Якубович: Хотите назвать слово целиком?')
        q = input("Вы: ").lower()

        if q == 'да':
            print("Якубович: Ну попробуйте")
            q = input("Вы: Это слово ").lower()
            if q == orig_word:
                print("Якубович: И у нас ПОБЕДИТЕЛЬ!")
            else:
                print("Якубович: Неверно")
        else:
            print("Якубович: Продолжаем")


        


            



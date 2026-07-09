def process_state_start():
    global global_current_state
    print("Добро пожаловать в кинотеатр 'Питон-Синема'!")
    print("Здесь можно посмотреть фильмы, купить билет и выбрать закуски.")
    print()
    input("Для продолжения нажмите Enter.")
    global_current_state = STATE_MAIN_MENU 

def process_state_main_menu():

    print("Главное меню")
    print()
    print("1) Посмотреть фильмы")
    print("2) Купить билет")
    print("3) Посмотреть закуски и напитки")
    print("4) Посмотреть мой билет")
    print("0) Выйти из программы")

    is_correct_input = False
    while is_correct_input == False:
        try:
            main_menu = int(input("Введите введите номер действия: "))

            if main_menu >= 0 and main_menu <= 4:
                is_correct_input = True
            else:
                print("Ошибка. Такого действия нет.")
        except:
            print("Ошибка. Вы ввели не число.")    
    global global_current_state
    if main_menu == 1:
        global_current_state = STATE_MOVIES_LIST
    elif main_menu == 2:
        global_current_state = STATE_BUY_TICKET
    elif main_menu == 3:
        global_current_state = STATE_SNACKS_MENU
    elif main_menu == 4:
        global_current_state = STATE_MY_TICKET
    elif main_menu == 0:
        global_current_state = STATE_EXIT

def process_state_movies_list():
    global global_current_state
    print("Список фильмов")
    print()
    for i in range(4):
        for j in range(5):
            print(f" {movies[i][j]}", end="")

        print()

    print()
    input("Нажмите Enter, чтобы вернуться в главное меню.")
    global_current_state = STATE_MAIN_MENU

def process_state_buy_ticket():
    print("Список фильмов")
    print()
    for i in range(4):
        for j in range(5):
            print(f" {movies[i][j]}", end="")

        print()
    
    is_correct_input = False
    while is_correct_input == False:
        try:
            input_movies = int(input("Введите введите номер фильма: "))

            if input_movies >= 1 and input_movies <= 4:
                is_correct_input = True
            else:
                print("Ошибка. Такого фильма нет.")
        except:
            print("Ошибка. Вы ввели не число.")
        
        name = input("Введите своё имя: ")

    is_correct_input = False
    while is_correct_input == False:
        try:
            count_ticket = int(input("Введите введите колличество билетов: "))

            if count_ticket >= 1:
                is_correct_input = True
            else:
                print("Ошибка. Нельзя купить 0 билетов.")
        except:
            print("Ошибка. Вы ввели не число.")

    if input_movies == 1:
        sum_maney = movies[input_movies - 1][3] * count_ticket
    elif input_movies == 2:
        sum_maney = movies[input_movies - 1][3] * count_ticket
    elif input_movies == 3:
        sum_maney = movies[input_movies - 1][3] * count_ticket
    elif input_movies == 4:
        sum_maney = movies[input_movies - 1][3] * count_ticket
    
    global global_ticket
    global_ticket = [name, movies[input_movies][1], count_ticket, sum_maney]

    print("Билет куплен!")
    print()
    print(f"Зритель: {global_ticket[0]}")
    print(f"Фильм: {global_ticket[1]}")
    print(f"Количество билетов: {global_ticket[2]}")
    print(f"Итого: {global_ticket[3]} руб.")

    global global_current_state
    global_current_state = STATE_MAIN_MENU
    global ticket
    ticket += 1

def process_state_snacks_menu():
    global global_current_state
    print("Закуски и напитки")
    print()
    for i in range(4):
        for j in range(4):
            print(f" {snacks[i][j]}", end="")

        print()

    print()
    input("Нажмите Enter, чтобы вернуться в главное меню.")
    global_current_state = STATE_MAIN_MENU

def process_state_my_ticket():
    global global_current_state
    if ticket == 0:
        print("Вы пока не купили билет.")
        
    else:
        print("Ваш билет")
        print()
        print(f"Зритель: {global_ticket[0]}")
        print(f"Фильм: {global_ticket[1]}")
        print(f"Количество билетов: {global_ticket[2]}")
        print(f"Итого: {global_ticket[3]} руб.")

    global_current_state = STATE_MAIN_MENU

def process_state_exit():
    print("Спасибо, что пользовались системой кинотеатра.")
    print("До свидания!")

STATE_START = 1
STATE_MAIN_MENU = 2
STATE_MOVIES_LIST = 3
STATE_BUY_TICKET = 4
STATE_SNACKS_MENU = 5
STATE_MY_TICKET = 6
STATE_EXIT = 0
ticket = 0
global_current_state = STATE_START

movies = [
["1)","Человек-паук", "фантастика", 350,"руб."],
["2)","Холодное сердце", "мультфильм", 300,"руб."],
["3)","Интерстеллар", "фантастика", 400,"руб."],
["4)","Один дома", "комедия", 250,"руб."]
]

snacks = [
["1)","Попкорн маленький", 180,"руб."],
["2)","Попкорн большой", 300,"руб."],
["3)","Кола", 150,"руб."],
["4)","Начос", 220,"руб."]
]

process = True

while process == True:
    if global_current_state == STATE_START:
        process_state_start()
    elif global_current_state == STATE_MAIN_MENU:
        process_state_main_menu()
    elif global_current_state == STATE_MOVIES_LIST:
        process_state_movies_list()
    elif global_current_state == STATE_BUY_TICKET:
        process_state_buy_ticket()
    elif global_current_state == STATE_SNACKS_MENU:
        process_state_snacks_menu()
    elif global_current_state == STATE_MY_TICKET:
        process_state_my_ticket()
    elif global_current_state == STATE_EXIT:
        process_state_exit()
        process = False




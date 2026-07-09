print("Выбираем первый язык программирования")
print("Оттветь на вопрсы")
print("Отвечайте только да или нет")
answer1 = str(input("Хочешь много зарабатывать? "))



if answer1 == "да":
    answer2 = str(input("Вы тупой?"))
    if answer2 == "да":
        answer21 = str(input("Очень?"))
        if answer21 == "да":
            answer31 = str(input("У вас есть друзья?"))
            if answer31 == "да":
                answer311 = str(input("Они тоже тупые?"))
                if answer311 == 'да':
                    print("JvaScript")
                else:
                    print("Ruby")
            else:
                print("PHP")    
        else:
            answer32 = str(input("Вы насмотрелись уроков ХАУДИ ХО?"))
            if answer32 == "да":
                print("Python")
            else:
                answer322 = str(input("Вам нравится Windows?"))
                if answer322 == "да":
                    print("C#")
                else:
                    answer3222 = str(input("Вы пи**р?"))
                    if answer3222 == "да":
                        print("Swift")
                    else:
                        print("Perl")
    else:
        answer214 = str(input("Вы инженер?"))
        if answer214 == "да":
            answer211 = str(input("Вым больше 50?"))
            if answer211 == "да":
                print("Fortan")
            else:
                print("MatLab")
        else:
            answer212 = str(input("У вас есть ноги?"))
            if answer212 == "да":
                answer213 = str(input("да"))
                if answer213 == "да":
                    print("Java")
                else:
                    print("C++")
            else:
                print("C")
elif answer1 == "нет":
    print("Ваш язык: Delphi")
else:
    print("ты дебил говори только да или нет")
text = ""

with open("input.txt", "r", encoding="utf-8") as file_in:
    text = file_in.read()

max_percent = 0
max_letter = ""

with open("output.txt", "r", encoding="utf-8") as file_:

    for letter in "абвгдеёжзийклмнопрстуфхцчшщъыьэюя":
        percent_letter_in_text = text.count(letter) / len(text) * 100
        print(f"количество букв {letter} в тексте = {percent_letter_in_text:.2f}%")

        if percent_letter_in_text > max_percent:
            max_percent = percent_letter_in_text
            max_letter = letter


print(f"max_letter = {max_letter} percent = {max_percent:.2f}%")
# import os

def show_menu() -> int:
    print()
    print("1. Вывод всего справочника")
    print("2. Поиск номера телефона по фамилии абонента")
    print("3. Поиск абонента по номеру телефона")
    print("4. Добавить запись в справочник")
    print("5. Сохранить справочник в файл")
    print("6. Закончить работу")
    print("Выберите необходимое действие:")
    return int(input())

def read_csv(filename: str) -> list:
    data = []
    fields = ["Фамилия", "Имя", "Телефон", "Описание"]
    with open(filename, 'r', encoding='utf-8') as fin:
        for line in fin:
            record = dict(zip(fields, line.strip().split(',')))
            data.append(record)
    return data

def find_number(pb: list, name: str) -> int:
    records = list(filter(lambda rec: rec, pb))

def print_phone_book(pb: list):
    fields = ["Фамилия", "Имя", "Телефон", "Описание"]
    
phone_book = read_csv('phon.txt')
while True:
    choice = show_menu()
    match choice:
        case 1:
            print(phone_book)
        case 6:
            break
        case _:
            continue

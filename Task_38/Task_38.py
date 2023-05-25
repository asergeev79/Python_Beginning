# import os

def show_menu(menu: list) -> int:
    print()
    for i in range(len(menu)):
        print(F"{i + 1} {menu[i]}")
    print("Выберите пункт меню:")
    return int(input())

def read_csv(filename: str) -> list:
    data = []
    with open(filename, 'r', encoding='utf-8') as fin:
        for line in fin:
            data.append(line.strip().split(','))
    
    fields = data[0]
    data = list(map(lambda rec: dict(zip(fields, rec)), data))
#    data[0] = fields
    return data

def find_record(pb: list, field: str, name: str) -> list:
    return list(filter(lambda item: item[field].upper() == name.upper(), pb))

def new_record() -> dict:
    fields = ["Фамилия", "Имя", "Телефон", "Описание"]
    record = dict()
    print('Введите фаимлию абонента')
    record[fields[0]] = input()
    print('Введите имя абонента')
    record[fields[1]] = input()
    print('Введите телефон абонента')
    record[fields[2]] = input()
    print('Введите описание абонента')
    record[fields[3]] = input()
    return record

def print_phone_book(pb: list):
    fields = ["Фамилия", "Имя", "Телефон", "Описание"]

main_menu = ["Вывод всего справочника",
             "Поиск в справочнике",
             "Добавить запись в справочник",
             "Сохранить справочник в файл",
             "Закончить работу"
]
phone_book = read_csv('phon.txt')
if phone_book != []:
    while True:
        choice = show_menu(main_menu)
        match choice:
            case 1:
                print(phone_book)
            case 2:
                print("Поиск по полю справочника:")
                choice = show_menu(phone_book[0])
                print("Введите строку посика")
                surname = input()
                print(find_record(phone_book, phone_book[0][choice], surname))
            case 3:
                phone_book.append(new_record())
            case 6:
                break
            case _:
                continue
else:
    print("Файл справочника должен сожержать описание полей")

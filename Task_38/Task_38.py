#from tabulate import tabulate

# функция вывода меню с нумерацией пунктов
def show_menu(menu: list) -> int:
    print()
    for number,menu_rec in enumerate(menu,start=1):
        print(number,menu_rec)
    print("Выберите пункт меню:")
    return int(input())

# функция чтения справочника из файла
def read_csv(filename: str) -> tuple:
    with open(filename, 'r', encoding='utf-8') as fin:
        data = [line.rstrip().split(',') for line in fin]

    first_row = data.pop(0)
    data = list(map(lambda rec: dict(zip(first_row, rec)), data))
    
    return first_row,data

# функция поиска записи в справочнике по полю
def find_record(pb: list, field: str, name: str) -> list:
    return list(filter(lambda item: item[field].upper() == name.upper(), pb))

# функция создания новой записи справочника
def new_record(rec_fields: list) -> dict:
    record = dict()
    for field in rec_fields:
        print(f"Введите поле {field} абонента:")
        record[field] = input()
    return record

def del_record(pb: list, pos: int):
    pb.pop(pos)

def print_phone_book(pb: list, field_pb: list, view='brief'):
    if view == "brief":
        print(" ".join(field_pb))
        print("=======================")
        for num,item in enumerate(pb,start=1):
            print(num," ".join(list(item.values())))
    else:
        for num, pb_record in enumerate(pb, start=1):
            print(f"\n{num}:")
            for desc,item in pb_record.items():
                print(f"{desc}: {item}")

# функция записи справочника в файл
def save_phone_book(pb: list, filename: str):
    with open(filename, 'w', encoding='utf-8') as fout:
        fout.write(",".join(list(pb[0].keys())) + "\n")
        fout.write("\n".join(list(map(lambda item: ",".join(list(item.values())), pb))))

main_menu = ["Вывод всего справочника",
             "Поиск в справочнике",
             "Добавить запись в справочник",
             "Удалить запись из справочника",
             "Изменить запись в справочнике",
             "Сохранить справочник в файл",
             "Закончить работу"
]
fields,phone_book = read_csv('phon.txt')
if phone_book != []:
    while True:
        choice = show_menu(main_menu)
        match choice:
            case 1:
                print("Вывод справочника:")
                choice = show_menu(["краткий","полный"])
                print_phone_book(phone_book, fields) if choice == 1 else print_phone_book(phone_book, fields,'full')
            case 2:
                print("Поиск по полю справочника:")
                choice = show_menu(fields)
                print("Введите строку поиска")
                search_string = input()
                print_phone_book(find_record(phone_book, fields[choice - 1], search_string), fields)
            case 3:
                phone_book.append(new_record(fields))
            case 4:
                print_phone_book(phone_book, fields)
                print("Введите номер записи для удаления")
                del_record(phone_book, int(input()) - 1)
                print_phone_book(phone_book, fields)
            case 5:
                print_phone_book(phone_book, fields)
                print("Введите номер записи для изменения:")
                choice = int(input())
                choice_list = []
                choice_list.append(phone_book[choice - 1])
                print_phone_book(choice_list, fields)
                print("Введите поле для изменения:")
                choice_desc = show_menu(fields)
                print("Введите новое значение:")
                phone_book[choice - 1][fields[choice_desc - 1]] = input()                
                print_phone_book(choice_list, fields)
            case 6:
                save_phone_book(phone_book, "phone1.txt")
            case 7:
                break
            case _:
                continue
else:
    print("Файл справочника должен содержать описание полей")

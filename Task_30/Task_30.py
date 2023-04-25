"""
Задача 30:  Заполните массив элементами арифметической прогрессии. 
Её первый элемент, разность и количество элементов нужно ввести с клавиатуры. 
Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
Каждое число вводится с новой строки.
"""

def n_member_of_arith_progression(x, y, z):
    return x + (z - 1)*y

def arith_progression(x, y, z):
    list_temp = []
    list_temp.append(x)
    for i in range(1, z):
        list_temp.append(list_temp[-1] + y)
    return list_temp

a1 = int(input("Введите первый элемент арифметической прогрессии: "))
d = int(input("Введите разность арифметической прогрессии: "))
n = int(input("Введите число членов арифметической прогрессии: "))

list1 = [n_member_of_arith_progression(a1, d, i) for i in range(1, n + 1)]
list2 = arith_progression(a1, d, n)

print(list1)
print(list2)

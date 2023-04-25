"""
Задача 32: Определить индексы элементов массива (списка), 
значения которых принадлежат заданному диапазону 
(т.е. не меньше заданного минимума и не больше заданного максимума)
"""

import random

def create_list(n):
    return [random.randint(1, 20) for i in range(n)]

def list_index(list_n, left_border, right_border):
    return [i for i in range(len(list_n)) if left_border <= list_n[i] <= right_border]

size = int(input("Введите размер массива: "))
lb = int(input("Введите левую границу диапазона: "))
rb = int(input("Введите правую границу диапазона: "))
list1 = create_list(size)
list2 = list_index(list1, lb, rb)

print("Исходный массив:")
print(list1)
print("Массив индексов элементов из диапазона:")
print(list2)

"""
Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
Пользователь вводит 2 числа. 
n — кол-во элементов первого множества. 
m — кол-во элементов второго множества. 
Затем пользователь вводит сами элементы множеств.
"""

import random

size = int(input("Введите размер первого массива: "))
list_1 = [random.randint(1, 20) for i in range(size)]

size = int(input("Введите размер второго массива: "))
list_2 = [random.randint(1, 20) for i in range(size)]

print("Заданные массивы:")
print(list_1)
print(list_2)

print("Набор чисел, встречающихся в обоих наборах, по возрастанию:")
print(sorted(set(list_1).intersection(set(list_2))))

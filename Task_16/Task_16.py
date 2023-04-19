"""
Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. 
Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

*Пример:*

5
    1 2 3 4 5
    3
    -> 1
"""
import random

size = int(input("Введите размер массива: "))

list_n = [random.randint(1, 100) for i in range(size)]

print("Заданный массив:")
print(list_n)

x = int(input("Введите искомое число: "))

count = 0
for i in list_n:
    if i == x:
        count += 1

print(f"Число {x} встречается в массиве {count} раз")

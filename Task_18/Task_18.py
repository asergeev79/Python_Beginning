"""
Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. 
Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

*Пример:*

5
    1 2 3 4 5
    6
    -> 5
"""
import random

size = int(input("Введите размер массива: "))
list_n = []

for i in range(size):
    list_n.append(random.randint(1, 100))

print("Заданный массив:")
print(list_n)

x = int(input("Введите искомое число: "))

min_diff = abs(x - list_n[0])
x_diff = set()

for i in list_n:
    diff = abs(i - x)
    if diff < min_diff:
        x_diff = set()
        x_diff.add(i)
        min_diff = diff
    elif diff == min_diff:
        x_diff.add(i)


print(f"Число/-а {x_diff} - ближайшее/-ие к {x}")

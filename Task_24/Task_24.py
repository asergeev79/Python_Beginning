"""
Задача 24: В фермерском хозяйстве в Карелии выращивают чернику. 
Она растёт на круглой грядке, причём кусты высажены только по окружности. 
Таким образом, у каждого куста есть ровно два соседних. Всего на грядке растёт N кустов.
Эти кусты обладают разной урожайностью, 
поэтому ко времени сбора на них выросло различное число ягод — на i-ом кусте выросло ai ягод.
В этом фермерском хозяйстве внедрена система автоматического сбора черники. 
Эта система состоит из управляющего модуля и нескольких собирающих модулей. 
Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом, 
собирает ягоды с этого куста и с двух соседних с ним.
Напишите программу для нахождения максимального числа ягод, 
которое может собрать за один заход собирающий модуль, 
находясь перед некоторым кустом заданной во входном файле грядки.
"""
import random

size = int(input("Введите размер грядки: ")) 
with open('Task_24.txt', "w") as f:
    list_n = [random.randint(1, 20) for i in range(size)]
    f.write(' '.join(str(list_1) for list_1 in list_n))

with open('Task_24.txt', "r") as f:
    list_m = list(map(int, f.readline().split()))

#print(list_n)
print(list_m)
list_sum3 = []
list_sum3.append(list_m[len(list_m) - 1] + list_m[0] + list_m[1])
for i in range(1, len(list_m) - 1):
    list_sum3.append(list_m[i - 1] + list_m[i] + list_m[i + 1])
list_sum3.append(list_m[len(list_m) - 2] + list_m[len(list_m) - 1] + list_m[0])

#print(list_sum3)
print(f"Максимальное число ягод за один раз - {max(list_sum3)}")

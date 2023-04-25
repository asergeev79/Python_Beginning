"""
Задача 26:  Напишите программу, которая на вход принимает два числа A и B, 
и возводит число А в целую степень B с помощью рекурсии.

*Пример:*

A = 3; B = 5 -> 243 (3⁵)
    A = 2; B = 3 -> 8 
"""

def power_recusrsion(x, y):
    if y == 0:
        return 1 
    return x * power_recusrsion(x, y - 1)


a = int(input("Введите основание степени: "))
b = int(input("Введите степень: "))

print(f"{a} в степени {b}:")
print(f"-> {power_recusrsion(a, b)}")

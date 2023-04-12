"""
Задача 10: 
На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. 
Определите минимальное число монеток, которые нужно перевернуть, 
чтобы все монетки были повернуты вверх одной и той же стороной. 
Выведите минимальное количество монет, которые нужно перевернуть
"""

n_coins = int(input("Введите количество монет: "))
print("Введите по порядку монеты, где 0 - решка, 1 - орёл")
sum_coins = 0
for i in range(n_coins):
    sum_coins += int(input(f"{i + 1}-я монета: "))
print("Минимальное кол-во монет, которое нужно перевернуть, чтобы они были повёрнуты одной стороной -")
print(sum_coins) if sum_coins <= n_coins // 2 else print(n_coins - sum_coins)

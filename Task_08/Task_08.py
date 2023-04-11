"""
Задача 8: 
Требуется определить, 
можно ли от шоколадки размером n × m долек отломить k долек, 
если разрешается сделать один разлом по прямой между дольками 
(то есть разломить шоколадку на два прямоугольника).

*Пример:*

3 2 4 -> yes
3 2 1 -> no
"""

print("Введите размер шоколадки N x M")
n_chocolate = int(input("N: "))
m_chocolate = int(input("M: "))

print("Сколько долек шоколадки надо отломить?")
k_slice = int(input("K: "))

if k_slice % n_chocolate == 0 or k_slice %m_chocolate == 0:
    print("Отломить одним разломом удастся")
    print(f"{n_chocolate} {m_chocolate} {k_slice} -> yes")
else:
    print("Отломить одним разломом не удастся")
    print(f"{n_chocolate} {m_chocolate} {k_slice} -> no")

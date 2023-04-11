"""
Задача 6: 
Вы пользуетесь общественным транспортом? 
Вероятно, вы расплачивались за проезд и получали билет с номером. 
Счастливым билетом называют такой билет с шестизначным номером, 
где сумма первых трех цифр равна сумме последних трех. 
Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. 
Вам требуется написать программу, которая проверяет счастливость билета.

*Пример:*

385916 -> yes
123456 -> no
"""

ticket = input("Введите номер билета: ")
if (len(ticket)) != 6:
    print("Номер билета должен быть шестизначным!")
else:
    ticket_left = int(ticket[:3])
    ticket_left_sum = ticket_left // 100 + ticket_left % 100 // 10 + ticket_left % 10
    ticket_right = int(ticket[-3:])
    ticket_right_sum = ticket_right // 100 + ticket_right % 100 // 10 + ticket_right % 10
    print (f"{ticket} -> yes") if ticket_left_sum == ticket_right_sum else print (f"{ticket} -> no")

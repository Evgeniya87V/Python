"""
Задача 2: Найдите сумму цифр трехзначного числа.

*Пример:*
123 -> 6 (1 + 2 + 3)
100 -> 1 (1 + 0 + 0) 
"""
#Решение 1
#i = input()

#print(int(i[0])+int(i[1])+int(i[2]))

#Решение 2
num = int(input("Введите трехзначное число: "))

# Получение цифр числа
digit1 = num // 100
digit2 = (num % 100) // 10
digit3 = num % 10

# Вычисление суммы цифр
sum_of_digits = digit1 + digit2 + digit3
print(f"Сумма цифр числа {num} равна {sum_of_digits}")

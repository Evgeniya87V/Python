"""
a = 123
b = 1.23
print(a)
print(b)

value = None
a = 123
b = 1.23
print(a)
print(b)
value = 1234
print(value)

a = 3
b = 11
s = 2022
print(a, b, s)
print(a,'-', b,'-', s)
print('{} - {} - {}'.format(a,b,s))
print(f'first - {a} second - {b} third - {s}')

print("Введите первое число:")
a = input()
b = input("Введите второе число:")
print(a, ' + ', b, ' = ', a + b)

n = 1.345
print(int(n)) # Отбрасывается дробная часть вне зависимости больше 0.5 или
#меньше
m = '345'
print(m * 2) # При умножении строки на число, она повторяется столько раз на
#какое была умножена
print(int(m) * 2)

a = 1.43425
b = 2.2983
c = round(a * b, 5) # 3,29633
print(c)
"""
"""
iter = 2
iter += 3 # iter = iter + 3
iter -= 4 # iter = iter - 4
iter *= 5 # iter = iter * 5
iter /= 5 # iter = iter / 5
iter //= 5 # iter = iter // 5
iter %= 5 # iter = iter % 5
iter **= 5 # iter = iter ** 5

a = 1 > 4
print(a) # False

a = 1 < 4 and 5 > 2
print(a) # True

a = 1 == 2
print(a) # False

a = 1 != 2
print(a) # True
"""

"""
username = input('Введите имя: ')
if username == 'Маша':
    print('Ура, это же МАША!')
elif username == 'Марина':
    print('Я так ждала Вас, Марина!')
elif username == 'Ильнар':
    print('Ильнар - топ)')
else:
    print('Привет, ', username)
"""

"""
n = int(input())
if n % 2 == 0 and n % 3 == 0:
    print('Число кратно 6')
if n % 5 == 0 and n % 3 == 0:
    print('Число кратно 15')
"""

"""
n = 423
summa = 0
while summa > 0:
    x = n % 10
    summa = summa + x
    n = n // 10
print(summa) # 9
"""

"""
i = 0
while i < 5:
    if i == 3:
        break
    i = i + 1
else:
    print('Пожалуй')
    print('хватит )')
print(i)

n = 423
summa = 0
while summa > 0:
x = n % 10
summa = summa + x
n = n // 10
else:
print('Пожалуй')
print('хватит )')
print(summa)
# Пожалуй
# хватит )
# 9

"""

"""
n = int(input())
flag = True
i = 2
while flag:
if n % i == 0: # если остаток при делении числа n на i равен 0
flag = False
print(i)
elif i > n // 2: # делить числа не может превышать введенное число, деленное
на 2
print(n)
flag = False
i += 1

"""
"""
r = range(5) # 0 1 2 3 4
r = range(2, 5) # 2 3 4
r = range(-5, 0) # ----
r = range(1, 10, 2) # 1 3 5 7
r = range(100, 0, -20) # 100 80 60 40 20
r = range(100, 0, -20) # range(100, 0, -20)
for i in r:
print(i)
# 100 80 60 40 20

"""




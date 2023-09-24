# Задание 1.
# Создайте несколько переменных разных типов.
# Проверьте к какому типу относятся созданные переменные.


# a = 344
# b = 'карч'
# c = True
# d = 43 / 12

# print(type(a))
# print(type(b))
# print(type(c))
# print(type(d))


# Задание 2.
# Создайте в переменной data список значений разных
# типов перечислив их через запятую внутри квадратных скобок. Для каждого элемента в цикле выведите:
# порядковый номер начиная с единицы значение адрес в памяти, размер в памяти,
# хэш объекта, результат проверки на целое число только если он положительный
# результат проверки на строку только если он положительный
# *Добавьте в список повторяющиеся элементы и сравните на результаты.

# import sys

# data = [123, 'текст', True, 5.45, 123]

# for idx, elem in enumerate(data, 1):
#     print(idx, elem, id(elem), sys.getsizeof(elem), hash(elem))
#     if isinstance(elem, int):
#         print('Целое число')
#     if isinstance(elem, str):
#         print('Строка')


# Задание 3. 
# Напишите программу, которая получает целое число
# и возвращает его двоичное, восьмеричное строковое представление.
# Функции bin и oct используйте для проверки своего результата.
# *Дополнительно
# Попробуйте избежать дублирования кода в преобразованиях к разным системам счисления
# Избегайте магических чисел
# Добавьте аннотацию типов где это возможно


# number = int(input())
# print(bin(number))
# print(oct(number))


# for i in [2, 8]:
#     n = number
#     res = ''
#     while n:
#         res = f'{n % i}' + res
#         n //= i
#     print(res)


# Задание 4.
# Напишите программу, которая вычисляет площадь круга и
# длину окружности по введённому диаметру.
# Диаметр не превышает 1000 у.е.
# Точность вычислений должна составлять
# не менее 42 знаков после запятой.

# import math
# import decimal

# decimal.getcontext().prec = 42
# def circle_diametr(dim):
#     return decimal.Decimal(math.pi) * pow((dim / 2), 2)

# def circumference(diametre):
#     return decimal.Decimal(math.pi) * diametre
# diametre = decimal.Decimal(input('Внесите диаметр, не более тысячи у.е.: '))

# print(circle_diametr(diametre))
# print(circumference(diametre))


# Задача 5.
# Напишите программу, которая решает квадратные уравнения
# даже если дискриминант отрицательный.
# Используйте комплексные числа для извлечения квадратного корня.

# import math

# #(b**2) - 4 * a * c this is diskriminant

# def diskriminant(a,b,c):
#     return pow(b,2) - 4 * a * c


# a = float(input("Ведите а:"))
# b = float(input("Ведите b:"))
# c = float(input("Ведите c:"))

# # print(diskriminant(a,b,c))

# dis = diskriminant(a,b,c)
# kor_dis = pow(diskriminant(a,b,c),0.5)

# if dis > 0:
#     print((-b+kor_dis)/(2*a))
#     print((-b-kor_dis)/(2*a))
# elif dis == 0:
#     print((-b-kor_dis)/(2*a))
# else:
#     print((-b+kor_dis)/(2*a))
#     print((-b-kor_dis)/(2*a))   


# Домашнее задание
# 2. Напишите программу, которая получает целое число и возвращает его шестнадцатеричное строковое представление.
# Функцию hex используйте для проверки своего результата.


# HEX_FACTOR = 16
# hex_data = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'a', 'b', 'c', 'd', 'e', 'f']

# def get_number_from_user() -> int:
#     enter = input('Input any integer number > 0: ')
#     return int(enter)

# def converter(number: int) -> str:
#     res: str = ''
#     while number > 0:
#         res = str(hex_data[number % HEX_FACTOR]) + res
#         number //= HEX_FACTOR
#     return res

# num = get_number_from_user()
# if isinstance(num, int):
#     print(converter(num))
# else:
#     print('Ошибка! Попробуй еще раз')
# print(hex(num)[2:])


# 3. Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем.
# Программа должна возвращать сумму и произведение* дробей.
# Для проверки своего кода используйте модуль fractions.

import re
import math
import fractions

fracs = list(map(int,re.split(" |/", input('Введите две дроби через /, а между дробями Пробел: '))))

sum_div = fracs[0] * fracs[3] + fracs[2] * fracs[1]
sum_denom = fracs[1] * fracs[3]
sum_nod = math.gcd(sum_div, sum_denom)
if sum_denom / sum_nod != 1:
    sum_fracs = str(int(sum_div / sum_nod)) + '/' + str(int(sum_denom / sum_nod))
else:
    sum_fracs = str(int(sum_div / sum_nod))

prod_div = fracs[0] * fracs[2]
prod_denom = fracs[1] * fracs[3]
prod_nod = math.gcd(prod_div, prod_denom)
if prod_denom / prod_nod != 1:
    prod_fracs = str(int(prod_div / prod_nod)) + '/' + str(int(prod_denom / prod_nod))
else:
    prod_fracs = str(int(prod_div / prod_nod))

print(sum_fracs, prod_fracs)

f1 = fractions.Fraction(fracs[0], fracs[1])
f2 = fractions.Fraction(fracs[2], fracs[3])
print(f1 + f2, f1 * f2)

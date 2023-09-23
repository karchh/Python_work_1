# a = int(input())
# b = int(input())
# c = int(input())
# disc = b**2 - 4*a*c
# x1 = (-b + disc**0.5) / (2*a)
# x2 = (-b - disc**0.5) / (2*a)
# print(x1, x2)


# 5 задача (готовая):
# сумма четных элементов от 1 до n исключая кратные е
# n = int(input())
# e = int(input())
# i = 1
# res = 0
# while i < n:
#     if i % e != 0 | i % 2 == 0:
#         res += i
#     i+=1
# print(res)

#задача 6 (вариант 1). напишите программу, которая запрашивает год и проверяет его на високосность
# year = int(input('Введите год: '))
# if (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0):
#     print('Год високосный')
# else:
#     print('Год не високосный')

# (вариант 2)
# year = int(input('Введите год: '))
# result = 'Год не високосный'
# if (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0):
#     result = 'Год високосный'
# print(result)

# (вариант 3)
# year = int(input('Введите год: '))
# small_year_cycle = 4
# middle_year_cycle = 100
# big_year_cycle = 400
# result = 'Год не високосный'
# if (year % small_year_cycle == 0) and (year % middle_year_cycle != 0) or (year % big_year_cycle == 0):
#     result = 'Год високосный'
# print(result)



# 2.Треугольник существует только тогда, когда сумма любых двух его сторон больше третьей.
# Дано a, b, c - стороны предполагаемого треугольника.
# Требуется сравнить длину каждого отрезка-стороны с суммой двух других.
# Если хотя бы в одном случае отрезок окажется больше суммы двух других, то треугольника с такими сторонами не существует.
# Отдельно сообщить является ли треугольник разносторонним, равнобедренным или равносторонним.

# print("Введите стороны треугольника: ")
# x = int(input("x: "))
# y = int(input("y: "))
# z = int(input("z: "))
# if x >= y+z or y >= x+z or z >= x+y: 
#     print("Треугольника с такими сторонами не существует") 
# else: 
#     print("Треугольник существует")
# if x == y == z:
# 	print("Треугольник равносторнний")
# elif x==y or y==z or z==x:
# 	print("Треугольник равнобедренный")
# else:
# 	print("Треугольник разносторонний")
 
#3. Напишите код, который запрашивает число и сообщает является ли оно простым или составным.
#Используйте правило для проверки: “Число является простым, если делится нацело только на единицу и на себя”.
#Сделайте ограничение на ввод отрицательных чисел и чисел больше 100 тысяч.

# MIN_LIMIT = 0
# MAX_LIMIT = 100000
# UNITY = 1
# MIN_PRIME_NUM = 2

# input_num = -1

# while not (MIN_LIMIT <= input_num <= MAX_LIMIT):
#     input_num = int(input('Введите целое число между: '))

# if input_num >= MIN_PRIME_NUM:
#     sum = 0
#     for i in range(UNITY, input_num + 1):
#         if input_num % i == 0:
#             sum += 1
#     if sum <= 2:
#         print(f'Число {input_num} простое')
#     else:
#         print(f'Число {input_num} составное')
# else:
#     print('Числа 0 и 1 не являются ни простыми, ни составными')

# 4. Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток. Программа
# должна подсказывать «больше» или «меньше» после каждой попытки. Для генерации случайного
# числа используйте код:
# from random import randint
# num = randint(LOWER_LIMIT, UPPER_LIMIT)

from random import randint

LOWER_LIMIT = 0
UPPER_LIMIT = 1000
ATTEMPT_COUNT = 10

num = randint(LOWER_LIMIT, UPPER_LIMIT)
print(f'Компьютер загадал целое число от {LOWER_LIMIT} до {UPPER_LIMIT}. Вам необходимо его угадать за {ATTEMPT_COUNT} попыток!')
count = 1
while count <= ATTEMPT_COUNT:
    print(f'Попытка {count}. Введите целое число: ')
    your_num = int(input())
    if your_num == num:
        print('В яблочко! Число угадано!!!')
        break
    elif num < your_num:
        print(f'Загаданное число меньше {your_num}')
    else:
        print(f'Загаданное число больше {your_num}')
    count += 1
else:
    print('Попытки закончились. Game Over!')


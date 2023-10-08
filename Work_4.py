# Задача 1. Напишите функцию для транспонирования матрицы

# matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# def print_matrix(input_matrix):
#     for column in input_matrix:
#         for row in column:
#             print(row, "\t", end="")
#         print()

# print_matrix(matrix)

# print()

# def matrix_transpositions(input_matrix):
#     new_matrix = []
#     list_in_matrix = []
#     count_start = 0
#     count_stop = 1
#     while count_start < len(matrix):
#         for column in input_matrix:
#             for row in column[count_start:count_stop:]:
#                 list_in_matrix.append(row)
#         new_matrix.append(list_in_matrix)
#         list_in_matrix = []
#         count_start += 1
#         count_stop += 1
#     return new_matrix

# print_matrix(matrix_transpositions(matrix))


# Задача 2. Напишите функцию принимающую на вход только ключевые параметры и возвращающую словарь,
# где ключ — значение переданного аргумента, а значение — имя аргумента.
# Если ключ не хешируем, используйте его строковое представление.

# def hashable_dicts(**kwargs):
#     reverse_dict = dict()
#     for key, value in kwargs.items():
#         if isinstance(value, (list, dict, set)):
#             value = str(value)
#         reverse_dict[value] = key
#     return reverse_dict


# print(hashable_dicts(ученики=["Денис", "Мария"], \
# друзья={1: "Борис", 2: "Илья", 3: "Роман"}))



# Задача 3. Возьмите задачу о банкомате из семинара 2. Разбейте её на отдельные операции — функции.
# Дополнительно сохраняйте все операции поступления и снятия средств в список.


bank = 0
count = 0
percent_take = 0.015
percent_add = 0.03
percent_tax = 0.01


def add_bank(cash: float) -> None:
    global bank
    global count
    bank += cash
    count += 1
    if count % 3 == 0:
        bank = bank + percent_add * bank
        print("начислены проценты в размере: ", percent_add * bank)

def take_bank(cash: float) -> None:
    global bank
    global count
    bank -= cash
    count += 1

    if cash*percent_take < 30:
        bank -= 30
        print("списаны проценты за обналичивание: ", 30)
    elif cash*percent_take > 600:
        bank -= 600
        print("списаны проценты за обналичивание: ", 600)
    else:
        bank -= cash * percent_take
        print("списаны проценты за обналичивание: ", cash * percent_take)
    if count % 3 == 0:
        bank = bank + percent_add * bank
        print("начислены проценты в размере: ", percent_add * bank)


def exit_bank():
    print("Рады вас видетеь снова!\n")
    exit()

def check_bank() -> int:
    while True:
        cash = int(input("Введите сумму опреации кратно 50\n"))
        if cash % 50 == 0:

            return cash


while True:
    action = input("1 - снять деньги\n2 - пополнить\n3 - баланс\n4 -выйти\n")

    if action == '1':
        if bank > 5_000_000:
            bank = bank - bank * percent_tax
            print ("списан налог на роскошь: ", bank * percent_tax)
        cash = check_bank()
        if cash < bank:
            take_bank(cash)
        else:
            print("no money\n")
        if bank > 5_000_000:
            bank = bank - bank * percent_tax
            print ("списан налог на роскошь: ", bank * percent_tax)
        print("Баланс = ", bank)
    elif action == '2':
        add_bank(check_bank())
        if bank > 5_000_000:
            bank = bank - bank * percent_tax
            print ("списан налог на роскошь: ", bank * percent_tax)
        print("Баланс = ", bank)
    elif action == '3':
        print("Баланс = ", bank)
    else:
        exit_bank()
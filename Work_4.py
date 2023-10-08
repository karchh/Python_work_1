# Напишите функцию для транспонирования матрицы

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


# Напишите функцию принимающую на вход только ключевые параметры и возвращающую словарь,
# где ключ — значение переданного аргумента, а значение — имя аргумента.
# Если ключ не хешируем, используйте его строковое представление.

def hashable_dicts(**kwargs):
    reverse_dict = dict()
    for key, value in kwargs.items():
        if isinstance(value, (list, dict, set)):
            value = str(value)
        reverse_dict[value] = key
    return reverse_dict


print(hashable_dicts(ученики=["Денис", "Мария"], \
друзья={1: "Борис", 2: "Илья", 3: "Роман"}))

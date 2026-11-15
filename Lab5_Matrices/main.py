# Лабораторная работа №5. Двумерные массивы и функции. Вариант 2
import random

def print_matrix(matrix):
    # Выводим строки матрицы по очереди.
    for row in matrix:
        print(" ".join("{:4d}".format(v) for v in row))

def count_columns_without_zero(matrix):
    # Считаем количество столбцов, в которых нет ни одного нуля.
    count = 0
    for col in range(len(matrix[0])):
        has_zero = False
        for row in range(len(matrix)):
            # Если найден ноль, столбец не подходит.
            if matrix[row][col] == 0:
                has_zero = True
                break
        if not has_zero:
            count += 1
    return count

def characteristic(row):
    # Характеристика строки — сумма положительных чётных элементов.
    total = 0
    for value in row:
        if value > 0 and value % 2 == 0:
            total += value
    return total

def sort_rows(matrix):
    # Копируем матрицу, чтобы исходный вариант остался доступен.
    result = [row[:] for row in matrix]
    # Сортируем строки по возрастанию характеристики методом обмена.
    for i in range(len(result) - 1):
        for j in range(len(result) - 1 - i):
            if characteristic(result[j]) > characteristic(result[j + 1]):
                # Меняем соседние строки местами.
                result[j], result[j + 1] = result[j + 1], result[j]
    return result

# Запрашиваем размеры прямоугольной матрицы.
rows = int(input("Количество строк: "))
cols = int(input("Количество столбцов: "))
if not (1 <= rows <= 20 and 1 <= cols <= 20):
    print("Размеры должны быть от 1 до 20.")
else:
    # Формируем целочисленную матрицу случайными значениями.
    matrix = [[random.randint(-9, 9) for _ in range(cols)] for _ in range(rows)]
    print("\nИсходная матрица:")
    print_matrix(matrix)
    # Выполняем пункт 1 варианта 2.
    print("\n1. Столбцов без нулей:", count_columns_without_zero(matrix))
    # Выполняем пункт 2 варианта 2.
    sorted_matrix = sort_rows(matrix)
    print("\n2. Строки по возрастанию характеристики:")
    print_matrix(sorted_matrix)
    for i, row in enumerate(sorted_matrix, 1):
        print("Характеристика строки {}: {}".format(i, characteristic(row)))

# Оставляем окно открытым при запуске двойным нажатием.
input("\nНажмите Enter для выхода...")

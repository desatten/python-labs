# Лабораторная работа №2. Задание 1, вариант 2.
# Вычисление значения функции, заданной графиком (вариант 2).
from math import sqrt


def calculate_y(x):
    """Вычисляет значение кусочно-заданной функции."""
    if x < -8:
        return -3.0
    elif x < -3:
        return 0.6 * x + 1.8
    elif x <= 3:
        return -sqrt(max(0.0, 9.0 - x * x))
    elif x < 5:
        return x - 3.0
    return 3.0


def main():
    print('Лабораторная работа №2 — задание 1, вариант 2')
    try:
        x = float(input('Введите значение X: '))
    except ValueError:
        print('Ошибка: необходимо ввести число.')
        return
    y = calculate_y(x)
    print(f'X = {x:.3f}; Y = {y:.3f}')


if __name__ == '__main__':
    main()

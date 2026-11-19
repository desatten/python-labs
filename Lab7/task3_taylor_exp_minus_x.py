# Лабораторная работа №7. Задание 3.
# График функции e^(-x), вычисляемой по ряду Тейлора с точностью 10^-3.
import math
import turtle as tr

EPS = 1e-3


def taylor_exp_minus_x(x, eps=EPS):
    """Сумма ряда 1 - x + x^2/2! - ... до достижения заданной точности."""
    term = 1.0
    total = term
    n = 1
    while True:
        term *= -x / n
        total += term
        if abs(term) < eps:
            return total
        n += 1
        if n > 10000:
            raise ArithmeticError('Не удалось достичь заданной точности.')


def main():
    print('Лабораторная работа №7 — задание 3')
    try:
        x_min = float(input('Начальное значение X: '))
        x_max = float(input('Конечное значение X: '))
        step = float(input('Шаг DX: '))
    except ValueError:
        print('Ошибка: введите числовые значения.')
        return
    if step <= 0 or x_min >= x_max:
        print('Ошибка: DX должен быть положительным, а X начальное меньше X конечного.')
        return

    count = max(2, int(math.ceil((x_max - x_min) / step)) + 1)
    xs = [x_min + i * step for i in range(count) if x_min + i * step <= x_max + step * 1e-9]
    if xs[-1] < x_max and x_max - xs[-1] < step * 1e-8:
        xs[-1] = x_max
    ys = [taylor_exp_minus_x(x) for x in xs]

    # Масштабируем график по введённому диапазону, чтобы он помещался в окне.
    y_min, y_max = min(0.0, min(ys)), max(ys)
    if math.isclose(y_min, y_max):
        y_max = y_min + 1.0
    margin_x = max((x_max - x_min) * 0.08, 0.2)
    margin_y = max((y_max - y_min) * 0.12, 0.2)

    tr.title('Лабораторная работа №7 — задание 3: ряд Тейлора')
    tr.setup(width=950, height=700)
    tr.setworldcoordinates(x_min - margin_x, y_min - margin_y,
                           x_max + margin_x, y_max + margin_y)
    tr.bgcolor('white')
    tr.speed(0)
    tr.hideturtle()
    tr.tracer(0, 0)

    # Координатные оси.
    tr.pensize(1)
    tr.pencolor('black')
    if y_min <= 0 <= y_max:
        tr.penup(); tr.goto(x_min - margin_x / 2, 0); tr.pendown()
        tr.goto(x_max + margin_x / 2, 0)
    if x_min <= 0 <= x_max:
        tr.penup(); tr.goto(0, y_min - margin_y / 2); tr.pendown()
        tr.goto(0, y_max + margin_y / 2)

    # Подписи графика.
    tr.penup()
    tr.goto(x_min, y_max + margin_y * 0.35)
    tr.write('y = e^(-x), ряд Тейлора, точность 10^-3', font=('Arial', 12, 'bold'))

    # Рисуем значения, вычисленные именно по ряду.
    tr.pencolor('blue')
    tr.pensize(2)
    tr.penup()
    tr.goto(xs[0], ys[0])
    tr.pendown()
    for x, y in zip(xs[1:], ys[1:]):
        tr.goto(x, y)

    # Контрольная кривая точной функции для визуального сравнения.
    tr.pencolor('red')
    tr.pensize(1)
    tr.penup()
    samples = 500
    for i in range(samples + 1):
        x = x_min + (x_max - x_min) * i / samples
        y = math.exp(-x)
        if i == 0:
            tr.goto(x, y)
            tr.pendown()
        else:
            tr.goto(x, y)
    tr.penup()
    tr.goto(x_min, y_min - margin_y * 0.65)
    tr.write('Синий — сумма ряда; красный — e^(-x) для сравнения', font=('Arial', 10, 'normal'))

    print('   X          Сумма ряда       exp(-X)')
    for x, y in zip(xs, ys):
        print(f'{x:8.3f}   {y:14.8f}   {math.exp(-x):14.8f}')
    tr.update()
    tr.done()


if __name__ == '__main__':
    main()

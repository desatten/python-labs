import random
import turtle as tr

N = 10000
X_MIN, X_MAX = -2.5, 2.5
Y_MIN, Y_MAX = -2.5, 2.5

INSIDE_COLOR = "green"
OUTSIDE_COLORS = ["red", "blue", "orange", "purple", "magenta", "cyan", "brown", "gold"]

UPPER_POLYGON = [
    (-2.0, 0.0),
    (2.0, 2.0),
    (0.0, 0.0),
]
LOWER_POLYGON = [
    (0.0, 0.0),
    (2.0, 0.0),
    (1.0, -2.0),
]


def point_in_polygon(x, y, polygon):
    """Алгоритм луча: True, если точка внутри многоугольника или на границе."""
    eps = 1e-10
    inside = False
    count = len(polygon)

    for i in range(count):
        x1, y1 = polygon[i]
        x2, y2 = polygon[(i + 1) % count]

        # Проверка принадлежности точки отрезку (граница включается).
        cross = (x - x1) * (y2 - y1) - (y - y1) * (x2 - x1)
        dot = (x - x1) * (x - x2) + (y - y1) * (y - y2)
        if abs(cross) <= eps and dot <= eps:
            return True

        # Пересечение горизонтального луча с ребром.
        if (y1 > y) != (y2 > y):
            x_intersection = x1 + (y - y1) * (x2 - x1) / (y2 - y1)
            if x < x_intersection:
                inside = not inside

    return inside


def is_hit(x, y):
    return (point_in_polygon(x, y, UPPER_POLYGON)
            or point_in_polygon(x, y, LOWER_POLYGON))


def polygon_area(polygon):
    """Площадь многоугольника по формуле Гаусса (shoelace)."""
    s = 0.0
    for i, (x1, y1) in enumerate(polygon):
        x2, y2 = polygon[(i + 1) % len(polygon)]
        s += x1 * y2 - x2 * y1
    return abs(s) / 2


def draw_polygon(polygon):
    tr.penup()
    tr.goto(polygon[0])
    tr.pendown()
    for vertex in polygon[1:]:
        tr.goto(vertex)
    tr.goto(polygon[0])
    tr.penup()


def main():
    hits = 0
    points = []

    for _ in range(N):
        x = random.uniform(X_MIN, X_MAX)
        y = random.uniform(Y_MIN, Y_MAX)
        hit = is_hit(x, y)
        hits += int(hit)
        points.append((x, y, hit))

    rectangle_area = (X_MAX - X_MIN) * (Y_MAX - Y_MIN)
    estimate = hits / N * rectangle_area
    exact = polygon_area(UPPER_POLYGON) + polygon_area(LOWER_POLYGON)
    error = abs(estimate - exact) / exact * 100 if exact else 0.0

    tr.title("Лабораторная работа №7 — задание 2")
    tr.setup(width=900, height=760)
    tr.setworldcoordinates(X_MIN - 0.5, Y_MIN - 1.0, X_MAX + 0.5, Y_MAX + 1.0)
    tr.bgcolor("white")
    tr.hideturtle()
    tr.speed(0)
    tr.tracer(0, 0)

    # Сначала рисуются контуры областей.
    tr.pensize(2)
    tr.pencolor("black")
    draw_polygon(UPPER_POLYGON)
    draw_polygon(LOWER_POLYGON)

    # Классификация точки и цвет используют одну и ту же функцию is_hit().
    for x, y, hit in points:
        color = INSIDE_COLOR if hit else random.choice(OUTSIDE_COLORS)
        tr.goto(x, y)
        tr.dot(3, color)

    tr.penup()
    tr.goto(X_MIN - 0.35, Y_MIN - 0.72)
    tr.write(f"N = {N}; попаданий = {hits}; оценка площади = {estimate:.4f}",
             font=("Arial", 11, "normal"))
    tr.goto(X_MIN - 0.35, Y_MIN - 0.92)
    tr.write(f"Реальная площадь = {exact:.4f}; относительная ошибка = {error:.2f}%",
             font=("Arial", 11, "normal"))

    print(f"Испытаний: {N}; попаданий: {hits}")
    print(f"Оценка площади: {estimate:.6f}; реальная площадь: {exact:.6f}")
    print(f"Относительная ошибка: {error:.2f}%")

    tr.update()
    tr.done()


if __name__ == "__main__":
    main()

# Лабораторная работа №7. Задание 2. Метод Монте-Карло, вариант 2.
# Область составлена из четверти круга во II четверти и нижнего треугольника
# (геометрия функции is_hit перенесена из исходной работы студента).
import random
import turtle as tr

N = 10000
X_MIN, X_MAX = -2.5, 2.5
Y_MIN, Y_MAX = -2.5, 2.5

def is_hit(x, y):
    in_upper_part = x <= 0 and y >= 0 and x*x + y*y <= 4
    in_lower_part = x >= 0 and y <= 0 and y >= -2*x and y >= 2*x-4
    return in_upper_part or in_lower_part

def real_area():
    # Четверть круга радиуса 2 плюс треугольник с основанием 2 и высотой 2.
    return 3.141592653589793 + 2.0

def main():
    hits=0
    points=[]
    for _ in range(N):
        x=random.uniform(X_MIN,X_MAX); y=random.uniform(Y_MIN,Y_MAX)
        hit=is_hit(x,y); hits += int(hit); points.append((x,y,hit))
    rectangle_area=(X_MAX-X_MIN)*(Y_MAX-Y_MIN)
    estimate=hits/N*rectangle_area
    exact=real_area()
    error=abs(estimate-exact)/exact*100

    tr.title('Лабораторная работа №7 — задание 2, метод Монте-Карло')
    tr.setup(850,700); tr.setworldcoordinates(X_MIN-0.5,Y_MIN-0.8,X_MAX+0.5,Y_MAX+0.8)
    tr.speed(0); tr.hideturtle(); tr.bgcolor('white')
    # Контур четверти круга.
    tr.pensize(2); tr.pencolor('black'); tr.penup(); tr.goto(-2,0); tr.pendown()
    tr.goto(0,0); tr.circle(2,90); tr.goto(-2,0)
    # Контур треугольной части: вершины (0,0), (2,0), (1,-2).
    tr.penup(); tr.goto(0,0); tr.pendown(); tr.goto(2,0); tr.goto(1,-2); tr.goto(0,0)
    # Случайные точки: попадания зелёные, промахи красные.
    for x,y,hit in points:
        tr.penup(); tr.goto(x,y); tr.dot(3, 'green' if hit else 'red')
    tr.penup(); tr.goto(-2.3,-3.0)
    tr.write(f'Испытаний: {N}   Попаданий: {hits}   Оценка площади: {estimate:.4f}',font=('Arial',11,'normal'))
    tr.goto(-2.3,-3.35)
    tr.write(f'Реальная площадь: {exact:.4f}   Относительная ошибка: {error:.2f}%',font=('Arial',11,'normal'))
    print(f'Испытаний: {N}; попаданий: {hits}')
    print(f'Оценка площади: {estimate:.6f}; реальная площадь: {exact:.6f}')
    print(f'Оценка составляет {estimate/exact*100:.2f}% реальной площади; относительная ошибка {error:.2f}%.')
    tr.done()
if __name__=='__main__': main()

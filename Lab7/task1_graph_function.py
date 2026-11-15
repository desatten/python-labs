# Лабораторная работа №7. Задание 1. График функции (вариант 2).
# Функция соответствует кусочно заданному графику из предыдущей работы.
import turtle as tr
from math import sqrt

def calculate_y(x):
    if x < -8: return -3.0
    if x < -3: return 0.6*x + 1.8
    if x <= 3: return -sqrt(max(0.0, 9-x*x))
    if x < 5: return x-3
    return 3.0

def main():
    x_min, x_max, step = -10.0, 10.0, 0.05
    y_min, y_max = -4.0, 4.0
    tr.title('Лабораторная работа №7 — задание 1, вариант 2')
    tr.setup(900, 600)
    tr.setworldcoordinates(x_min, y_min, x_max, y_max)
    tr.speed(0); tr.hideturtle(); tr.bgcolor('white')
    # Координатные оси и деления.
    tr.pencolor('gray'); tr.pensize(1)
    tr.penup(); tr.goto(x_min,0); tr.pendown(); tr.goto(x_max,0)
    tr.penup(); tr.goto(0,y_min); tr.pendown(); tr.goto(0,y_max)
    for x in range(int(x_min), int(x_max)+1, 1):
        tr.penup(); tr.goto(x,-0.08); tr.pendown(); tr.goto(x,0.08)
    for y in range(int(y_min), int(y_max)+1):
        tr.penup(); tr.goto(-0.12,y); tr.pendown(); tr.goto(0.12,y)
    tr.penup(); tr.goto(0.3, y_max-0.35); tr.write('y', font=('Arial',12,'normal'))
    tr.goto(x_max-0.5,0.25); tr.write('x', font=('Arial',12,'normal'))
    tr.pencolor('blue'); tr.pensize(2)
    x=x_min; tr.penup(); tr.goto(x,calculate_y(x)); tr.pendown()
    while x <= x_max:
        tr.goto(x,calculate_y(x)); x += step
    tr.done()
if __name__=='__main__': main()

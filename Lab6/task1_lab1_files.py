# Лабораторная работа №6. Файлы. Задание: дополнение к лабораторной №1.
# Вход: lab1_input.txt (по одной alpha в строке). Выход: lab1_output.txt.
from math import sin, cos, pi, sqrt
from pathlib import Path

BASE = Path(__file__).resolve().parent
INPUT_FILE = BASE / 'lab1_input.txt'
OUTPUT_FILE = BASE / 'lab1_output.txt'

def calculate(alpha):
    z1 = cos(alpha) + sin(alpha) + cos(3 * alpha) + sin(3 * alpha)
    z2 = 2 * sqrt(2) * cos(alpha) * sin(pi / 4 + 2 * alpha)
    return z1, z2

def main():
    if not INPUT_FILE.exists():
        INPUT_FILE.write_text('# alpha (радианы), по одному числу в строке\n-1\n-0.5\n0\n0.5\n1\n', encoding='utf-8')
    results = ['Лабораторная работа №6 — обработка данных лабораторной №1',
               f"{'alpha':>12} {'z1':>16} {'z2':>16} {'|z1-z2|':>16}"]
    for number, line in enumerate(INPUT_FILE.read_text(encoding='utf-8').splitlines(), 1):
        line = line.split('#', 1)[0].strip()
        if not line:
            continue
        try:
            alpha = float(line)
            z1, z2 = calculate(alpha)
            results.append(f'{alpha:12.6f} {z1:16.8f} {z2:16.8f} {abs(z1-z2):16.3e}')
        except ValueError as exc:
            results.append(f'Строка {number}: некорректные данные ({exc})')
    OUTPUT_FILE.write_text('\n'.join(results) + '\n', encoding='utf-8')
    print(f'Готово. Результат записан в {OUTPUT_FILE.name}')

if __name__ == '__main__': main()

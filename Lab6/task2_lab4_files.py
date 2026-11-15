# Лабораторная работа №6. Файловая обработка задания из лабораторной №4, вариант 2.
# Входной файл содержит числа массива по одному в строке; выход — отчёт.
from pathlib import Path
BASE = Path(__file__).resolve().parent
INPUT_FILE, OUTPUT_FILE = BASE/'lab4_input.txt', BASE/'lab4_output.txt'

def analyze(numbers):
    positive_sum = sum(v for v in numbers if v > 0)
    max_i = max(range(len(numbers)), key=lambda i: abs(numbers[i]))
    min_i = min(range(len(numbers)), key=lambda i: abs(numbers[i]))
    left, right = sorted((max_i, min_i))
    product = 1.0
    for value in numbers[left + 1:right]: product *= value
    return positive_sum, max_i, min_i, product, sorted(numbers, reverse=True)

def main():
    if not INPUT_FILE.exists():
        INPUT_FILE.write_text('# Элементы массива (2–30 чисел)\n2.5\n-4\n0\n1.5\n-0.5\n3\n', encoding='utf-8')
    values=[]
    for line in INPUT_FILE.read_text(encoding='utf-8').splitlines():
        line=line.split('#',1)[0].strip()
        if line:
            try: values.append(float(line))
            except ValueError: raise ValueError(f'Некорректное число: {line}')
    if not 2 <= len(values) <= 30: raise ValueError('В файле должно быть от 2 до 30 чисел.')
    s, imax, imin, product, ordered = analyze(values)
    report = ['Лабораторная работа №6 — файловая версия лабораторной №4, вариант 2',
              f'Исходный массив: {values}', f'Сумма положительных элементов: {s:.4f}',
              f'Максимум по модулю: {values[imax]} (позиция {imax+1})',
              f'Минимум по модулю: {values[imin]} (позиция {imin+1})',
              f'Произведение элементов между ними: {product:.8g}',
              f'Массив по убыванию: {ordered}']
    OUTPUT_FILE.write_text('\n'.join(report)+'\n', encoding='utf-8')
    print(f'Готово. Результат записан в {OUTPUT_FILE.name}')
if __name__ == '__main__': main()

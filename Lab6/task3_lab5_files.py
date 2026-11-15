# Лабораторная работа №6. Файловая версия лабораторной №5, вариант 2.
# Входной файл: первая строка — число строк и столбцов, далее матрица.
from pathlib import Path
BASE=Path(__file__).resolve().parent
INPUT_FILE, OUTPUT_FILE=BASE/'lab5_input.txt', BASE/'lab5_output.txt'

def characteristic(row): return sum(v for v in row if v > 0 and v % 2 == 0)
def count_columns_without_zero(matrix):
    return sum(all(row[c] != 0 for row in matrix) for c in range(len(matrix[0])))
def sort_rows(matrix): return sorted((row[:] for row in matrix), key=characteristic)
def main():
    if not INPUT_FILE.exists():
        INPUT_FILE.write_text('''# Размеры матрицы: строки столбцы\n4 5\n1 2 0 -4 6\n3 8 5 2 -1\n0 4 7 6 9\n2 -2 1 3 4\n''',encoding='utf-8')
    lines=[ln.split('#',1)[0].strip() for ln in INPUT_FILE.read_text(encoding='utf-8').splitlines()]
    tokens=[part for ln in lines if ln for part in ln.split()]
    if len(tokens)<2: raise ValueError('Не заданы размеры матрицы.')
    rows,cols=map(int,tokens[:2])
    if not (1<=rows<=20 and 1<=cols<=20): raise ValueError('Размеры матрицы должны быть от 1 до 20.')
    vals=list(map(int,tokens[2:]))
    if len(vals)!=rows*cols: raise ValueError(f'Ожидалось {rows*cols} элементов, получено {len(vals)}.')
    matrix=[vals[i*cols:(i+1)*cols] for i in range(rows)]
    ordered=sort_rows(matrix)
    fmt=lambda m: '\n'.join(' '.join(f'{v:4d}' for v in row) for row in m)
    report=['Лабораторная работа №6 — файловая версия лабораторной №5, вариант 2',
            'Исходная матрица:',fmt(matrix),f'Количество столбцов без нулей: {count_columns_without_zero(matrix)}',
            'Строки по возрастанию характеристики (сумма положительных чётных элементов):',fmt(ordered),
            'Характеристики: '+', '.join(str(characteristic(row)) for row in ordered)]
    OUTPUT_FILE.write_text('\n'.join(report)+'\n',encoding='utf-8')
    print(f'Готово. Результат записан в {OUTPUT_FILE.name}')
if __name__=='__main__': main()

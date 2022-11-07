# Найдите максимальную сумму пути от вершины до основания
# следующего треугольника euler18.txt

from datetime import datetime
from euler11 import readmatrix

n = 15


def msu(rows, n_line):
    for i in range(len(rows[n_line])):
        rows[n_line][i] += max([rows[n_line + 1][i],
                                rows[n_line + 1][i + 1]])
    return rows[n_line][0] if len(rows[n_line]) == 1 else msu(rows, n_line - 1)


if __name__ == '__main__':
    # 1 вариант
    start_time = datetime.now()
    matrix = readmatrix("euler18.txt")
    print(msu(matrix, n - 2))
    print(datetime.now() - start_time)

    # 2 вариант
    start_time = datetime.now()
    pass
    print(datetime.now() - start_time)

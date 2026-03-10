# Найдите максимальную сумму пути от вершины до основания
# следующего треугольника euler18.txt

from datetime import datetime
from bs4 import BeautifulSoup as bs
from requests import get

n = 15


def readmatrix(namefile=None, text=None, mode=None):
    """Возвращает матрицу чисел или слов из файла или переданного текста"""
    matrix = []
    if text is not None:
        for line in range(len(text)):
            matrix.append([int(i) for i in text[line].split(" ")])
    elif mode is None:
        with open(namefile) as f:
            for line in f:
                matrix.append([int(i) for i in line.rstrip('\n').split()])
    elif mode == 'text':
        with open(namefile) as f:
            for line in f:
                matrix = line.replace('"', '').split(',')
    return matrix


def msu(rows, n_line):
    """Возвращает максимальную сумму пути по треугольнику"""
    for i in range(len(rows[n_line])):
        rows[n_line][i] += max([rows[n_line + 1][i],
                                rows[n_line + 1][i + 1]])
    return rows[n_line][0] if len(rows[n_line]) == 1 else msu(rows, n_line - 1)


def get_data(url, tag, n):
    """Возвращает чистый текст по n-ному заданному тегу и url"""
    return bs(get(url, timeout=3).text, 'lxml').find_all(tag)[n].text

# 1 вариант
start_time = datetime.now()
matrix = readmatrix("euler18.txt")
print(msu(matrix, n - 2))
print(datetime.now() - start_time)

# 2 вариант
start_time = datetime.now()
url = 'https://euler.jakumo.org/problems/view/18.html'
matrix = readmatrix(text=get_data(url, 'p', 4).strip().split("\n"))
print(msu(matrix, n - 2))
print(datetime.now() - start_time)

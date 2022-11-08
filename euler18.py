# Найдите максимальную сумму пути от вершины до основания
# следующего треугольника euler18.txt

from project_euler_defs import *

n = 15

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

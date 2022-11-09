# Каково наибольшее произведение четырех подряд идущих
# чисел в таблице 20×20, расположенных в любом направлении
# (вверх, вниз, вправо, влево или по диагонали)?

from project_euler_defs import *

n = 4

# 1 Вариант
start_time = datetime.now()
matrix = readmatrix("euler11.txt")
# Транспонирование матрицы
matrix_transpose = [[0 for j in range(len(matrix))]
                    for i in range(len(matrix[0]))]
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        matrix_transpose[j][i] = matrix[i][j]

print(max(product_multiply(matrix, n)
          + product_multiply(matrix_transpose, n)
          + [product_multiply_diagonals(matrix, n)]))
print(datetime.now() - start_time)

# 2 Вариант
start_time = datetime.now()
matrix = array(readmatrix("euler11.txt"))
matrix_transpose = matrix.transpose()
print(max(product_multiply(matrix, n)
          + product_multiply(matrix_transpose, n)
          + [product_multiply_diagonals(matrix, n)]))
print(datetime.now() - start_time)

# 3 Вариант
start_time = datetime.now()
url = 'https://euler.jakumo.org/problems/view/11.html'
matrix = array(readmatrix(text=get_data(url, 'p', 1).strip().split("\n")))
matrix_transpose = matrix.transpose()
print(max(product_multiply(matrix, n)
          + product_multiply(matrix_transpose, n)
          + [product_multiply_diagonals(matrix, n)]))
print(datetime.now() - start_time)

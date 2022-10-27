# Каково наибольшее произведение четырех подряд идущих
# чисел в таблице 20×20, расположенных в любом направлении
# (вверх, вниз, вправо, влево или по диагонали)?

from datetime import datetime
from numpy import array

n = 4


def readmatrix(namefile):
    # Считывает из файла двумерную матрицу
    f = open(namefile)
    matrix = [line.replace("\n", "").split() for line in f]
    return matrix


def product_multiply(matrix, n):
    """Перемножает по n элементов в строке матрицы
    и возвращает список произведений"""
    product = []
    for i in range(len(matrix[0]) - n + 1):
        for j in range(len(matrix)):
            num = 1
            for k in range(n):
                num *= int(matrix[j][i + k])
            product.append(num)
    return(product)


def product_multiply_diagonals(matrix, n):
    """Перемножает по n элементов матрицы по диагоналям и
    возвращает максимальное произведение (экономим память)"""
    max_product = 0
    for x in range(len(matrix[0]) - n + 1):
        for y in range(len(matrix[0]) - n + 1):
            # по диагонали вправо вниз
            num = 1
            for i in range(n):
                num *= int(matrix[x + i][y + i])
            if num > max_product:
                max_product = num

            # по диагонали вправо вверх
            num = 1
            for i in range(n):
                num *= int(matrix[x - i][y + i])
            if num > max_product:
                max_product = num

            # по диагонали влево вниз
            num = 1
            for i in range(n):
                num *= int(matrix[x + i][y - i])
            if num > max_product:
                max_product = num

            # по диагонали влево вверх
            num = 1
            for i in range(n):
                num *= int(matrix[x - i][y - i])
            if num > max_product:
                max_product = num
    return max_product


# 1 Вариант
start_time = datetime.now()
matrix = readmatrix("euler11.txt")

# Транспонирование матрицы
matrix_transpose = [[0 for j in range(len(matrix))] for i in range(len(matrix[0]))]
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        matrix_transpose[j][i] = matrix[i][j]

print(max(product_multiply(matrix, n) + product_multiply(matrix_transpose, n) + [product_multiply_diagonals(matrix, n)]))
print(datetime.now() - start_time)

# 2 Вариант
start_time = datetime.now()
matrix = array(readmatrix("euler11.txt"))
matrix_transpose = matrix.transpose()
print(max(product_multiply(matrix, n) + product_multiply(matrix_transpose, n) + [product_multiply_diagonals(matrix, n)]))
print(datetime.now() - start_time)

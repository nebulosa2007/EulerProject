# Каково наибольшее произведение четырех подряд идущих чисел в таблице 20×20,
# расположенных в любом направлении (вверх, вниз, вправо, влево или по
# диагонали)?

from datetime import datetime
from typing import List, Optional

from numpy import array


def readmatrix(
    namefile: Optional[str] = None,
    text: Optional[List[str]] = None,
    mode: Optional[str] = None
) -> List:
    """
    Возвращает матрицу чисел или слов из файла или переданного текста.

    Args:
        namefile: Путь к файлу.
        text: Текст для парсинга.
        mode: Режим чтения ('text' для слов, None для чисел).

    Returns:
        Матрица чисел или список слов.
    """
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


def product_multiply(matrix: List[List[int]], n: int) -> List[int]:
    """
    Возвращает список произведений n элементов в строках матрицы.

    Args:
        matrix: Матрица чисел.
        n: Количество элементов для перемножения.

    Returns:
        Список произведений.
    """
    product = []
    for i in range(len(matrix[0]) - n + 1):
        for j in range(len(matrix)):
            num = 1
            for k in range(n):
                num *= matrix[j][i + k]
            product.append(num)
    return product


def product_multiply_diagonals(matrix: List[List[int]], n: int) -> int:
    """
    Перемножает по n элементов матрицы по диагоналям.

    Args:
        matrix: Матрица чисел.
        n: Количество элементов для перемножения.

    Returns:
        Максимальное произведение.
    """
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


def get_data(url: str, tag: str, n: int) -> str:
    """
    Возвращает чистый текст по n-ному заданному тегу и url.

    Args:
        url: URL-адрес страницы.
        tag: HTML-тег для поиска.
        n: Индекс элемента.

    Returns:
        Текстовое содержимое элемента.
    """
    from bs4 import BeautifulSoup as bs
    from requests import get

    return bs(get(url, timeout=3).text, 'lxml').find_all(tag)[n].text


def euler11() -> None:
    """
    Решение задачи Эйлера №11.

    Каково наибольшее произведение четырех подряд идущих чисел в таблице
    20×20, расположенных в любом направлении?
    """
    n = 4

    # 1 Вариант
    start_time = datetime.now()
    matrix = readmatrix("euler11.txt")
    matrix_transpose = [[0 for _ in range(len(matrix))]
                        for _ in range(len(matrix[0]))]
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            matrix_transpose[j][i] = matrix[i][j]

    print(max(
        product_multiply(matrix, n)
        + product_multiply(matrix_transpose, n)
        + [product_multiply_diagonals(matrix, n)]
    ))
    print(datetime.now() - start_time)

    # 2 Вариант
    start_time = datetime.now()
    matrix = array(readmatrix("euler11.txt"))
    matrix_transpose = matrix.transpose()
    print(max(
        product_multiply(matrix, n)
        + product_multiply(matrix_transpose, n)
        + [product_multiply_diagonals(matrix, n)]
    ))
    print(datetime.now() - start_time)

    # 3 Вариант
    start_time = datetime.now()
    url = 'https://euler.jakumo.org/problems/view/11.html'
    matrix = array(readmatrix(text=get_data(url, 'p', 1).strip().split("\n")))
    matrix_transpose = matrix.transpose()
    print(max(
        product_multiply(matrix, n)
        + product_multiply(matrix_transpose, n)
        + [product_multiply_diagonals(matrix, n)]
    ))
    print(datetime.now() - start_time)


if __name__ == "__main__":
    euler11()

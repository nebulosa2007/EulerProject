# Найдите максимальную сумму пути от вершины до основания
# следующего треугольника euler18.txt

from datetime import datetime
from typing import List, Optional

from bs4 import BeautifulSoup as bs
from requests import get


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


def msu(rows: List[List[int]], n_line: int) -> int:
    """
    Возвращает максимальную сумму пути по треугольнику.

    Args:
        rows: Матрица треугольника.
        n_line: Номер строки для начала вычислений.

    Returns:
        Максимальная сумма пути.
    """
    for i in range(len(rows[n_line])):
        rows[n_line][i] += max(
            rows[n_line + 1][i],
            rows[n_line + 1][i + 1]
        )
    if len(rows[n_line]) == 1:
        return rows[n_line][0]
    return msu(rows, n_line - 1)


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
    return bs(get(url, timeout=3).text, 'lxml').find_all(tag)[n].text


def euler18() -> None:
    """
    Решение задачи Эйлера №18.

    Найдите максимальную сумму пути от вершины до основания треугольника.
    """
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


if __name__ == "__main__":
    euler18()

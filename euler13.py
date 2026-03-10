# Найдите первые десять цифр суммы следующих ста 50-значных чисел.
# Ответ: 5537376230

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


def euler13() -> None:
    """
    Решение задачи Эйлера №13.

    Найдите первые десять цифр суммы следующих ста 50-значных чисел.
    """
    n = 10

    # 1 вариант
    start_time = datetime.now()
    numbers = readmatrix("euler13.txt")
    sum_vertical, total = 0, 0
    for j in range(1, len(numbers[0]) + 1):
        for i in range(len(numbers)):
            sum_vertical += numbers[i][j * -1]
        total += sum_vertical * (10 ** (j - 1))
        sum_vertical = 0
    print(str(total)[0:10])
    print(datetime.now() - start_time)

    # 2 вариант
    start_time = datetime.now()
    url = 'https://euler.jakumo.org/problems/view/13.html'
    numbers = get_data(url, 'div', 9).strip().split("\n")
    column_numbers, long_number = [], {}
    for j in range(1, len(numbers[0]) + 1):
        for i in range(len(numbers)):
            column_numbers.append(int(numbers[i][j * -1]))
        long_number[len(numbers[0]) - j] = sum(column_numbers)
        column_numbers = []
    j -= 1
    total_num = [0] * (j + len(str(long_number[j])))
    for i in long_number.keys():
        for k, j_val in enumerate(list(str(long_number[i]))):
            total_num[i + k] += int(j_val)
            if total_num[i + k] > 9:
                total_num[i + k - 1] += total_num[i + k] // 10
                total_num[i + k] %= 10
    print(''.join(str(x) for x in total_num)[:10])
    print(datetime.now() - start_time)


if __name__ == "__main__":
    euler13()

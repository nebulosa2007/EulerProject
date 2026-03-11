# Найдите наибольшее произведение тринадцати последовательных цифр в
# данном 1000-значном числе.

from datetime import datetime
from functools import reduce
from math import prod
from typing import List

from bs4 import BeautifulSoup as bs
from requests import get


def get_data(url: str, tag: str, n: int) -> str:
    """
    Возвращает чистый текст по n-ному заданному тегу и url.

    Args:
        url: URL-адрес страницы.
        tag: HTML-тег для поиска.
        n: Индекс элемента в списке найденных тегов.

    Returns:
        Текстовое содержимое найденного элемента.
    """
    return bs(get(url, timeout=3).text, 'lxml').find_all(tag)[n].text


def multiply_numbers(*numset: str) -> int:
    """
    Возвращает произведение чисел в заданной выборке.

    Args:
        *numset: Последовательность чисел в строковом формате.

    Returns:
        Произведение всех чисел.
    """
    return reduce(lambda x, y: int(x) * int(y), numset)


def loadfiletolistnumbers(namefile: str) -> List[str]:
    """
    Возвращает список из чисел заданного файла.

    Args:
        namefile: Путь к файлу.

    Returns:
        Список цифр как строк.
    """
    number = []
    with open(namefile) as f:
        while True:
            c = f.read(1)
            if c == '':
                break
            elif c != '\n':
                number.append(c)
    return number


def euler08() -> None:
    """
    Решение задачи Эйлера №8.

    Найдите наибольшее произведение тринадцати последовательных цифр в
    данном 1000-значном числе.
    """
    n = 13

    # 1 Вариант
    number = loadfiletolistnumbers('euler08.txt')
    all_prod = []

    start_time = datetime.now()
    for i in range(len(number) - n):
        numset = number[i:i + n]
        if len(numset) >= n or '0' not in numset:
            all_prod.append(multiply_numbers(*numset))
    print(max(all_prod))
    print(datetime.now() - start_time)

    # 2 Вариант
    start_time = datetime.now()
    print(max(
        prod(map(int, number[i:i + n]))
        for i in range(len(number) - n)
    ))
    print(datetime.now() - start_time)

    # 3 Вариант
    start_time = datetime.now()
    url = 'https://euler.jakumo.org/problems/view/8.html'
    text = list(get_data(url, 'p', 1).replace('\n', ''))
    print(max(
        prod(map(int, text[i:i + n]))
        for i in range(len(text) - n)
    ))
    print(datetime.now() - start_time)


if __name__ == "__main__":
    euler08()

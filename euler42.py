# n-й член последовательности треугольных чисел задается как tn = ½n(n+1)
# Используя euler42.txt определите, сколько в нем треугольных слов,
# преобразовывая каждую букву в число, соответствующее ее порядковому номеру
# в алфавите и складывая эти значения

from datetime import datetime
from typing import List, Optional

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


def figurate_number(number: int, base: int = 3) -> int:
    """
    Возвращает number-ое многоугольное число по заданной базе угольности.

    Args:
        number: Порядковый номер числа.
        base: База угольности (3 = треугольные, 5 = пятиугольные и т.д.).

    Returns:
        Многоугольное число.
    """
    assert base >= 3
    return int(((base - 2) * number ** 2 - (base - 4) * number) / 2)


def isfigurate_number(test_number: int, base: int = 3) -> bool:
    """
    Проверяет является ли число многоугольным по заданной базе.

    Args:
        test_number: Число для проверки.
        base: База угольности.

    Returns:
        True если число является многоугольным, иначе False.
    """
    assert base >= 3
    r = (8 * (base - 2) * test_number + (base - 4) ** 2) ** 0.5
    return ((r + base - 4) / (2 * base - 4)) % 1 == 0


def euler42() -> None:
    """
    Решение задачи Эйлера №42.

    Сколько треугольных слов в файле?
    """
    n = "https://projecteuler.net/project/resources/p042_words.txt"

    # 1 вариант
    start_time = datetime.now()
    words = readmatrix("euler42.txt", mode='text')
    print(len([
        w for w in words
        if isfigurate_number(sum(ord(x) - 64 for x in w), 3)
    ]))
    print(datetime.now() - start_time)

    # 2 вариант
    start_time = datetime.now() 
    response = get(n, timeout=3)
    if response.status_code != 200:
        exit()
    words = response.content.decode().replace('"', '').split(',')
    max_n = 0
    for x in words:
        max_n = max(sum(ord(c) - 64 for c in x), max_n)
    triangle_numbers = [figurate_number(_, 3) for _ in range(1, max_n + 1)]
    print(len([
        w for w in words
        if sum(ord(c) - 64 for c in w) in triangle_numbers
    ]))
    print(datetime.now() - start_time)


if __name__ == "__main__":
    euler42()

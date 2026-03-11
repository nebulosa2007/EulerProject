# Начните с сортировки в алфавитном порядке. Затем подсчитайте алфавитные
# значения каждого имени и умножьте это значение на порядковый номер имени
# в отсортированном списке для получения количества очков имени.
# Какова сумма очков имен в файле?

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


def names_points(*names: str) -> int:
    """
    Возвращает сумму очков отсортированных имен.

    Args:
        *names: Имена для подсчета очков.

    Returns:
        Сумма очков всех имен.
    """
    return sum(
        sum(ord(j) - 64 for j in names[i]) * (i + 1)
        for i in range(len(names))
    )


def euler22() -> None:
    """
    Решение задачи Эйлера №22.

    Какова сумма очков имен в файле?
    """
    n = "https://projecteuler.net/project/resources/p022_names.txt"

    # 1 вариант
    start_time = datetime.now()
    print(names_points(*sorted(readmatrix("euler22.txt", mode='text'))))
    print(datetime.now() - start_time)

    # 2 вариант
    start_time = datetime.now()
    response = get(n, timeout=3)
    if response.status_code != 200:
        exit()
    names = sorted(response.content.decode().replace('"', '').split(','))
    print(names_points(*names))
    print(datetime.now() - start_time)


if __name__ == "__main__":
    euler22()

# Сколько существует таких маршрутов в сетке 20×20?

from datetime import datetime
from functools import lru_cache
from math import factorial
from typing import Dict, Tuple


memory: Dict[Tuple[int, int], int] = {(1, 0): 1, (0, 1): 1}


@lru_cache(2 ** 20)
def func(x: int, y: int) -> int:
    """
    Возвращает количество маршрутов до точки (x, y).

    Args:
        x: Координата x.
        y: Координата y.

    Returns:
        Количество маршрутов.
    """
    if (x, y) not in memory:
        if x == 0:
            memory[(x, y)] = func(x, y - 1)
        elif y == 0:
            memory[(x, y)] = func(x - 1, y)
        else:
            memory[(x, y)] = func(x - 1, y) + func(x, y - 1)
    return memory[(x, y)]


def euler15() -> None:
    """
    Решение задачи Эйлера №15.

    Сколько существует таких маршрутов в сетке 20×20?
    """
    n = 20

    # 1 вариант
    start_time = datetime.now()
    print(func(n, n))
    print(datetime.now() - start_time)

    # 2 вариант
    start_time = datetime.now()
    counter = 1
    for i in range(n):
        counter = counter * (2 * n - i) // (1 + i)
    print(counter)
    print(datetime.now() - start_time)

    # 3 вариант
    start_time = datetime.now()
    print(int(factorial(2 * n) / (factorial(n) ** 2)))
    print(datetime.now() - start_time)

    # 4 вариант
    start_time = datetime.now()
    dp = {(0, 0): 1}
    for i in range(n + 1):
        for j in range(n + 1):
            if i == 0 or j == 0:
                dp[(i, j)] = 1
            else:
                dp[(i, j)] = dp[(i - 1, j)] + dp[(i, j - 1)]
    print(dp[(n, n)])
    print(datetime.now() - start_time)


if __name__ == "__main__":
    euler15()

# Сколько существует таких маршрутов в сетке 20×20?

from datetime import datetime
from functools import lru_cache
from math import factorial

n = 20

memory = {(1, 0): 1, (0, 1): 1}


@lru_cache(2 ** 20)
def func(x, y):
    if (x, y) not in memory:
        if x == 0:
            memory[(x, y)] = func(x, y - 1)
        elif y == 0:
            memory[(x, y)] = func(x - 1, y)
        else:
            memory[(x, y)] = func(x - 1, y) + func(x, y - 1)
    return memory[(x, y)]


if __name__ == '__main__':
    # 1 вариант
    start_time = datetime.now()
    print(func(n, n))
    print(datetime.now() - start_time)

    # 2 вариант
    start_time = datetime.now()
    counter = 1
    for _ in range(20):
        counter = counter * (40 - _) // (1 + _)
    print(counter)

    # 3 вариант
    print(int(factorial(2 * n) / (factorial(n) ** 2)))

    # 4 вариант
    dp = {(0, 0): 1}
    for i in range(n + 1):
        for j in range(n + 1):
            if i == 0 or j == 0:
                dp[(i, j)] = 1
            else:
                dp[(i, j)] = dp[(i - 1, j)] + dp[(i, j - 1)]
    print(dp[(n, n)])
    print(datetime.now() - start_time)

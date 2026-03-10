# Найдите сумму всех чисел меньше 1000, кратных 3 или 5.

from datetime import datetime as dt
import functools as ft


def euler01() -> None:
    """
    Решение задачи Эйлера №1.

    Найдите сумму всех чисел меньше 1000, кратных 3 или 5.
    """
    n = 1_000

    # Вариант 1
    start_time = dt.now()
    total = 0
    for i in range(n):
        if i % 3 == 0 or i % 5 == 0:
            total += i
    print(total)
    print(dt.now() - start_time)

    # Вариант 2
    start_time = dt.now()
    print(ft.reduce(
        lambda x, y: x + y,
        list(filter(lambda x: x % 3 == 0 or x % 5 == 0, list(range(n))))
    ))
    print(dt.now() - start_time)


if __name__ == "__main__":
    euler01()

# Найдите сумму всех четных элементов ряда Фибоначчи, которые не превышают
# четыре миллиона.

from datetime import datetime
from functools import reduce
from itertools import takewhile
from typing import Generator


def fibonacci(f1: int = 0, f2: int = 1) -> Generator[int, None, None]:
    """
    Итерируемая функция вычисления следующего числа Фибоначчи.

    Args:
        f1: Первое число последовательности.
        f2: Второе число последовательности.

    Yields:
        Очередное число Фибоначчи.
    """
    while True:
        yield f1
        f1, f2 = f2, f1 + f2


def euler02() -> None:
    """
    Решение задачи Эйлера №2.

    Найдите сумму всех четных элементов ряда Фибоначчи,
    которые не превышают четыре миллиона.
    """
    n = 4_000_000

    # 1 Вариант
    start_time = datetime.now()
    odd_fb_sum, iterator = 0, fibonacci()
    while (fb_num := next(iterator)) < n:
        odd_fb_sum += fb_num if fb_num % 2 == 0 else 0
    print(odd_fb_sum)
    print(datetime.now() - start_time)

    # 2 Вариант
    start_time = datetime.now()
    print(reduce(
        lambda x, y: x + y,
        filter(lambda s: s % 2 == 0, takewhile(lambda f: f < n, fibonacci()))
    ))
    print(datetime.now() - start_time)


if __name__ == "__main__":
    euler02()

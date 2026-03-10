# Какое число является 10001-м простым числом?

from datetime import datetime
from itertools import count, islice
from typing import Generator, Optional


def primes(dimension: Optional[int] = None) -> Generator[int, None, None]:
    """
    Итерируемая функция генерации простых чисел.

    Args:
        dimension: Количество цифр в числах (None для всех простых чисел).

    Yields:
        Очередное простое число.
    """
    start = 2 if dimension is None else 10 ** (dimension - 1) + 1
    ints = count(start)
    while True:
        p = next(ints)
        yield p
        ints = filter(p.__rmod__, ints)


def euler07() -> None:
    """
    Решение задачи Эйлера №7.

    Какое число является 10001-м простым числом?
    """
    n = 10_001

    # 1 Вариант
    start_time = datetime.now()
    number = primes()
    for i in range(n):
        prime = next(number)
    print(prime)
    print(datetime.now() - start_time)

    # 2 Вариант
    start_time = datetime.now()
    print(list(islice(primes(), n))[-1])
    print(datetime.now() - start_time)


if __name__ == "__main__":
    euler07()

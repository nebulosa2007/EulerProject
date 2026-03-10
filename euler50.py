# Какое из простых чисел меньше одного миллиона можно записать в
# виде суммы наибольшего количества последовательных простых чисел?

from datetime import datetime
from functools import lru_cache
from itertools import count
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


@lru_cache(2 ** 5)
def isprime(number: int) -> bool:
    """
    Проверка числа на простоту перебором делителей.

    Args:
        number: Число для проверки.

    Returns:
        True если число простое, иначе False.
    """
    if number in {2, 3, 5, 7}:
        return True
    if number < 2 or number % 2 == 0:
        return False
    if number % 3 == 0 or number % 5 == 0:
        return False
    a, k = number, 0
    for i in range(5, int(number ** 0.5), 6):
        k += 1 if a % i == 0 or a % (i + 2) == 0 else 0
    return k <= 0


def euler50() -> None:
    """
    Решение задачи Эйлера №50.

    Какое из простых чисел меньше одного миллиона можно записать в виде
    суммы наибольшего количества последовательных простых чисел?
    """
    n = 1_000_000

    # 1 вариант
    start_time = datetime.now()
    con_primes = []
    for i in primes():
        if sum(con_primes) + i >= n:
            while not isprime(sum(con_primes)):
                con_primes = con_primes[1:]
            break
        else:
            con_primes.append(i)
    print(sum(con_primes), len(con_primes))
    print(datetime.now() - start_time)

    # 2 вариант
    start_time = datetime.now()
    pass
    print(datetime.now() - start_time)


if __name__ == "__main__":
    euler50()

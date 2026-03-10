# Какое из простых чисел меньше одного миллиона можно записать в
# виде суммы наибольшего количества последовательных простых чисел?

from datetime import datetime
from itertools import count
from functools import lru_cache


def primes(dimension=None):
    """Итерируемая функция генерация простых чисел"""
    start = 2 if dimension is None else 10 ** (dimension - 1) + 1
    ints = count(start)
    while True:
        p = next(ints)
        yield p
        ints = filter(p.__rmod__, ints)


@lru_cache(2 ** 5)
def isprime(number: int):
    """Проверка числа на простоту перебором делителей"""
    if number in {2, 3, 5, 7}: return True
    if number < 2 or number % 2 == 0: return False
    if number % 3 == 0 or number % 5 == 0: return False
    a, k = number, 0
    for i in range(5, int(number**0.5), 6):
        k += 1 if a % i == 0 or a % (i + 2) == 0 else 0
    return True if k <= 0 else False


def euler50():
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

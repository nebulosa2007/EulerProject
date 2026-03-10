# Найдите сумму всех простых чисел меньше двух миллионов.

from datetime import datetime
from functools import reduce


def eratosfen(number):
    """Решето Эратосфена: генерация простых чисел вплоть до заданного числа"""
    sieve = list(range(number + 1))
    sieve[1] = 0
    for i in sieve:
        if i > 1:
            for j in range(2 * i, len(sieve), i):
                sieve[j] = 0
    return sieve


def euler10():
    n = 2_000_000

    # 1 Вариант
    start_time = datetime.now()
    print(reduce(lambda x, y: x + y, eratosfen(n)))
    print(datetime.now() - start_time)

    # 2 Вариант
    start_time = datetime.now()
    pass
    print(datetime.now() - start_time)


if __name__ == "__main__":
    euler10()

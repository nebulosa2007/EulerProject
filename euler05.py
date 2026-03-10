# Какое самое маленькое число делится нацело на все числа от 1 до 20?

from datetime import datetime
from functools import lru_cache


def eratosfen(number):
    """Решето Эратосфена: генерация простых чисел вплоть до заданного числа"""
    sieve = list(range(number + 1))
    sieve[1] = 0
    for i in sieve:
        if i > 1:
            for j in range(2 * i, len(sieve), i):
                sieve[j] = 0
    return sieve


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


def euler05():
    n = 20

    # 1 Вариант
    start_time = datetime.now()
    result = 1
    for k in set(eratosfen(n)) - {0}:
        i = 1
        while k ** (i + 1) < n:
            i += 1
        result *= k ** i
    print(result)
    print(datetime.now() - start_time)

    # 2 Вариант
    start_time = datetime.now()
    result = 1
    for k in range(n + 1):
        if isprime(k): result *= k ** max([_ for _ in range(n // 2) if k ** _ < n])
    else:
        print(result)
    print(datetime.now() - start_time)


if __name__ == "__main__":
    euler05()

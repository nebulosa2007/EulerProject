# Найдите произведение коэффициентов a < 1000 и b <= 1000 для
# квадратичного выражения, которое выражает максимальное число
# простых чисел для последовательных значений n, начиная с n = 0

from datetime import datetime
from functools import lru_cache
from typing import List


def eratosfen(number: int) -> List[int]:
    """
    Решето Эратосфена: генерация простых чисел вплоть до заданного числа.

    Args:
        number: Верхняя граница диапазона.

    Returns:
        Список, где индекс - число, значение - 0 для составных,
        само число для простых.
    """
    sieve = list(range(number + 1))
    sieve[1] = 0
    for i in sieve:
        if i > 1:
            for j in range(2 * i, len(sieve), i):
                sieve[j] = 0
    return sieve


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
    return True if k <= 0 else False


def euler27() -> None:
    """
    Решение задачи Эйлера №27.

    Найдите произведение коэффициентов a и b для квадратичного выражения,
    которое выражает максимальное число простых чисел.
    """
    n = 1_000

    # 1 вариант
    start_time = datetime.now()
    primes_num = sorted(set(eratosfen(n)))
    primes_num[0], primes, max_n_primes = 1, primes_num[:], 0
    for b in primes_num:
        for a in primes_num:
            i = 0
            for x in range(a, -2 * a, -2 * a):
                while True:
                    quadratic = i ** 2 + x * i + b
                    if quadratic not in primes:
                        if isprime(quadratic) and quadratic > 0:
                            primes.append(quadratic)
                        else:
                            if i - 1 > max_n_primes:
                                max_n_primes, axb = i - 1, x * b
                            break
                    i += 1
    print(axb)
    print(datetime.now() - start_time)

    # 2 вариант
    start_time = datetime.now()
    pass
    print(datetime.now() - start_time)


if __name__ == "__main__":
    euler27()

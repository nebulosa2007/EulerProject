# Какое самое маленькое число делится нацело на все числа от 1 до 20?

from datetime import datetime
from functools import lru_cache
from typing import List


def eratosfen(number: int) -> List[int]:
    """
    Решето Эратосфена: генерация простых чисел вплоть до заданного числа.

    Args:
        number: Верхняя граница диапазона.

    Returns:
        Список, где индекс - число, значение - 0 для составных, само число
        для простых.
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


def euler05() -> None:
    """
    Решение задачи Эйлера №5.

    Какое самое маленькое число делится нацело на все числа от 1 до 20?
    """
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
        if isprime(k):
            result *= k ** max([
                _ for _ in range(n // 2) if k ** _ < n
            ])
    print(result)
    print(datetime.now() - start_time)


if __name__ == "__main__":
    euler05()

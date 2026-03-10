# Какое существует наибольшее n-значное пан-цифровое простое число?

from datetime import datetime
from functools import lru_cache
from itertools import permutations


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


def euler41() -> None:
    """
    Решение задачи Эйлера №41.

    Какое существует наибольшее n-значное пан-цифровое простое число?
    """
    n = 9

    # 1 вариант
    start_time = datetime.now()
    pan_primes = []
    for z in range(n, 1, -1):
        pan_primes_check = [
            int(''.join(str(_) for _ in x))
            for x in permutations(range(1, z + 1), z)
            if isprime(int(''.join(str(_) for _ in x)))
        ]
        if pan_primes_check:
            pan_primes.append(max(pan_primes_check))
    print(max(pan_primes))
    print(datetime.now() - start_time)

    # 2 вариант
    start_time = datetime.now()
    pass
    print(datetime.now() - start_time)


if __name__ == "__main__":
    euler41()

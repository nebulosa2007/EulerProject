# Найдите сумму единственных одиннадцати простых чисел, из которых можно
# выбрасывать цифры как справа налево, так и слева направо, но числа при
# этом остаются простыми.

from datetime import datetime
from functools import lru_cache
from typing import Generator, List


def eratosfen(number: int) -> List[int]:
    """
    Решето Эратосфена: генерация простых чисел вплоть до заданного числа.

    Args:
        number: Верхняя граница диапазона.

    Returns:
        Список простых чисел.
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
    """Проверка числа на простоту перебором делителей.

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


def del_digit_left_or_right(number: int) -> Generator[int, None, None]:
    """Возвращает число без правой или левой цифры поочередно.

    Args:
        number: Исходное число.

    Yields:
        Число с удаленными цифрами.
    """
    yield number
    number_str = str(number)
    for k in range(1, len(number_str)):
        yield int(number_str[k:])
        yield int(number_str[:-k])


def euler37() -> None:
    """
    Решение задачи Эйлера №37.

    Найдите сумму одиннадцати простых чисел, из которых можно
    выбрасывать цифры как справа налево, так и слева направо.
    """
    n = 11

    # 1 вариант
    start_time = datetime.now()
    dimension = 1_000_000
    primes = list(set(eratosfen(dimension)) - {0, 2, 3, 5, 7})
    trucalable_primes, counter = [], 0
    while len(trucalable_primes) < n or primes[counter] > dimension:
        next_prime, counter = primes[counter], counter + 1
        if all(map(isprime, del_digit_left_or_right(next_prime))):
            trucalable_primes.append(next_prime)
    print(sum(trucalable_primes))
    print(datetime.now() - start_time)

    # 2 вариант
    start_time = datetime.now()
    c, s = 0, 0
    i = n
    while c < n:
        if all(map(isprime, del_digit_left_or_right(i))):
            c += 1
            s += i
        i += 2
    print(s)
    print(datetime.now() - start_time)


if __name__ == "__main__":
    euler37()


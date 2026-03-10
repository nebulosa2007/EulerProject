# Сколько существует круговых простых чисел меньше миллиона?

from datetime import datetime
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


def euler35() -> None:
    """
    Решение задачи Эйлера №35.

    Сколько существует круговых простых чисел меньше миллиона?
    """
    n = 1_000_000

    # 1 вариант
    start_time = datetime.now()
    primes, circular_primes = set(eratosfen(n)) - {0}, []
    for i in primes:
        if len(set(str(i))) == 1:
            circular_primes.append(i)
            continue

        next_num, circular_primes_check, power = i, [i], len(str(i)) - 1
        for _ in range(power):
            next_num = next_num % 10 * 10 ** power + next_num // 10
            if next_num in primes:
                circular_primes_check.append(next_num)
            else:
                circular_primes_check = []
                break
        circular_primes += [
            x for x in circular_primes_check if x not in circular_primes
        ]

    print(len(circular_primes))
    print(datetime.now() - start_time)

    # 2 вариант
    start_time = datetime.now()
    primes_bool = [True] * (n + 1)
    i = 2
    while i * i <= n:
        if primes_bool[i]:
            for j in range(i * 2, n + 1, i):
                primes_bool[j] = False
        i += 1

    primes_bool[0] = primes_bool[1] = False
    count = 0
    for i in range(1, n + 1):
        if primes_bool[i] is False:
            continue
        next_num, flag = str(i), True
        for _ in next_num:
            next_num = next_num[1:] + next_num[0]
            flag &= primes_bool[int(next_num)]
        if flag:
            count += 1
    print(count)
    print(datetime.now() - start_time)


if __name__ == "__main__":
    euler35()

# Каково наименьшее нечетное составное число, которое нельзя записать
# в виде суммы простого числа и удвоенного квадрата?

from datetime import datetime
from typing import List


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


def euler46() -> None:
    """
    Решение задачи Эйлера №46.

    Каково наименьшее нечетное составное число, которое нельзя записать
    в виде суммы простого числа и удвоенного квадрата?
    """
    n = 10_000

    # 1 вариант
    start_time = datetime.now()
    goldbah_conjecture = set()
    for p in set(eratosfen(n)):
        for k in range(int(n ** 0.5)):
            goldbah_conjecture.add(p + 2 * k * k)
    print(min(set(range(3, n, 2)) - goldbah_conjecture))
    print(datetime.now() - start_time)

    # 2 вариант
    start_time = datetime.now()
    pass
    print(datetime.now() - start_time)


if __name__ == "__main__":
    euler46()

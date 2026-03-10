# Найдите сумму всех пан-цифровых чисел из цифр от 0 до 9,
# обладающих данным свойством.

from datetime import datetime
from itertools import permutations
from typing import List, Optional


def eratosfen_lists(
    number: int,
    dimension: Optional[int] = None
) -> List[int]:
    """
    Решето Эратосфена: генерация списка простых чисел.

    Args:
        number: Верхняя граница диапазона.
        dimension: Размерность для начального числа.

    Returns:
        Список простых чисел.
    """
    start = 1 if dimension is None else dimension
    sieve = []
    for k in [
        x for x in range(10 ** (start - 1) + 1, number + 1)
        if x not in [
            i for sub in [
                list(range(2 * j, number + 1, j))
                for j in range(2, number // 2)
            ]
            for i in sub
        ]
    ]:
        sieve.append(k)
    return sieve


def euler43() -> None:
    """
    Решение задачи Эйлера №43.

    Найдите сумму всех пан-цифровых чисел из цифр от 0 до 9.
    """
    n = 10

    # 1 вариант
    start_time = datetime.now()
    pan_numbers = list(permutations(range(n), n))
    pan_numbers_sub, divisors = [], eratosfen_lists(18)
    for i in pan_numbers:
        if i[0] != 0:
            check_pan_number = [
                100 * i[y] + 10 * i[y + 1] + i[y + 2]
                for y in range(1, len(i) - 2)
            ]
            if all(
                check_pan_number[z] % divisors[z] == 0
                for z in range(len(check_pan_number))
            ):
                pan_numbers_sub.append(int(''.join(str(x) for x in i)))
    print(sum(pan_numbers_sub))
    print(datetime.now() - start_time)

    # 2 вариант
    start_time = datetime.now()
    pass
    print(datetime.now() - start_time)


if __name__ == "__main__":
    euler43()

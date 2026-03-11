# Каково первое треугольное число, у которого более пятисот делителей?

from datetime import datetime
from math import ceil, sqrt
from typing import List, Union


def all_factors_list(
    number: int,
    justcount: bool = False
) -> Union[List[int], int]:
    """
    Возвращает список делителей заданного числа или их количество.

    Args:
        number: Число для факторизации.
        justcount: Если True, возвращает количество делителей.

    Returns:
        Список делителей или их количество.
    """
    divisor, divisor_list = 2, [1, number]
    for i in range(2, ceil(sqrt(number)) + 1):
        if number % i == 0:
            if justcount:
                divisor += 2
            else: 
                divisor_list.append(i)
                divisor_list.append(number // i)
    if justcount:
        if ceil(sqrt(number)) ** 2 == number:
            return divisor - 1
        return divisor
    else:
        if ceil(sqrt(number)) ** 2 == number:
            return divisor_list[:-1]
        return divisor_list


def figurate_number(number: int, base: int = 3) -> int:
    """
    Возвращает number-ое многоугольное число по заданной базе угольности.

    Args:
        number: Порядковый номер числа.
        base: База угольности (3 = треугольные, 5 = пятиугольные и т.д.).

    Returns:
        Многоугольное число.
    """
    assert base >= 3
    return int(((base - 2) * number ** 2 - (base - 4) * number) / 2)


def euler12() -> None:
    """
    Решение задачи Эйлера №12.

    Каково первое треугольное число, у которого более пятисот делителей?
    """
    n = 500

    # 1 вариант
    start_time = datetime.now()
    i = 1
    triangle = figurate_number(i, 3)
    divisors = all_factors_list(triangle, justcount=True)
    while divisors < n:
        i += 1
        triangle = figurate_number(i, 3)
        divisors = all_factors_list(triangle, justcount=True)
    print(f'{i}-th triangle number: {triangle} with {divisors} divisors')
    print(datetime.now() - start_time)

    # 2 вариант
    start_time = datetime.now()
    pass
    print(datetime.now() - start_time)


if __name__ == "__main__":
    euler12()

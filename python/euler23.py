# Найдите сумму всех положительных чисел, которые не могут быть записаны как
# сумма двух избыточных чисел.

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


def euler23() -> None:
    """
    Решение задачи Эйлера №23.

    Найдите сумму всех положительных чисел, которые не могут быть записаны
    как сумма двух избыточных чисел.
    """
    n = 28_123

    # 1 вариант
    start_time = datetime.now()
    number_list = [0 for _ in range(n)]
    start_sum = sum(range(n))
    for i in range(n):
        divisor_list = all_factors_list(i)[:-1]
        if sum(divisor_list) > i:
            number_list[i] = i
    print(
        start_sum - sum(i * 2 for i in set(number_list) if i * 2 < n)
    )
    print(datetime.now() - start_time)

    # 2 вариант
    start_time = datetime.now()
    pass
    print(datetime.now() - start_time)


if __name__ == "__main__":
    euler23()

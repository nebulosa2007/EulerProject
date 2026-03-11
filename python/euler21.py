# Подсчитайте сумму всех дружественных чисел меньше 10000

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


def euler21() -> None:
    """
    Решение задачи Эйлера №21.

    Подсчитайте сумму всех дружественных чисел меньше 10000.
    """
    n = 10_000

    # 1 вариант
    start_time = datetime.now()
    amicable_pairs = []
    for x in range(10, n):
        if x not in amicable_pairs:
            x_sum_divisors = sum(all_factors_list(x)) - x
            y_sum_divisors = sum(all_factors_list(x_sum_divisors)) - x_sum_divisors
            if y_sum_divisors == x and x != x_sum_divisors:
                amicable_pairs.append(x)
                amicable_pairs.append(x_sum_divisors)
    print(sum(amicable_pairs))
    print(datetime.now() - start_time)

    # 2 вариант
    start_time = datetime.now()
    divisorsum = [0] * n
    for i in range(1, n):
        for j in range(i * 2, n, i):
            divisorsum[j] += i
    sum_amic_pairs = 0
    for i in range(1, n):
        j = divisorsum[i]
        if j != i and j < n and divisorsum[j] == i:
            sum_amic_pairs += i
    print(sum_amic_pairs)
    print(datetime.now() - start_time)


if __name__ == "__main__":
    euler21()

# Каков самый большой делитель числа 600 851 475 143,
# являющийся простым числом?

from datetime import datetime
from typing import List


def prime_factors_list(n: int) -> List[int]:
    """
    Возвращает список простых множителей заданного числа.

    Args:
        n: Число для факторизации.

    Returns:
        Список простых множителей числа.
    """
    divisor, nodarray = 2, []
    while divisor ** 2 <= n:
        if n % divisor == 0:
            n //= divisor
            nodarray.append(divisor)
        else:
            divisor += 1
    if n != 1:
        nodarray.append(n)
    return nodarray


def euler03() -> None:
    """
    Решение задачи Эйлера №3.

    Каков самый большой делитель числа 600 851 475 143,
    являющийся простым числом?
    """
    n = 600_851_475_143

    # 1 вариант
    start_time = datetime.now()
    print(max(prime_factors_list(n)))
    print(datetime.now() - start_time)

    # 2 вариант
    start_time = datetime.now()
    pass
    print(datetime.now() - start_time)


if __name__ == "__main__":
    euler03()

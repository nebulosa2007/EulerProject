# Найдите сумму цифр в числе 100!

from datetime import datetime
from functools import lru_cache
from math import factorial


@lru_cache(2 ** 5)
def factorial_self(number: int) -> int:
    """
    Возвращает факториал заданного числа.

    Args:
        number: Число для вычисления факториала.

    Returns:
        Факториал числа.
    """
    if number == 0:
        return 1
    result = 1
    for i in range(1, number + 1):
        result *= i
    return result


def euler20() -> None:
    """
    Решение задачи Эйлера №20.

    Найдите сумму цифр в числе 100!
    """
    n = 100

    # 1 вариант
    start_time = datetime.now()
    print(sum(int(x) for x in str(factorial_self(n))))
    print(datetime.now() - start_time)

    # 2 вариант
    start_time = datetime.now()
    print(sum(int(x) for x in str(factorial(n))))
    print(datetime.now() - start_time)


if __name__ == "__main__":
    euler20()

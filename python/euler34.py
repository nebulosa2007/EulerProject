# 145 является любопытным числом, поскольку 1! + 4! + 5! = 1 + 24 + 120 = 145.
# Найдите сумму всех чисел, каждое из которых равно сумме факториалов своих
# цифр. Примечание: поскольку 1! = 1 и 2! = 2 не являются суммами, учитывать
# их не следует.

from datetime import datetime
from functools import lru_cache


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


def getpower(n: int, factorial_list: list) -> int:
    """
    Возвращает степень для определения верхней границы поиска.

    Args:
        n: База для вычисления.
        factorial_list: Список факториалов.

    Returns:
        Степень для верхней границы.
    """
    test, power = n - 1, 1
    while factorial_list[n - 1] * power > test:
        test = test * 10 + n - 1
        power += 1
    return power


def factorial_digit_sum(
    n: int,
    with_zeroes: list,
    without_zeroes: list
) -> int:
    """
    Возвращает сумму списков факториалов.

    Args:
        n: Число для вычисления.
        with_zeroes: Список сумм факториалов с ведущими нулями.
        without_zeroes: Список сумм факториалов без ведущих нулей.

    Returns:
        Сумма факториалов цифр числа.
    """
    result = 0
    while n >= 10_000:
        result += with_zeroes[n % 10_000]
        n //= 10_000
    return result + without_zeroes[n]


def euler34() -> None:
    """
    Решение задачи Эйлера №34.

    Найдите сумму всех чисел, каждое из которых равно сумме факториалов
    своих цифр.
    """
    n = 10

    # 1 вариант
    start_time = datetime.now()
    factorial_list = [factorial_self(_) for _ in range(n)]
    curious_numbers = []
    upper_bound = n ** getpower(n, factorial_list)
    for i in range(3, upper_bound):
        number_list = [int(x) for x in str(i)]
        sum_number_list = sum(factorial_list[x] for x in number_list)
        if sum_number_list > i:
            continue
        elif sum_number_list == i:
            curious_numbers.append(i)
    print(sum(curious_numbers))
    print(datetime.now() - start_time)

    # 2 вариант
    start_time = datetime.now()
    factorial_list = [factorial_self(_) for _ in range(n)]
    sum_fact_not_0 = [
        sum(factorial_self(int(c)) for c in str(i))
        for i in range(10 ** 4)
    ]
    sum_fact_0 = [
        sum(factorial_self(int(c)) for c in str(i).zfill(4))
        for i in range(10 ** 4)
    ]
    upper_bound = 10 ** getpower(n, factorial_list)
    print(sum(
        i for i in range(3, upper_bound)
        if i == factorial_digit_sum(i, sum_fact_0, sum_fact_not_0)
    ))
    print(datetime.now() - start_time)


if __name__ == "__main__":
    euler34()

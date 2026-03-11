# Найдите самый большой палиндром,
# полученный умножением двух трехзначных чисел.

from datetime import datetime


def check_palindrom(number: str) -> bool:
    """
    Проверка заданного числа на палиндром.

    Args:
        number: Строковое представление числа.

    Returns:
        True если число является палиндромом, иначе False.
    """
    return number == number[::-1]


def euler04() -> None:
    """
    Решение задачи Эйлера №4.

    Найдите самый большой палиндром,
    полученный умножением двух трехзначных чисел.
    """
    n = 1_000

    # 1 Вариант
    start_time = datetime.now()
    pol = []
    for i in range(100, n):
        for j in range(100, n):
            if check_palindrom(str(i * j)):
                pol.append(i * j)
    print(max(pol))
    print(datetime.now() - start_time)

    # 2 Вариант
    start_time = datetime.now()
    print(max([
        i * j
        for i in range(100, n)
        for j in range(100, n)
        if check_palindrom(str(i * j))
    ]))
    print(datetime.now() - start_time)


if __name__ == "__main__":
    euler04()

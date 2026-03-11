# Найдите последние десять цифр суммы 1^1 + 2^2 + 3^3 + ... + 1000^1000.

from datetime import datetime


def euler48() -> None:
    """
    Решение задачи Эйлера №48.

    Найдите последние десять цифр суммы 1^1 + 2^2 + 3^3 + ... + 1000^1000.
    """
    n = 10

    # 1 вариант
    start_time = datetime.now()
    long_number = 0
    for i in range(1, 1001):
        long_number += i ** i
    print(str(long_number)[-n:])
    print(datetime.now() - start_time)

    # 2 вариант
    start_time = datetime.now()
    result, long_number = 0, 10 ** n
    for i in range(1, 1001):
        temp = i
        for j in range(1, i):
            temp *= i
            temp %= long_number
        result += temp
        result %= long_number
    print(result)
    print(datetime.now() - start_time)

    # 3 вариант
    start_time = datetime.now()
    print(str(sum(i ** i for i in range(1, 1001)))[-n:])
    print(datetime.now() - start_time)


if __name__ == "__main__":
    euler48()

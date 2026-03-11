# Какова сумма цифр числа 2 в степени 1000?

from datetime import datetime


def euler16() -> None:
    """
    Решение задачи Эйлера №16.

    Какова сумма цифр числа 2 в степени 1000?
    """
    n = 1_000

    # 1 вариант
    start_time = datetime.now()
    print(sum(int(x) for x in str(2 ** n)))
    print(datetime.now() - start_time)

    # 2 вариант
    start_time = datetime.now()
    print(sum(map(int, str(2 ** n))))
    print(datetime.now() - start_time)


if __name__ == "__main__":
    euler16()

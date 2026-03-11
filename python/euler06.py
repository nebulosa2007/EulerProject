# Найдите разность между суммой квадратов и квадратом суммы первых
# ста натуральных чисел.

from datetime import datetime
from functools import reduce


def euler06() -> None:
    """
    Решение задачи Эйлера №6.

    Найдите разность между суммой квадратов и квадратом суммы первых
    ста натуральных чисел.
    """
    n = 100

    # 1 Вариант
    start_time = datetime.now()
    list_num = list(range(n + 1))
    print(
        reduce(lambda x, y: x + y, list_num) ** 2
        - reduce(lambda x, y: x + y, map(lambda x: x ** 2, list_num))
    )
    print(datetime.now() - start_time)

    # 2 Вариант
    start_time = datetime.now()
    print(sum(range(n + 1)) ** 2 - sum(x ** 2 for x in range(n + 1)))
    print(datetime.now() - start_time)


if __name__ == "__main__":
    euler06()

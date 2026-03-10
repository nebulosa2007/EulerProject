# Какова миллионная словарная перестановка из цифр
# 0, 1, 2, 3, 4, 5, 6, 7, 8 и 9?

from datetime import datetime
from itertools import permutations


def euler24() -> None:
    """
    Решение задачи Эйлера №24.

    Какова миллионная словарная перестановка из цифр 0-9?
    """
    n = 1_000_000

    # 1 вариант
    start_time = datetime.now()
    print(*list(permutations(range(10), 10))[n - 1])
    print(datetime.now() - start_time)

    # 2 вариант
    start_time = datetime.now()
    pass
    print(datetime.now() - start_time)


if __name__ == "__main__":
    euler24()

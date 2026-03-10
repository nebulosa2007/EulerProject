# Найдите значение следующего выражения числа Чамбертоуна:
# d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000

from datetime import datetime
from functools import reduce


def euler40() -> None:
    """
    Решение задачи Эйлера №40.

    Найдите значение произведения цифр числа Чамбертоуна.
    """
    n = 1_000_000

    # 1 вариант
    start_time = datetime.now()
    champernowne = ''.join(str(_) for _ in range(n + 1))
    positions = [10 ** _ for _ in range(len(str(n)))]
    result = reduce(
        lambda x, y: x * y,
        [int(champernowne[pos]) for pos in positions]
    )
    print(result)
    print(datetime.now() - start_time)

    # 2 вариант
    start_time = datetime.now()
    pass
    print(datetime.now() - start_time)


if __name__ == "__main__":
    euler40()

# Сколькими разными способами можно составить £2, используя
# любое количество монет?

from datetime import datetime
from typing import List


def num_sets(n: int, coins: List[int]) -> int:
    """
    Возвращает количество вариантов расстановки суммы n.

    Args:
        n: Искомая сумма.
        coins: Список номиналов монет.

    Returns:
        Количество способов составить сумму.
    """
    if n < 0:
        return 0
    if n == 0:
        return 1
    if len(coins) == 1:
        return 1 if n % coins[0] == 0 else 0
    return num_sets(n - coins[0], coins) + num_sets(n, coins[1:])


def euler31() -> None:
    """
    Решение задачи Эйлера №31.

    Сколькими разными способами можно составить £2?
    """
    n = 200
    coins = [1, 2, 5, 10, 20, 50, 100, 200]

    # 1 вариант
    start_time = datetime.now()
    sets = [1] + [0] * n
    for coin in coins:
        for i in range(len(sets) - coin):
            sets[i + coin] += sets[i]
    print(sets[-1])
    print(datetime.now() - start_time)

    # 2 вариант
    start_time = datetime.now()
    print(num_sets(n, coins[::-1]))
    print(datetime.now() - start_time)


if __name__ == "__main__":
    euler31()

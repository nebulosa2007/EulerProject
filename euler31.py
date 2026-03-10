# Сколькими разными способами можно составить £2, используя
# любое количество монет?

from datetime import datetime

n = 200

coins = [1, 2, 5, 10, 20, 50, 100, 200]


def num_sets(n, coins):
    """Возвращает количество вариантов расстановки суммы n,
    через список слагаемых coins"""
    if n < 0: return 0
    if n == 0: return 1
    if len(coins) == 1: return n % coins[0] == 0
    return num_sets(n - coins[0], coins) + num_sets(n, coins[1:])

# 1 вариант
start_time = datetime.now()
sets = [1] + [0] * n
for coin in coins:
    for i in range(len(sets) - coin):
        sets[i + coin] += sets[i]
else:
    print(sets[-1])
print(datetime.now() - start_time)

# 2 вариант
start_time = datetime.now()
print(num_sets(n, coins[::-1]))
print(datetime.now() - start_time)

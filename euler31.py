# Сколькими разными способами можно составить £2, используя
# любое количество монет?

from project_euler_defs import *

n = 200

coins = [1, 2, 5, 10, 20, 50, 100, 200]

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

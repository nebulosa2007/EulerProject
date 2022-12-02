# Каково наименьшее нечетное составное число, которое нельзя записать
# в виде суммы простого числа и удвоенного квадрата?

from project_euler_defs import *

n = 10_000

# 1 вариант
start_time = datetime.now()
goldbah_conjecture = set()
for p in set(eratosfen(n)):
    for k in range(int(n ** 0.5)):
        goldbah_conjecture.add(p + 2 * k * k)
else:
    print(min(set(range(3, n, 2)) - goldbah_conjecture))
print(datetime.now() - start_time)

# 2 вариант
start_time = datetime.now()
pass
print(datetime.now() - start_time)

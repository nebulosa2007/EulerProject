# Каково наименьшее нечетное составное число, которое нельзя записать
# в виде суммы простого числа и удвоенного квадрата?

from datetime import datetime

n = 10_000


def eratosfen(number):
    """Решето Эратосфена: генерация простых чисел вплоть до заданного числа"""
    sieve = list(range(number + 1))
    sieve[1] = 0
    for i in sieve:
        if i > 1:
            for j in range(2 * i, len(sieve), i):
                sieve[j] = 0
    return sieve

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

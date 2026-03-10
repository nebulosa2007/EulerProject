# Какое число является 10001-м простым числом?

from datetime import datetime
from itertools import islice, count

n = 10_001


def primes(dimension=None):
    """Итерируемая функция генерация простых чисел"""
    start = 2 if dimension is None else 10 ** (dimension - 1) + 1
    ints = count(start)
    while True:
        p = next(ints)
        yield p
        ints = filter(p.__rmod__, ints)

# 1 Вариант
start_time = datetime.now()
number = primes()
for i in range(n):
    prime = next(number)
else:
    print(prime)
print(datetime.now() - start_time)

# 2 Вариант
start_time = datetime.now()
print(list(islice(primes(), n))[-1])
print(datetime.now() - start_time)

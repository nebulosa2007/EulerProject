# Какое число является 10001-м простым числом?

from itertools import islice, count
from datetime import datetime

n = 10_001


def primes():
    ints = count(2)
    while True:
        p = next(ints)
        yield p
        ints = filter(p.__rmod__, ints)

if __name__ == '__main__':
    # 1 Вариант
    start_time = datetime.now()
    print(list(islice(primes(), n))[-1])
    print(datetime.now() - start_time)

    # 2 Вариант
    start_time = datetime.now()
    pass
    print(datetime.now() - start_time)

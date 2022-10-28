# Найдите сумму всех чисел меньше 1000, кратных 3 или 5.

from functools import reduce
from datetime import datetime

n = 1_000

if __name__ == '__main__':
    # Вариант 1
    start_time = datetime.now()
    sum = 0
    for i in range(n):
        if i % 3 == 0 or i % 5 == 0:
            sum += i
    print(sum)
    print(datetime.now() - start_time)

    # Вариант 2
    start_time = datetime.now()
    print(reduce(lambda x, y: x + y,
        list(filter(lambda x: x % 3 == 0 or x % 5 == 0,
            list(range(n))))))
    print(datetime.now() - start_time)

# Найдите сумму цифр в числе 100!

from datetime import datetime
from functools import reduce
from math import factorial

n = 100


def factorial_self(number):
    return reduce(lambda x, y: x * y, range(1, number + 1))


if __name__ == '__main__':
    # 1 вариант
    start_time = datetime.now()
    print(sum(int(x) for x in list(str(factorial_self(n)))))
    print(datetime.now() - start_time)

    # 2 вариант
    start_time = datetime.now()
    print(sum(int(x) for x in str(factorial(n))))
    print(datetime.now() - start_time)

# Найдите сумму цифр в числе 100!

from datetime import datetime
from functools import reduce, lru_cache
from math import factorial

n = 100


@lru_cache(2 ** 5)
def factorial_self(number):
    """Возвращает факториал заданного числа"""
    return 1 if number ==0 else reduce(lambda x, y: x * y, range(1, number + 1))

# 1 вариант
start_time = datetime.now()
print(sum(int(x) for x in list(str(factorial_self(n)))))
print(datetime.now() - start_time)

# 2 вариант
start_time = datetime.now()
print(sum(int(x) for x in str(factorial(n))))
print(datetime.now() - start_time)

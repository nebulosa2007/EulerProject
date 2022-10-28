# Каков самый большой делитель числа 600 851 475 143,
# являющийся простым числом?

from datetime import datetime
from re import fullmatch
from functools import lru_cache

n = 600_851_475_143


def isPrime_reg(n):
    return not bool(fullmatch(r'(11+?)\1+', '1' * n))


@lru_cache(2 ** 5)
def isprime(number: int):
    a, k = number, 0
    for i in range(2, a // 2 + 1):
        k += 1 if a % i == 0 else 0
    return True if k <= 0 else False


def maxcommondivisors(n):
    divisor, nodarray = 2, []
    while divisor ** 2 <= n:
        if n % divisor == 0:
            n //= divisor
            if isprime(divisor):
                nodarray.append(divisor)
        else:
            divisor += 1
    if n != 1:
        nodarray.append(n)
    return nodarray


if __name__ == '__main__':
    # 1 вариант
    start_time = datetime.now()
    print(max(maxcommondivisors(n)))
    print(datetime.now() - start_time)

    # 2 вариант
    start_time = datetime.now()
    pass
    print(datetime.now() - start_time)

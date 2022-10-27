# Каков самый большой делитель числа 600 851 475 143,
# являющийся простым числом?

from datetime import datetime
import re
from euler05 import eratosfen

n = 600_851_475_143


def isPrime_reg(n):
    return not bool(re.fullmatch(r'(11+?)\1+', '1' * n))


def isprime(number: int):
    a = number
    k = 0
    for i in range(2, a // 2 + 1):
        if (a % i == 0):
            k = k + 1
    if (k <= 0):
        return True
    else:
        return False


def maxcommondivisors(n):
    divisor = 2
    nodarray = []
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

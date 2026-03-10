# Каков самый большой делитель числа 600 851 475 143,
# являющийся простым числом?

from datetime import datetime

n = 600_851_475_143


def prime_factors_list(n):
    """Возвращет список простых множителей заданного числа"""
    divisor, nodarray = 2, []
    while divisor ** 2 <= n:
        if n % divisor == 0:
            n //= divisor
            nodarray.append(divisor)
        else: divisor += 1
    if n != 1: nodarray.append(n)
    return nodarray

# 1 вариант
start_time = datetime.now()
print(max([_ for _ in prime_factors_list(n)]))
print(datetime.now() - start_time)

# 2 вариант
start_time = datetime.now()
pass
print(datetime.now() - start_time)

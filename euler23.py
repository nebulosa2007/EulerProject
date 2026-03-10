# Найдите сумму всех положительных чисел, которые не могут быть записаны как
# сумма двух избыточных чисел.

from datetime import datetime
from math import ceil, sqrt

n = 28_123


def all_factors_list(number, justcount=False):
    """Возвращает список делителей заданного числа, либо количество делителей"""
    divisor, divisor_list = 2, [1, number]
    for i in range(2, ceil(sqrt(number)) + 1):
        if number % i == 0:
            if justcount:
                divisor += 2
            else: 
                divisor_list.append(i)
                divisor_list.append(number // i)
    if justcount:
        return divisor - 1 if ceil(sqrt(number)) ** 2 == number else divisor
    else:
        return divisor_list[:-1] if ceil(sqrt(number)) ** 2 == number else divisor_list

# 1 вариант
start_time = datetime.now()
number_list = [0 for _ in range(n)]
start_sum = sum([_ for _ in range(n)])
for i in range(n):
    divisor_list = all_factors_list(i)[:-1]
    if sum(divisor_list) > i: number_list[i] = i
temp = [i * 2 for i in set(number_list) if i * 2 < n]
print(start_sum - sum(i * 2 for i in set(number_list) if i * 2 < n))
print(datetime.now() - start_time)

# 2 вариант
start_time = datetime.now()
pass
print(datetime.now() - start_time)

# Подсчитайте сумму всех дружественных чисел меньше 10000

from project_euler_defs import *

n = 10_000

# 1 вариант
start_time = datetime.now()
print(all_factors_list(20 ** 2))
amicable_pairs = []
for x in range(10, n):
    if x not in amicable_pairs:
        # print(x, all_factors_list(x))
        x_sum_divisors = sum(all_factors_list(x)) - x
        y_sum_divisors = sum(all_factors_list(x_sum_divisors)) - x_sum_divisors
        if y_sum_divisors == x and x != x_sum_divisors:
            amicable_pairs.append(x)
            amicable_pairs.append(x_sum_divisors)
print(sum(amicable_pairs))
print(datetime.now() - start_time)

# 2 вариант
start_time = datetime.now()
divisorsum = [0] * n
for i in range(1, n):
    for j in range(i * 2, n, i):
        divisorsum[j] += i
sum_amic_pairs = 0
for i in range(1, n):
    j = divisorsum[i]
    if j != i and j < n and divisorsum[j] == i: sum_amic_pairs += i
print(sum_amic_pairs)
print(datetime.now() - start_time)

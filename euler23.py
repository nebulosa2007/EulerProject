# Найдите сумму всех положительных чисел, которые не могут быть записаны как
# сумма двух избыточных чисел.

from project_euler_defs import *

n = 28_123

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

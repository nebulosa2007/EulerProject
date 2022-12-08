# Каково первое треугольное число, у которого более пятисот делителей?

from project_euler_defs import *

n = 500

# 1 вариант
start_time = datetime.now()
i = 1
while (divisors := len(all_factors_list(triangle := figurate_number(i, 3)))) < n:
    i += 1
print(f'{triangle}: {divisors=}')
print(datetime.now() - start_time)

# 2 вариант
start_time = datetime.now()
i = 1
while (divisors := count_divisors(triangle := figurate_number(i, 3))) < n:
    i += 1
print(f'{triangle}: {divisors=}')
print(datetime.now() - start_time)

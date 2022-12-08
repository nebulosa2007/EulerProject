# Каково первое треугольное число, у которого более пятисот делителей?

from project_euler_defs import *

n = 500

# 1 вариант
start_time = datetime.now()
i = 1
while (divisors := all_factors_list(triangle := figurate_number(i, 3), justcount=True)) < n:
    i += 1
print(f'{i}-th triangle number: {triangle} with {divisors} divisors')
print(datetime.now() - start_time)

# 2 вариант
start_time = datetime.now()
pass
print(datetime.now() - start_time)

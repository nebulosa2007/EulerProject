# Каково первое треугольное число, у которого более пятисот делителей?

from project_euler_defs import *

n = 500

# 1 вариант
start_time = datetime.now()
triangle_number, i = 1, 1
factors_long_time_number = factors_long_time(triangle_number)
if n <= 150:  # очень долгое решение полным перебором! Ограничитель
    while len(factors_long_time_number) < n:
        i += 1
        triangle_number += i
        factors_long_time_number = factors_long_time(triangle_number)
    print(triangle_number, ":",
            factors_long_time_number, "-",
            len(factors_long_time_number))
print(datetime.now() - start_time)

# 2 вариант
start_time = datetime.now()
triangle_number = defactoring(n)
factors_long_time_number = factors_long_time(triangle_number)
print(triangle_number, ":",
        factors_long_time_number, "-",
        len(factors_long_time_number))
print(datetime.now() - start_time)

# Найдите самый большой палиндром,
# полученный умножением двух трехзначных чисел.

from project_euler_defs import *

n = 1_000

# 1 Вариант
start_time = datetime.now()
pol = []
for i in range(100, n):
    for j in range(100, n):
        if check_palindrom(str(i * j)):
            pol.append(i * j)
print(max(pol))
print(datetime.now() - start_time)

# 2 Вариант
start_time = datetime.now()
print(max([i * j for i in range(100, n)
            for j in range(100, n)
            if check_palindrom(str(i * j))]))
print(datetime.now() - start_time)

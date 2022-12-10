# Сколько существует таких маршрутов в сетке 20×20?

from project_euler_defs import *

n = 20

# 1 вариант
start_time = datetime.now()
print(func(n, n))
print(datetime.now() - start_time)

# 2 вариант
start_time = datetime.now()
counter = 1
for _ in range(n):
    counter = counter * (2 * n - _) // (1 + _)
else: 
    print(counter)
print(datetime.now() - start_time)

# 3 вариант
start_time = datetime.now()
print(int(factorial(2 * n) / (factorial(n) ** 2)))
print(datetime.now() - start_time)

# 4 вариант
start_time = datetime.now()
dp = {(0, 0): 1}
for i in range(n + 1):
    for j in range(n + 1):
        if i == 0 or j == 0: dp[(i, j)] = 1
        else: dp[(i, j)] = dp[(i - 1, j)] + dp[(i, j - 1)]
print(dp[(n, n)])
print(datetime.now() - start_time)

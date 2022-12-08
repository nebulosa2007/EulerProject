# Какое самое маленькое число делится нацело на все числа от 1 до 20?

from project_euler_defs import *

n = 20

# 1 Вариант
start_time = datetime.now()
result = 1
for k in set(eratosfen(n)) - {0}:
    i = 1
    while k ** (i + 1) < n:
        i += 1
    result *= k ** i
print(result)
print(datetime.now() - start_time)

# 2 Вариант
start_time = datetime.now()
result = 1
for k in range(n + 1):
    if isprime(k):
        result *= k ** max([_ for _ in range(n // 2) if k ** _ < n])
else:
    print(result)
print(datetime.now() - start_time)

# Найдите последние десять цифр суммы 1^1 + 2^2 + 3^3 + ... + 1000^1000.

from project_euler_defs import *

n = 10

# 1 вариант
start_time = datetime.now()
long_number = 0
for i in range(1, 1000):
    long_number += i ** i
else:
    print(str(long_number)[-n:])
print(datetime.now() - start_time)

# 2 вариант
start_time = datetime.now()
result, long_number = 0, 10 ** n
for i in range(1, 1000):
    temp = i
    for j in range(1, i):
        temp *= i
        temp %= long_number
    result += temp
    result %= long_number
else:
    print(result)
print(datetime.now() - start_time)

# 3 вариант
start_time = datetime.now()
print(str(sum([_ ** _ for _ in range(1, 1000)]))[-n:])
print(datetime.now() - start_time)

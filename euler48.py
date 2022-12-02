# Найдите последние десять цифр суммы 1^1 + 2^2 + 3^3 + ... + 1000^1000.

from project_euler_defs import *

n = 1000

# 1 вариант
start_time = datetime.now()
long_number = 0
for i in range(1, 1000):
    long_number += i ** i
else:
    print(str(long_number)[-10:])
print(datetime.now() - start_time)

# 2 вариант
start_time = datetime.now()
result = 0
long_number = 10 ** 10  # степень - количество искомых последних цифр
for i in range(1, n):
    temp = i
    for j in range(1, i):
        temp *= i
        temp %= long_number
    result += temp
    result %= long_number
else:
    print(result)
print(datetime.now() - start_time)

# Начиная с числа 1 и двигаясь дальше вправо по часовой стрелке,
# считаем суммы диагоналей. Какова сумма чисел в диагоналях спирали
# 1001 на 1001, образованной таким же способом?

from project_euler_defs import *

n = 1001

# 1 вариант
start_time = datetime.now()
num = 1
print(sum(num := num + lyr for lyr in range(2, n, 2) for _ in range(4)) + 1)
print(datetime.now() - start_time)

# 2 вариант
start_time = datetime.now()
print(sum(map(lambda i: 4 * i ** 2 - 6 * (i - 1), range(3, n + 1, 2))) + 1)
print(datetime.now() - start_time)

# 3 вариант
start_time = datetime.now()
print((4 * n ** 3 + 3 * n ** 2 + 8 * n - 9) // 6)
print(datetime.now() - start_time)

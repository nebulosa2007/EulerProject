# Найдите сумму всех простых чисел меньше двух миллионов.

from project_euler_defs import *

n = 2_000_000

# 1 Вариант
start_time = datetime.now()
print(reduce(lambda x, y: x + y, eratosfen(n)))
print(datetime.now() - start_time)

# 2 Вариант
start_time = datetime.now()
pass
print(datetime.now() - start_time)

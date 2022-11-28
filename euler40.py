# Найдите значение следующего выражения числа Чамбертоуна:
# d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000

from project_euler_defs import *

n = 1_000_000

# 1 вариант
start_time = datetime.now()
print(reduce(lambda x, y: x * y,
             [int(''.join(str(_) for _ in range(n + 1))[_])
              for _ in [10 ** _ for _ in range(len(str(n)))]]))
print(datetime.now() - start_time)

# 2 вариант
start_time = datetime.now()
pass
print(datetime.now() - start_time)

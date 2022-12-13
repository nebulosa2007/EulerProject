# Какова миллионная словарная перестановка из цифр
# 0, 1, 2, 3, 4, 5, 6, 7, 8 и 9?

from project_euler_defs import *

n = 1_000_000

# 1 вариант
start_time = datetime.now()
print(*list(permutations([_ for _ in range(10)], 10))[n - 1])
print(datetime.now() - start_time)

# 2 вариант
start_time = datetime.now()
pass
print(datetime.now() - start_time)

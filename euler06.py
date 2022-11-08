# Найдите разность между суммой квадратов и квадратом суммы первых
# ста натуральных чисел.

from project_euler_defs import *

n = 100

# 1 Вариант
start_time = datetime.now()
list_num = list(range(n + 1))
print(reduce((lambda x, y: x + y), list_num) ** 2
      - reduce((lambda x, y: x + y),
                  list(map(lambda x: x ** 2, list_num))))
print(datetime.now() - start_time)

# 2 Вариант
start_time = datetime.now()
print(sum(_ for _ in range(n + 1)) ** 2
      - sum(_ ** 2 for _ in range(n + 1)))
print(datetime.now() - start_time)

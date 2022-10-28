# Найдите разность между суммой квадратов и квадратом суммы первых
# ста натуральных чисел.

from functools import reduce
from datetime import datetime

n = 100

if __name__ == '__main__':
    # 1 Вариант
    start_time = datetime.now()
    list_num = list(range(n + 1))
    print(reduce((lambda x, y: x + y), list_num) ** 2 -
        reduce((lambda x, y: x + y),
        list(map(lambda x: x ** 2, list_num))))
    print(datetime.now() - start_time)

    # 2 Вариант
    start_time = datetime.now()
    print(sum(x for x in range(n + 1)) ** 2 - sum(x ** 2 for x in range(n + 1)))
    print(datetime.now() - start_time)

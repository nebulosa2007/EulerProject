# Найдите пару пятиугольных чисел Pj и Pk, для которых сумма и разность
# являются пятиугольными числами и значение D = |Pk − Pj| минимально,
# и дайте значение D в качестве ответа.

from project_euler_defs import *

n = None

# 1 вариант
start_time = datetime.now()
i, flag = 1, True
while flag:
    i += 1
    next_pent = figurate_number(i, 5)
    for j in range(i - 1, 0, -1):
        result = next_pent - (prev_pent := figurate_number(j, 5))
        if (isfigurate_number(result, 5)
                and isfigurate_number(prev_pent + next_pent, 5)):
            flag = False
            break
print(result)
print(datetime.now() - start_time)

# 2 вариант
start_time = datetime.now()
pass
print(datetime.now() - start_time)

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
    next_pent = pentagonal_number(i)
    for j in range(i - 1, 0, -1):
        result = next_pent - (prev_pent := pentagonal_number(j))
        if ispentagonal(result) and ispentagonal(prev_pent + next_pent):
            flag = False
            break
print(result)
print(datetime.now() - start_time)

# 2 вариант
start_time = datetime.now()
pass
print(datetime.now() - start_time)

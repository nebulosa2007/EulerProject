# Какова сумма цифр числа 2 в степени 1000?

from project_euler_defs import *

n = 1_000

# 1 вариант
start_time = datetime.now()
print(sum(int(_) for _ in list(str(2 ** n))))
print(datetime.now() - start_time)

# 2 вариант
start_time = datetime.now()
print(sum(map(int, str(2 ** n))))
print(datetime.now() - start_time)

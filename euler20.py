# Найдите сумму цифр в числе 100!

from project_euler_defs import *

n = 100

# 1 вариант
start_time = datetime.now()
print(sum(int(x) for x in list(str(factorial_self(n)))))
print(datetime.now() - start_time)

# 2 вариант
start_time = datetime.now()
print(sum(int(x) for x in str(factorial(n))))
print(datetime.now() - start_time)

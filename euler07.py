# Какое число является 10001-м простым числом?

from project_euler_defs import *

n = 10_001

# 1 Вариант
start_time = datetime.now()
print(list(islice(primes(), n))[-1])
print(datetime.now() - start_time)

# 2 Вариант
start_time = datetime.now()
pass
print(datetime.now() - start_time)

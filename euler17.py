# Сколько букв понадобится для записи всех чисел от 1 до 1000
# (one thousand) включительно?

from project_euler_defs import *

n = 1_000

# 1 вариант
start_time = datetime.now()
print(f'From 1 to {n} sum symbols is:',
      sum(len(''.join(numerals(x))) for x in range(1, n + 1)))
print(datetime.now() - start_time)

# 2 вариант
start_time = datetime.now()
pass
print(datetime.now() - start_time)

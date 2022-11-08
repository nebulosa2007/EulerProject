# Сколько букв понадобится для записи всех чисел от 1 до 1000
# (one thousand) включительно?

from project_euler_defs import *

n = 1000

# 1 вариант
start_time = datetime.now()
sum_symbols = 0
for x in range(1, n + 1):
    sum_symbols += len(''.join(numerals(x)))
print("From 1 to", x, "sum symbols is:", sum_symbols)
print(datetime.now() - start_time)

# 2 вариант
start_time = datetime.now()
# print(''.join(numerals(999)))
print(datetime.now() - start_time)

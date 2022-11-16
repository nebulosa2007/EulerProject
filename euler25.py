# Каков порядковый номер первого члена последовательности
# Фибоначчи, содержащего 1000 цифр?

from project_euler_defs import *

n = 1_000

# 1 вариант
start_time = datetime.now()
fb_counter = 0
iterator = fibonacci()
fb_num = next(iterator)
while len(str(fb_num)) < n:
    fb_counter += 1
    fb_num = next(iterator)
print(fb_counter)
print(datetime.now() - start_time)

# 2 вариант
start_time = datetime.now()
fb_counter = 0
for i in fibonacci():
    if len(str(i)) == n:
        break
    fb_counter += 1
print(fb_counter)
print(datetime.now() - start_time)

# Найдите сумму всех четных элементов ряда Фибоначчи, которые не превышают
# четыре миллиона.

from datetime import datetime
from itertools import takewhile
from functools import reduce

n = 4_000_000


def fibonacci(f1=0, f2=1):
    while True:
        yield f1
        f1, f2 = f2, f1 + f2


# 1 Вариант
start_time = datetime.now()
odd_fb_sum = 0
iterator = fibonacci()
fb_num = next(iterator)
while fb_num < n:
    if fb_num % 2 == 0:
        odd_fb_sum += fb_num
    fb_num = next(iterator)
print(odd_fb_sum)
print(datetime.now() - start_time)

# 2 Вариант
start_time = datetime.now()
print(reduce(lambda x, y: x + y,
    filter(lambda s: s % 2 == 0,
        (takewhile(lambda f: f < n,
            fibonacci())))))
print(datetime.now() - start_time)

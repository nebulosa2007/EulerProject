# Найдите значение d < 1000, для которого 1/d в десятичном виде
# содержит самую длинную повторяющуюся последовательность цифр.

from project_euler_defs import *

n = 1_000

# 1 вариант
"""c обычной точностью ответ - неверный. Показан в качестве
вариантов поиска подстрок, более частая задача в Питоне"""
start_time = datetime.now()
patterns = []
for x in range(1, n):
    patterns.append((x, 1 / x, repeat_inside(str(1 / x)[2:])))
max_pattern = max((x[2] for x in patterns), key=len, default='')
print([x for x in patterns if x[2] == max_pattern])
print(datetime.now() - start_time)

# 2 вариант
start_time = datetime.now()
period, ans = 0, {}
for x in range(1, n + 1):
    ans[x] = 0
    while x % 2 == 0:
        x //= 2
    while x % 5 == 0:
        x //= 5
    if x != 1:
        period = next(i for i in count(1) if 10**i % x == 1)
        ans[x] = period

max_period, denominator = ans[1], 1
for x in ans:
    if ans[x] > max_period: max_period, denominator = ans[x], x
else:
    print(denominator, max_period)
# or
print({k: v for k, v in ans.items() if v == max(ans.values())})
# or
print({x: y for x, y in filter(lambda x: ans[x[0]] == max(ans.values()),
                               ans.items())})
print(datetime.now() - start_time)

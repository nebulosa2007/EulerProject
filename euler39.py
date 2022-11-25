# p - периметр прямоугольного треугольника с целочисленными длинами сторон
# {a,b,c} Какое значение p ≤ 1000 дает максимальное число решений?

from project_euler_defs import *

n = 1_000

# 1 вариант
start_time = datetime.now()
perimeter = {}
for p in range(2, n + 1, 2):
    counter_triplets = 0
    for a in range(1, p):
        for b in range(a, p - a):
            if a * a + b * b == (p - a - b) * (p - a - b):
                counter_triplets += 1
    if counter_triplets:
        perimeter[p] = counter_triplets
print({k: v for k, v in perimeter.items() if v == max(perimeter.values())})
print(datetime.now() - start_time)

# 2 вариант
start_time = datetime.now()
p = {}
for a in range(1, 500):
    for b in range(a, 500):
        c = (a**2 + b**2)**0.5
        p_test = a + b + int(c)
        if int(c) == c and p_test <= 1000:
            p[p_test] = p[p_test] + 1 if p_test in p.keys() else 1
print({k: v for k, v in perimeter.items() if v == max(perimeter.values())})
print(datetime.now() - start_time)

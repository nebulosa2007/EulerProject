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
            if a ** 2 + b ** 2 == (p - a - b) ** 2: counter_triplets += 1
    if counter_triplets: perimeter[p] = counter_triplets
print({k: v for k, v in perimeter.items() if v == max(perimeter.values())})
print(datetime.now() - start_time)

# 2 вариант
start_time = datetime.now()
perimeter = {}
for a in range(1, n // 2):
    for b in range(a, n // 2):
        c = (a ** 2 + b ** 2) ** 0.5
        perimeter_test = a + b + int(c)
        if int(c) == c and perimeter_test <= n:
            perimeter[perimeter_test] = (perimeter[perimeter_test] + 1 
                                        if perimeter_test in perimeter.keys() else 1)
print({k: v for k, v in perimeter.items() if v == max(perimeter.values())})
print(datetime.now() - start_time)

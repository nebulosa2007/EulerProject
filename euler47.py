# Найдите первые четыре последовательных числа, каждое из которых имеет четыре
# отличных друг от друга простых множителя. Каким будет первое число?

from project_euler_defs import *

n = 4

# 1 вариант
start_time = datetime.now()
i, counter = 1, 0
while counter < n:
    if len(set(prime_factors_list(i := i + 1))) == n: counter += 1
    else: counter = 0
print(i - n + 1)
print(datetime.now() - start_time)

# 2 вариант
start_time = datetime.now()
siege = [0] * 150_000
for i in range(2, len(siege)):
    if siege[i] == n:
        if (counter := counter + 1) == n: break
    else:
        counter = 0
        if siege[i] == 0: siege[i::i] = [_ + 1 for _ in siege[i::i]]
print(i - n + 1)
print(datetime.now() - start_time)

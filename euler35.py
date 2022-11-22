# Сколько существует круговых простых чисел меньше миллиона?

from project_euler_defs import *

n = 1_000_000

# 1 вариант
start_time = datetime.now()
primes, circular_primes = set(eratosfen(n)) - {0}, []
for i in primes:
    if len(set(list(str(i)))) == 1:
        circular_primes += [i]
        continue

    next_num, circular_primes_check, power = i, [i], len(str(i)) - 1
    for _ in range(power):
        next_num = next_num % 10 * 10 ** power + next_num // 10
        if next_num in primes:
            circular_primes_check.append(next_num)
        else:
            circular_primes_check = []
            break
    circular_primes += [_ for _ in circular_primes_check
                        if _ not in circular_primes]

print(len(circular_primes))
print(datetime.now() - start_time)

# 2 вариант
start_time = datetime.now()

primes_bool, i = [True] * (n + 1), 2
while i * i <= n:
    if primes_bool[i]:
        for j in range(i * 2, n + 1, i):
            primes_bool[j] = False
    i += 1

primes_bool[0] = primes_bool[1] = False
count = 0
for i in range(1, n + 1):
    if primes_bool[i] is False:
        continue
    next_num, flag = str(i), True
    for _ in next_num:
        next_num = next_num[1:] + next_num[0]
        flag &= primes_bool[int(next_num)]
    if flag:
        count += 1
else:
    print(count)

print(datetime.now() - start_time)

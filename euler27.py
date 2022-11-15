# Найдите произведение коэффициентов a < 1000 и b <= 1000 для
# квадратичного выражения, которое выражает максимальное число
# простых чисел для последовательных значений n, начиная с n = 0


from project_euler_defs import *

# n = 1_000

# 1 вариант

start_time = datetime.now()
an = 1
bn = 41
for a in range(-an + 1, an):
    primes = {(0, 0): 0}
    n = 0
    max_n_primes = 0
    for b in range(-bn, bn + 1):
        ans = n ** 2 + a * n + b
        while isprime(ans):
            n += 1
            ans = n ** 2 + a * n + b
        if n > max_n_primes:
            max_n_primes = n
            primes[(a, b)] = max_n_primes
print(primes)
ank = [k for k, v in primes.items() if v == max(primes.values())]
print(ank[0][0] * ank[0][1])
print(datetime.now() - start_time)

# 2 вариант
start_time = datetime.now()
pass
print(datetime.now() - start_time)

# Найдите произведение коэффициентов a < 1000 и b <= 1000 для
# квадратичного выражения, которое выражает максимальное число
# простых чисел для последовательных значений n, начиная с n = 0


from project_euler_defs import *

n = 1_000

# 1 вариант
start_time = datetime.now()
primes_num = sorted(set(eratosfen(n)))
primes_num[0], primes, max_n_primes = 1, primes_num[:], 0
for b in primes_num:
    for a in primes_num:
        i = 0
        for x in range(a, -2 * a, -2 * a):
            while True:
                quadratic = i**2 + x * i + b
                if quadratic not in primes:
                    if isprime(quadratic) and quadratic > 0:
                        primes.append(quadratic)
                    else:
                        if i - 1 > max_n_primes:
                            max_n_primes, axb = i - 1, x * b
                        break
                i += 1
print(axb)
print(datetime.now() - start_time)

# 2 вариант
start_time = datetime.now()
pass
print(datetime.now() - start_time)

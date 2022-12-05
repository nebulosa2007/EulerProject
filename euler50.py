# Какое из простых чисел меньше одного миллиона можно записать в
# виде суммы наибольшего количества последовательных простых чисел?

from project_euler_defs import *

n = 1_000_000

# 1 вариант
start_time = datetime.now()
con_primes = []
for i in primes():
    if sum(con_primes) + i >= n:
        while not isprime(sum(con_primes)):
            con_primes = con_primes[1:]
        break
    else:
        con_primes.append(i)
print(sum(con_primes), len(con_primes))
print(datetime.now() - start_time)

# 2 вариант
start_time = datetime.now()
pass
print(datetime.now() - start_time)

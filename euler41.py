# Какое существует наибольшее n-значное пан-цифровое простое число?

from project_euler_defs import *

n = 9

# 1 вариант
start_time = datetime.now()
pan_primes = []
for z in range(n, 1, -1):
    pan_primes_check = [int(''.join(str(_) for _ in x))
                        for x in list(permutations(
                                      [_ for _ in range(1, z + 1)], z))
                        if isprime(int(''.join(str(_) for _ in x)))]
    if pan_primes_check != []:
        pan_primes.append(max(pan_primes_check))
else:
    print(max(pan_primes))
print(datetime.now() - start_time)

# 2 вариант
start_time = datetime.now()
pass
print(datetime.now() - start_time)

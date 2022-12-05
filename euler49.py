# Какое 12-значное число образуется, если объединить три члена
# этой прогрессии?

from project_euler_defs import *

n = 4

# 1 вариант
start_time = datetime.now()
prime_permutation = []
primes = [i for i in set(eratosfen(10 ** n)) if i > 999]
for sets_primes in primes:
    pr_check = sorted(list(set([x for x in [int(''.join(x))
                for x in permutations(str(sets_primes))]
                                         if x in primes])))
    if len(pr_check) >= 3:
        if found := int(twelve_digit(pr_check)):
            if found not in prime_permutation:
                prime_permutation.append(found)
else:
    print(prime_permutation[-1])
print(datetime.now() - start_time)

# 2 вариант
start_time = datetime.now()
pass
print(datetime.now() - start_time)

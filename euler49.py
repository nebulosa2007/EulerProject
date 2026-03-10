# Какое 12-значное число образуется, если объединить три члена
# этой прогрессии?

from datetime import datetime
from itertools import permutations


def eratosfen(number):
    """Решето Эратосфена: генерация простых чисел вплоть до заданного числа"""
    sieve = list(range(number + 1))
    sieve[1] = 0
    for i in sieve:
        if i > 1:
            for j in range(2 * i, len(sieve), i):
                sieve[j] = 0
    return sieve


def twelve_digit(pan_primes_check):
    for i in range(len(pan_primes_check)):
        for j in range(i + 1, len(pan_primes_check)):
            delta = pan_primes_check[j] - pan_primes_check[i]
            if pan_primes_check[j] + delta in pan_primes_check:
                return (str(pan_primes_check[i]) + str(pan_primes_check[j])
                        + str(pan_primes_check[j] + delta))
    return False


def euler49():
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


if __name__ == "__main__":
    euler49()

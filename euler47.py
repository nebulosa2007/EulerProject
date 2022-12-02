# Найдите первые четыре последовательных числа, каждое из которых имеет четыре
# отличных друг от друга простых множителя. Каким будет первое число?

from project_euler_defs import *

n = 4

# 1 вариант
start_time = datetime.now()
pass
print(datetime.now() - start_time)

# 2 вариант
start_time = datetime.now()


def solve():
    """ Compute the answer to Project Euler's problem #47 """

    target = 4  # number of prime factors and successive integers
    limit = 150000  # arbitrary upper-bound on the search, found by trial and error
    n_prime_divisors = [0] * limit  # the number of prime divisors of each integer considered

    run_length = 0  # length of the current run of valid integers
    for n in range(2, limit):
        if n_prime_divisors[n] == 0:
            # n is prime, sieve out multiples of n
            for m in range(2 * n, limit, n):
                n_prime_divisors[m] += 1  # m is divisible by n (prime)
            run_length = 0  # n is invalid, reset our run counter
        elif n_prime_divisors[n] == target:
            run_length += 1  # n is valid, increment our run counter
        else:
            run_length = 0  # n is invalid, reset our run counter

        if run_length == target:
            return n - target + 1  # we've found the smallest target run


print(solve())


def p44(L, nf, ns):
    L += ns
    f = [0] * L
    c = 0
    for n in range(2, L):
        if f[n] == nf:
            c += 1
            if c == ns:
                print(n - ns + 1)
                c -= 1
        else:
            c = 0
            if f[n] == 0:
                f[n::n] = [x + 1 for x in f[n::n]]
    return


p44(300000, 4, 4)
print(datetime.now() - start_time)

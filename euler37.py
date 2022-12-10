# Найдите сумму единственных одиннадцати простых чисел, из которых можно
# выбрасывать цифры как справа налево, так и слева направо, но числа при
# этом остаются простыми.

from project_euler_defs import *

n = 11

# 1 вариант
start_time = datetime.now()
dimension = 1_000_000  # Эмпирически подобрана размерность
primes = list(set(eratosfen(dimension)) - {0, 2, 3, 5, 7})
trucalable_primes, counter = [], 0
while len(trucalable_primes) < n or primes[counter] > dimension:
    next_prime, counter = primes[counter], counter + 1
    if all(map(isprime, del_digit_left_or_right(next_prime))):
        trucalable_primes.append(next_prime)
print(sum(trucalable_primes))
print(datetime.now() - start_time)

# 2 вариант
start_time = datetime.now()
c = s = 0
i = n
while c < n:
    if all(map(isprime, del_digit_left_or_right(i))):
        c += 1
        s += i
    i += 2
print(s)
print(datetime.now() - start_time)

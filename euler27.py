# Найдите произведение коэффициентов a < 1000 и b <= 1000 для
# квадратичного выражения, которое выражает максимальное число
# простых чисел для последовательных значений n, начиная с n = 0


from project_euler_defs import *

n = 50_000

# 1 вариант
start_time = datetime.now()
an = 1000
bn = 1000
primes_num = set(eratosfen(1000000))
primes_num.remove(0)
print(datetime.now() - start_time)
list_pri = {}
max_n_primes = 0
for a in range(-an + 1, an):
    n = 0
    for b in range(-bn, bn + 1):
        while n ** 2 + a * n + b in primes_num:
            n += 1
        if n > max_n_primes:
            max_n_primes = n
            list_pri[(a, b)] = n
# print(list_pri)
print(len(list_pri))
print(max(list_pri.values()))
print(datetime.now() - start_time)
ank = [k for k, v in list_pri.items() if v == max(list_pri.values())]
print(ank, max(list_pri.values()))
print(ank[0][0] * ank[0][1])
print(datetime.now() - start_time)

# 2 вариант
start_time = datetime.now()

def sieve(n):
    is_prime = [True]*n
    is_prime[0] = False
    is_prime[1] = False
    for i in range(2,int(n**0.5+1)):
        index = i*2
        while index < n:
            is_prime[index] = False
            index = index+i
    prime = []
    for i in range(n):
        if is_prime[i] == True:
            prime.append(i)
    return prime

def is_prime(n):
    """function to check if the number
    is prime or not"""
    for i in range(2,int(abs(n)**0.5)+1):
        if n%i == 0:
            return False
    return True

#primes below 1000
primes1000 = sieve(1000)

#copy of primes1000 variable
primes = primes1000[:]

#assume the largest value is 0 at start
largest = 0

#looping through a quadratic equation
for b in primes1000:
    for a in primes1000:
        i = 0
        #positive a and b
        while True:
            quadratic = i**2+a*i+b
            if quadratic not in primes:
                if is_prime(quadratic):
                    primes.append(quadratic)
                else:
                    if i-1 > largest:
                        largest = i-1
                        axb = a*b
                    break
            i += 1
        i = 0
        #negative a and positive b
        while True:
            quadratic = i**2-a*i+b
            if quadratic not in primes:
                if is_prime(quadratic) and quadratic>0:
                    primes.append(quadratic)
                else:
                    if i-1 > largest:
                        largest = i-1
                        axb = -1*a*b
                    break
            i += 1

#printing the largest value of a*b
print(axb)
print(datetime.now() - start_time)

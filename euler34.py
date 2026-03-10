# 145 является любопытным числом, поскольку 1! + 4! + 5! = 1 + 24 + 120 = 145.
# Найдите сумму всех чисел, каждое из которых равно сумме факториалов своих
# цифр. Примечание: поскольку 1! = 1 и 2! = 2 не являются суммами, учитывать
# их не следует.

from datetime import datetime
from functools import reduce, lru_cache

n = 10


@lru_cache(2 ** 5)
def factorial_self(number):
    """Возвращает факториал заданного числа"""
    return 1 if number ==0 else reduce(lambda x, y: x * y, range(1, number + 1))


def getpower(n, factorial_list):
    test, power = n - 1, 1
    while factorial_list[n - 1] * power > test:
        test = test * 10 + n - 1
        power += 1
    return power


def factorial_digit_sum(n, with_zeroes, without_zeroes):
    """Возвращет сумму списков факториалов"""
    result = 0
    while n >= 10_000:
        result += with_zeroes[n % 10_000]
        n //= 10_000
    return result + without_zeroes[n]

# 1 вариант
start_time = datetime.now()
factorial_list = [factorial_self(_) for _ in range(n)]
curious_numbers = []
for i in range(3, n ** getpower(n, factorial_list)):
    number_list = [int(i) for i in list(str(i))]
    sum_number_list = sum(factorial_list[i] for i in number_list)
    if sum_number_list > i: continue
    elif sum_number_list == i: curious_numbers.append(i)
else:
    print(sum(curious_numbers))
print(datetime.now() - start_time)

# 2 вариант
start_time = datetime.now()
factorial_list = [factorial_self(_) for _ in range(n)]
sum_fact_not_0 = [sum(factorial_self(int(c)) 
                      for c in str(i)) for i in range(10 ** 4)]
sum_fact_0 = [sum(factorial_self(int(c)) 
                  for c in str(i).zfill(4)) for i in range(10 ** 4)]
print(sum([i for i in range(3, 10 ** getpower(n, factorial_list)) 
          if i == factorial_digit_sum(i, sum_fact_0, sum_fact_not_0)]))
print(datetime.now() - start_time)

# Подсчитайте сумму всех дружественных чисел меньше 10000

from datetime import datetime
from euler12 import factors_long_time

n = 10_000


if __name__ == '__main__':
    # 1 вариант
    start_time = datetime.now()
    amicable_pairs = []
    for x in range(10, n):
        if x not in amicable_pairs:
            x_sum_divisors = sum(factors_long_time(x)[:-1])
            y_sum_divisors = sum(factors_long_time(x_sum_divisors)[:-1])
            if y_sum_divisors == x and x != x_sum_divisors:
                amicable_pairs.append(x)
                amicable_pairs.append(x_sum_divisors)
    print(sum(amicable_pairs))
    print(datetime.now() - start_time)

    # 2 вариант
    start_time = datetime.now()
    # Генерация сумм множителей, решетом Эратосфена
    divisorsum = [0] * n
    for i in range(1, n):
        for j in range(i * 2, n, i):
            divisorsum[j] += i

    # Поиск дружественных чисел и их суммирование
    sum_amic_pairs = 0
    for i in range(1, n):
        j = divisorsum[i]
        if j != i and j < n and divisorsum[j] == i:
            sum_amic_pairs += i
    print(sum_amic_pairs)
    print(datetime.now() - start_time)

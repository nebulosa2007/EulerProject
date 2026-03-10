# Каково первое треугольное число, у которого более пятисот делителей?

from datetime import datetime
from math import ceil, sqrt


def all_factors_list(number, justcount=False):
    """Возвращает список делителей заданного числа, либо количество делителей"""
    divisor, divisor_list = 2, [1, number]
    for i in range(2, ceil(sqrt(number)) + 1):
        if number % i == 0:
            if justcount:
                divisor += 2
            else: 
                divisor_list.append(i)
                divisor_list.append(number // i)
    if justcount:
        return divisor - 1 if ceil(sqrt(number)) ** 2 == number else divisor
    else:
        return divisor_list[:-1] if ceil(sqrt(number)) ** 2 == number else divisor_list


def figurate_number(number, base=None):
    """ Возвращает number-ое многоугольное число по заданной базе угольности"""
    assert base >= 3
    return int(((base - 2) * number ** 2 - (base - 4) * number) / 2)


def euler12():
    n = 500

    # 1 вариант
    start_time = datetime.now()
    i = 1
    while (divisors := all_factors_list(triangle := figurate_number(i, 3), justcount=True)) < n:
        i += 1
    print(f'{i}-th triangle number: {triangle} with {divisors} divisors')
    print(datetime.now() - start_time)

    # 2 вариант
    start_time = datetime.now()
    pass
    print(datetime.now() - start_time)


if __name__ == "__main__":
    euler12()

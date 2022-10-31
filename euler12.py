# Каково первое треугольное число, у которого более пятисот делителей?

from datetime import datetime
from math import ceil, sqrt


n = 500


def factors_long_time(number):
    divisor, divisor_list = 1, []
    while divisor <= number:
        if number % divisor == 0:
            divisor_list.append(divisor)
        divisor += 1
    return divisor_list


def exact_square(number):
    return True if ceil(sqrt(number)) ** 2 == number else False


def defactoring(number):
    """ Оптимальный алгоритм факторизации:
        1. Первоначальное количество делителей = 2
            (чтобы не перебирать 1 и само число)
        2. Делители рассматриваем в промежутке
            от 2 до квадратного корня числа.
        3. При нахождении делителя увеличиваем их
            количество на 2 (т.к делители всегда ходят парами)
        4. Если число представляет собой точный квадрат (имеет
        целый корень) уменьшаем результирующее количество делителей на 1.
    """
    natural_number, count_divisor = 2, 2
    while count_divisor < number:
        count_divisor = 2
        triangle_number = sum([c for c in range(1, natural_number + 1)])
        for i in range(2, ceil(sqrt(triangle_number))):
            if triangle_number % i == 0:
                count_divisor += 2
        if exact_square(triangle_number):
            count_divisor -= 1
        natural_number += 1
    return number if number == 1 or number == 2 else triangle_number


if __name__ == '__main__':
    # 1 вариант
    start_time = datetime.now()
    triangle_number, i = 1, 1
    factors_long_time_number = factors_long_time(triangle_number)
    if n <= 150:  # очень долгое решение полным перебором! Ограничитель
        while len(factors_long_time_number) < n:
            i += 1
            triangle_number += i
            factors_long_time_number = factors_long_time(triangle_number)
        print(triangle_number, ":",
              factors_long_time_number, "-",
              len(factors_long_time_number))
    print(datetime.now() - start_time)

    # 2 вариант
    start_time = datetime.now()
    triangle_number = defactoring(n)
    factors_long_time_number = factors_long_time(triangle_number)
    print(triangle_number, ":",
          factors_long_time_number, "-",
          len(factors_long_time_number))
    print(datetime.now() - start_time)

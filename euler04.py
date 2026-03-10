# Найдите самый большой палиндром,
# полученный умножением двух трехзначных чисел.

from datetime import datetime


def check_palindrom(number):
    """Проверка заданного числа на палиндром"""
    return True if number == number[::-1] else False


def euler04():
    n = 1_000

    # 1 Вариант
    start_time = datetime.now()
    pol = []
    for i in range(100, n):
        for j in range(100, n):
            if check_palindrom(str(i * j)): pol.append(i * j)
    print(max(pol))
    print(datetime.now() - start_time)

    # 2 Вариант
    start_time = datetime.now()
    print(max([i * j for i in range(100, n)
               for j in range(100, n)
               if check_palindrom(str(i * j))]))
    print(datetime.now() - start_time)


if __name__ == "__main__":
    euler04()

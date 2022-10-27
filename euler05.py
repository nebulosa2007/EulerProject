# Какое самое маленькое число делится нацело на все числа от 1 до 20?

from datetime import datetime

n = 20


def eratosfen(number):
    """Решето Эратосфена: генерация простых чисел
       вплоть до введённого числа
    """
    sieve = list(range(number + 1))
    sieve[1] = 0    # без этой строки итоговый список будет содержать единицу
    for i in sieve:
        if i > 1:
            for j in range(2 * i, len(sieve), i):
                sieve[j] = 0
    return sieve


def multiply(number):
    result = 1
    for k in eratosfen(number):
        if k == 0:
            continue
        i = 1
        while k ** (i + 1) < number:
            i += 1
        result *= k ** i
    return result


def eratosfen_lists(number):
    # Генерация списка простых чисел на списках
    result = 1
    for k in [x for x in range(2, number + 1) if x not in [i for sub in [list(range(2 * j, number + 1, j)) for j in range(2, number // 2)] for i in sub]]:
        i = 1
        while k ** (i + 1) < number:
            i += 1
        result *= k ** i
    return result


if __name__ == '__main__':
    # 1 Вариант
    start_time = datetime.now()
    print(multiply(n))
    print(datetime.now() - start_time)

    # 2 Вариант
    start_time = datetime.now()
    print(eratosfen_lists(n))
    print(datetime.now() - start_time)

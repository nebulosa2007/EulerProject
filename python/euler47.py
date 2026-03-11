# Найдите первые четыре последовательных числа, каждое из которых имеет четыре
# отличных друг от друга простых множителя. Каким будет первое число?

from datetime import datetime
from typing import List


def prime_factors_list(n: int) -> List[int]:
    """
    Возвращает список простых множителей заданного числа.

    Args:
        n: Число для факторизации.

    Returns:
        Список простых множителей.
    """
    divisor, nodarray = 2, []
    while divisor ** 2 <= n:
        if n % divisor == 0:
            n //= divisor
            nodarray.append(divisor)
        else:
            divisor += 1
    if n != 1:
        nodarray.append(n)
    return nodarray


def euler47() -> None:
    """
    Решение задачи Эйлера №47.

    Найдите первые четыре последовательных числа, каждое из которых имеет
    четыре различных простых множителя.
    """
    n = 4

    # 1 вариант
    start_time = datetime.now()
    i, counter = 1, 0
    while counter < n:
        i += 1
        if len(set(prime_factors_list(i))) == n:
            counter += 1
        else:
            counter = 0
    print(i - n + 1)
    print(datetime.now() - start_time)

    # 2 вариант
    start_time = datetime.now()
    siege = [0] * 150_000
    counter = 0
    result_i = 0
    for i in range(2, len(siege)):
        if siege[i] == n:
            counter += 1
            if counter == n:
                result_i = i
                break
        else:
            counter = 0
            if siege[i] == 0:
                siege[i::i] = [x + 1 for x in siege[i::i]]
    if result_i == 0:
        exit("Need to increase siege")
    print(result_i - n + 1)
    print(datetime.now() - start_time)


if __name__ == "__main__":
    euler47()

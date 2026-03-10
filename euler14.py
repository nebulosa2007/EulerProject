# Какой начальный элемент последовательности Коллатца меньше миллиона
# генерирует самую длинную последовательность?
# n → n/2 (n - четное)
# n → 3n + 1 (n - нечетное)

from datetime import datetime
from functools import lru_cache


@lru_cache(2 ** 20)
def collatz(number: int) -> int:
    """
    Возвращает следующее число Коллатца.

    Args:
        number: Текущее число последовательности.

    Returns:
        Следующее число Коллатца.
    """
    return int(number / 2) if number % 2 == 0 else number * 3 + 1


def collatz_recursion(number: int, counter: int) -> int:
    """
    Возвращает счётчик шагов в рекурсивном алгоритме Коллатца.

    Args:
        number: Текущее число.
        counter: Текущий счётчик шагов.

    Returns:
        Количество шагов до достижения 1.
    """
    if number == 1:
        return counter
    if number % 2 == 0:
        return collatz_recursion(int(number / 2), counter + 1)
    return collatz_recursion(3 * number + 1, counter + 1)


def euler14() -> None:
    """
    Решение задачи Эйлера №14.

    Какой начальный элемент последовательности Коллатца меньше миллиона
    генерирует самую длинную последовательность?
    """
    n = 1_000_000

    # 1 вариант
    start_time = datetime.now()
    max_counter, counter = 2, 2
    for number in range(3, n):
        x = number
        while x != 2:
            counter += 1
            x = collatz(x)
        if max_counter < counter:
            max_counter, winner = counter, number
        counter = 2
    print(f'{winner} : {max_counter}')
    print(datetime.now() - start_time)

    # 2 вариант
    start_time = datetime.now()
    counter = max_counter = winner = 0
    for i in range(13, n):
        counter = collatz_recursion(i, 1)
        if counter > max_counter:
            winner, max_counter = i, counter
    print(f'{winner} : {max_counter}')
    print(datetime.now() - start_time)

    # 3 вариант
    start_time = datetime.now()
    known_collatz = {key: 0 for key in range(1, n)}
    max_counter = winner = 0
    for number in range(1, n):
        temp, counter = number, 1
        while temp > 1:
            temp = collatz(temp)
            if temp in known_collatz and known_collatz[temp] != 0:
                counter += known_collatz[temp]
                break
            counter += 1
        known_collatz[number] = counter
        if counter > max_counter:
            max_counter, winner = counter, number
    print(f'{winner} : {max_counter}')
    print(datetime.now() - start_time)


if __name__ == "__main__":
    euler14()

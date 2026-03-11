# Найдите сумму всех чисел меньше миллиона, являющихся палиндромами
# по основаниям 10 и 2.

from datetime import datetime


def check_palindrom(number: str) -> bool:
    """
    Проверка заданного числа на палиндром.

    Args:
        number: Строковое представление числа.

    Returns:
        True если число является палиндромом, иначе False.
    """
    return number == number[::-1]


def euler36() -> None:
    """
    Решение задачи Эйлера №36.

    Найдите сумму всех чисел меньше миллиона, являющихся палиндромами
    по основаниям 10 и 2.
    """
    n = 1_000_000

    # 1 вариант
    start_time = datetime.now()
    sum_db_palindromes = 0
    for i in range(n):
        if check_palindrom(str(i)):
            if check_palindrom(str(bin(i)[2:])):
                sum_db_palindromes += i
    print(sum_db_palindromes)
    print(datetime.now() - start_time)

    # 2 вариант
    start_time = datetime.now()
    print(sum(
        x for x in range(n)
        if check_palindrom(str(x)) and check_palindrom(str(bin(x)[2:]))
    ))
    print(datetime.now() - start_time)


if __name__ == "__main__":
    euler36()

# Найдите сумму всех чисел, которые могут быть записаны в виде
# суммы пятых степеней их цифр.

from datetime import datetime


def sum_power_of_digits(x: int, n: int) -> int:
    """
    Возвращает сумму цифр в заданной степени.

    Args:
        x: Число для вычисления.
        n: Степень для возведения цифр.

    Returns:
        Сумма цифр числа в степени n.
    """
    return sum(int(z) ** n for z in str(x))


def euler30() -> None:
    """
    Решение задачи Эйлера №30.

    Найдите сумму всех чисел, которые могут быть записаны в виде
    суммы пятых степеней их цифр.
    """
    n = 5

    # 1 вариант
    start_time = datetime.now()
    num_list = []
    for x in range(2, n * 9 ** n):
        narciss_numbers = sum_power_of_digits(x, n)
        if narciss_numbers == x:
            num_list.append(x)
    print(sum(num_list))
    print(datetime.now() - start_time)

    # 2 вариант
    start_time = datetime.now()
    print(sum(
        i for i in range(2, n * 9 ** n)
        if sum_power_of_digits(i, n) == i
    ))
    print(datetime.now() - start_time)


if __name__ == "__main__":
    euler30()

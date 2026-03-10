# Найдите пару пятиугольных чисел Pj и Pk, для которых сумма и разность
# являются пятиугольными числами и значение D = |Pk − Pj| минимально,
# и дайте значение D в качестве ответа.

from datetime import datetime


def figurate_number(number: int, base: int = 3) -> int:
    """
    Возвращает number-ое многоугольное число по заданной базе угольности.

    Args:
        number: Порядковый номер числа.
        base: База угольности (3 = треугольные, 5 = пятиугольные и т.д.).

    Returns:
        Многоугольное число.
    """
    assert base >= 3
    return int(((base - 2) * number ** 2 - (base - 4) * number) / 2)


def isfigurate_number(test_number: int, base: int = 3) -> bool:
    """
    Проверяет является ли число многоугольным по заданной базе.

    Args:
        test_number: Число для проверки.
        base: База угольности.

    Returns:
        True если число является многоугольным, иначе False.
    """
    assert base >= 3
    r = (8 * (base - 2) * test_number + (base - 4) ** 2) ** 0.5
    return ((r + base - 4) / (2 * base - 4)) % 1 == 0


def euler44() -> None:
    """
    Решение задачи Эйлера №44.

    Найдите пару пятиугольных чисел с минимальной разностью.
    """
    # 1 вариант
    start_time = datetime.now()
    i, flag = 1, True
    while flag:
        i += 1
        next_pent = figurate_number(i, 5)
        for j in range(i - 1, 0, -1):
            prev_pent = figurate_number(j, 5)
            result = next_pent - prev_pent
            if (isfigurate_number(result, 5)
                    and isfigurate_number(prev_pent + next_pent, 5)):
                flag = False
                break
    print(result)
    print(datetime.now() - start_time)

    # 2 вариант
    start_time = datetime.now()
    pass
    print(datetime.now() - start_time)


if __name__ == "__main__":
    euler44()

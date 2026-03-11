# Можно убедиться в том, что T285 = P165 = H143 = 40755
# Найдите следующее треугольное число, являющееся также пятиугольным и
# шестиугольным

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


def euler45() -> None:
    """
    Решение задачи Эйлера №45.

    Найдите следующее треугольное число, являющееся также пятиугольным
    и шестиугольным.
    """
    n = 143

    # 1 вариант
    start_time = datetime.now()
    i = n + 1
    test_number = figurate_number(i, base=6)
    while not isfigurate_number(test_number, 5):
        i += 1
        test_number = figurate_number(i, base=6)
    print(figurate_number(i * 2 - 1, 3))
    print(datetime.now() - start_time)

    # 2 вариант
    start_time = datetime.now()
    pass
    print(datetime.now() - start_time)


if __name__ == "__main__":
    euler45()

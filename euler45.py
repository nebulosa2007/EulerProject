# Можно убедиться в том, что T285 = P165 = H143 = 40755
# Найдите следующее треугольное число, являющееся также пятиугольным и
# шестиугольным

from datetime import datetime


def figurate_number(number, base=None):
    """ Возвращает number-ое многоугольное число по заданной базе угольности"""
    assert base >= 3
    return int(((base - 2) * number ** 2 - (base - 4) * number) / 2)


def isfigurate_number(test_number, base=None):
    """ Проверяет является ли число многоугольным по заданной базе
    угольности"""
    assert base >= 3
    R = (8 * (base - 2) * test_number + (base - 4) ** 2) ** 0.5
    return ((R + base - 4) / (2 * base - 4)) % 1 == 0


def euler45():
    n = 143

    # 1 вариант
    start_time = datetime.now()
    test_number = figurate_number(i := n + 1, base=6)
    while not isfigurate_number(test_number, 5):
        test_number = figurate_number(i := i + 1, base=6)
    print(figurate_number(i * 2 - 1, 3))
    print(datetime.now() - start_time)

    # 2 вариант
    start_time = datetime.now()
    pass
    print(datetime.now() - start_time)


if __name__ == "__main__":
    euler45()

# Сколько воскресений выпадает на первое число месяца в двадцатом веке
# (с 1 января 1901 года до 31 декабря 2000 года)?

from datetime import datetime
from calendar import monthrange


def isleap_year(year: int) -> bool:
    """
    Проверяет високосный ли год.

    Args:
        year: Год для проверки.

    Returns:
        True если год високосный, иначе False.
    """
    return year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)


def counter_prime_weekday(year: int, weeknum: int) -> int:
    """
    Возвращает количество совпадений заданного дня недели с 1 числом месяца.

    Args:
        year: Конечный год периода (с 1900).
        weeknum: Номер дня недели (1-7).

    Returns:
        Количество совпадений.
    """
    assert year >= 1900 and 1 <= weeknum <= 7
    month30 = [4, 6, 9, 11]
    febrary = {'standard': 28, 'leap': 29}
    days_month, sum_days = [], []
    for y in range(1900, year + 1):
        year_type = 'leap' if isleap_year(y) else 'standard'
        for month in range(1, 13):
            if month in month30:
                days_month.append(30)
            elif month == 2:
                days_month.append(febrary[year_type])
            else:
                days_month.append(31)
        sum_days += days_month
        days_month = []
    alldays = counter_prime = 0
    for x in sum_days:
        alldays += x
        if (alldays + 1) % weeknum == 0:
            counter_prime += 1
    return counter_prime


def euler19() -> None:
    """
    Решение задачи Эйлера №19.

    Сколько воскресений выпадает на первое число месяца в двадцатом веке?
    """
    n = 2000

    # 1 вариант
    start_time = datetime.now()
    print(counter_prime_weekday(n, 7) - counter_prime_weekday(1900, 7))
    print(datetime.now() - start_time)

    # 2 вариант
    start_time = datetime.now()
    counter_prime = 0
    for year in range(1901, n + 1):
        for month in range(1, 13):
            if monthrange(year, month)[0] == 6:
                counter_prime += 1
    print(counter_prime)
    print(datetime.now() - start_time)


if __name__ == "__main__":
    euler19()

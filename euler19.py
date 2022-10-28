# Сколько воскресений выпадает на первое число месяца в
# двадцатом веке (с 1 января 1901 года до 31 декабря 2000 года)?

from datetime import datetime
from calendar import monthrange

n = 2000


def leap_year(year):
    # Проверяет високосный ли год
    if year % 100 == 0:
        return True if year % 400 == 0 else False
    return True if year % 4 == 0 else False


def counter_prime_weekday(year, weeknum):
    # Генерирует список количества дней в месяце, с 1900 года вплоть до year
    # затем считает совпадения заданного дня недели с 1 днём месяца
    assert year >= 1900 and weeknum >= 1 and weeknum <= 7
    month30 = [4, 6, 9, 11]
    febrary = {'standard': 28, 'leap': 29}
    days_month = []
    sum_days = []
    for year in range(1900, year + 1):
        year_type = 'leap' if leap_year(year) else 'standard'
        for month in range(1, 13):
            if month in month30 and n != 2:
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
        counter_prime += 1 if (alldays + 1) % weeknum == 0 else 0
    return counter_prime


if __name__ == '__main__':
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

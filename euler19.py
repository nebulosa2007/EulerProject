# Сколько воскресений выпадает на первое число месяца в
# двадцатом веке (с 1 января 1901 года до 31 декабря 2000 года)?

from project_euler_defs import *

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

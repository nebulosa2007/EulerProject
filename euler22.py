# Начните с сортировки в алфавитном порядке. Затем подсчитайте алфавитные
# значения каждого имени и умножьте это значение на порядковый номер имени
# в отсортированном списке для получения количества очков имени.
# Какова сумма очков имен в файле?

from datetime import datetime
from requests import get
from euler11 import readmatrix

n = "https://projecteuler.net/project/resources/p022_names.txt"


def names_points(*names):
    return sum(sum(ord(j) - 64
                   for j in list(names[i])) * (i + 1)
               for i in range(len(names)))


if __name__ == '__main__':
    # 1 вариант
    start_time = datetime.now()
    print(names_points(*sorted(readmatrix("euler22.txt", mode='text'))))
    print(datetime.now() - start_time)

    # 2 вариант
    start_time = datetime.now()
    response = get(n, timeout=3)
    if response.status_code != 200:
        exit()
    names = sorted(response.content.decode().replace('"', '').split(','))
    print(names_points(*names))
    print(datetime.now() - start_time)

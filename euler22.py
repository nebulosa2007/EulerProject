# Начните с сортировки в алфавитном порядке. Затем подсчитайте алфавитные
# значения каждого имени и умножьте это значение на порядковый номер имени
# в отсортированном списке для получения количества очков имени.
# Какова сумма очков имен в файле?

from datetime import datetime
from requests import get

n = "https://projecteuler.net/project/resources/p022_names.txt"


def readmatrix(namefile=None, text=None, mode=None):
    """Возвращает матрицу чисел или слов из файла или переданного текста"""
    matrix = []
    if text is not None:
        for line in range(len(text)):
            matrix.append([int(i) for i in text[line].split(" ")])
    elif mode is None:
        with open(namefile) as f:
            for line in f:
                matrix.append([int(i) for i in line.rstrip('\n').split()])
    elif mode == 'text':
        with open(namefile) as f:
            for line in f:
                matrix = line.replace('"', '').split(',')
    return matrix


def names_points(*names):
    """Возвращает сумму очков отсортированных имен"""
    return sum(sum(ord(j) - 64
                   for j in list(names[i])) * (i + 1)
               for i in range(len(names)))

# 1 вариант
start_time = datetime.now()
print(names_points(*sorted(readmatrix("euler22.txt", mode='text'))))
print(datetime.now() - start_time)

# 2 вариант
start_time = datetime.now()
if (response := get(n, timeout=3)).status_code != 200: exit()
names = sorted(response.content.decode().replace('"', '').split(','))
print(names_points(*names))
print(datetime.now() - start_time)

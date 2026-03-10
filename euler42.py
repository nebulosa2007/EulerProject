# n-й член последовательности треугольных чисел задается как tn = ½n(n+1)
# Используя euler42.txt определите, сколько в нем треугольных слов,
# преобразовывая каждую букву в число, соответствующее ее порядковому номеру
# в алфавите и складывая эти значения

from datetime import datetime
from requests import get


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


def euler42():
    n = "https://projecteuler.net/project/resources/p042_words.txt"

    # 1 вариант
    start_time = datetime.now()
    print(len([_ for _ in readmatrix("euler42.txt", mode='text')
               if isfigurate_number(sum(ord(x) - 64 for x in _), 3)]))
    print(datetime.now() - start_time)

    # 2 вариант
    start_time = datetime.now() 
    if (response := get(n, timeout=3)).status_code != 200:
        exit()
    words = response.content.decode().replace('"', '').split(',')
    max_n = 0
    for x in words:
        max_n = max(sum(ord(_) - 64 for _ in x), max_n)
    else:
        triangle_numbers = [figurate_number(_, 3) for _ in range(1, max_n + 1)]
    print(len([_ for _ in words
               if sum(ord(x) - 64 for x in _) in triangle_numbers]))
    print(datetime.now() - start_time)


if __name__ == "__main__":
    euler42()

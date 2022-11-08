# Найдите наибольшее произведение тринадцати последовательных цифр в
# данном 1000-значном числе.

from functools import reduce
from datetime import datetime
from math import prod
from bs4 import BeautifulSoup as bs
from requests import get

n = 13


def get_data(url, tag, n):
    return bs(get(url).text, 'lxml').find_all(tag)[n].text


def multiply_numbers(*numset):
    # перемножает все числа в выборке
    return reduce((lambda x, y: int(x) * int(y)), numset)


def loadfiletolist(namefile):
    # Чтение длинного числа
    number = []
    with open(namefile) as f:
        while True:
            c = f.read(1)
            if c == '':
                break
            else:
                if c != '\n':
                    number.append(c)
    return number


if __name__ == '__main__':
    # 1 Вариант
    number = loadfiletolist('euler08.txt')
    all_prod = []

    start_time = datetime.now()
    for i in range(len(number) - n):
        numset = number[i:i + n]
        if len(numset) >= n or '0' not in numset:
            all_prod.append(multiply_numbers(*numset))
    print(max(all_prod))
    print(datetime.now() - start_time)

    # 2 Вариант
    start_time = datetime.now()
    print(max(prod(map(int, number[i:i + n])) for i in range(len(number) - n)))
    print(datetime.now() - start_time)

    # 3 Вариант
    start_time = datetime.now()
    url = 'https://euler.jakumo.org/problems/view/8.html'
    text = list(get_data(url, 'p', 1).replace('\n', ''))
    print(max(prod(map(int, text[i:i + n])) for i in range(len(text) - n)))
    print(datetime.now() - start_time)

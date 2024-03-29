from datetime import datetime
from itertools import takewhile, islice, count, permutations
from functools import reduce, lru_cache
from re import fullmatch
from math import prod, ceil, sqrt, factorial, gcd
from numpy import array
from bs4 import BeautifulSoup as bs
from requests import get
from calendar import monthrange
from re import findall

# problem 02
def fibonacci(f1=0, f2=1):
    """Итерируемая функция вычисления следующего числа Фибоначчи"""
    while True:
        yield f1
        f1, f2 = f2, f1 + f2


# problem 03
def isPrime_reg(n):
    """Проверка числа на простоту через регулярные выражения"""
    return not bool(fullmatch(r'(11+?)\1+', '1' * n))


@lru_cache(2 ** 5)
def isprime(number: int):
    """Проверка числа на простоту перебором делителей"""
    if number in {2, 3, 5, 7}: return True
    if number < 2 or number % 2 == 0: return False
    if number % 3 == 0 or number % 5 == 0: return False
    a, k = number, 0
    for i in range(5, int(number**0.5), 6):
        k += 1 if a % i == 0 or a % (i + 2) == 0 else 0
    return True if k <= 0 else False


def prime_factors_list(n):
    """Возвращет список простых множителей заданного числа"""
    divisor, nodarray = 2, []
    while divisor ** 2 <= n:
        if n % divisor == 0:
            n //= divisor
            nodarray.append(divisor)
        else: divisor += 1
    if n != 1: nodarray.append(n)
    return nodarray


# problem 04
def check_palindrom(number):
    """Проверка заданного числа на палиндром"""
    return True if number == number[::-1] else False


# problem 05
def eratosfen(number):
    """Решето Эратосфена: генерация простых чисел вплоть до заданного числа"""
    sieve = list(range(number + 1))
    sieve[1] = 0
    for i in sieve:
        if i > 1:
            for j in range(2 * i, len(sieve), i):
                sieve[j] = 0
    return sieve


def eratosfen_lists(number, dimension=None):
    """Решето Эратосфена: генерация списка простых чисел на списках
    до заданного числа"""
    start = 1 if dimension is None else dimension
    sieve = []
    for k in [x for x in range(10 ** (start - 1) + 1, number + 1)
              if x not in [i for sub in [list(range(2 * j, number + 1, j))
                                         for j in range(2, number // 2)]
                           for i in sub]]:
        sieve.append(k)
    return sieve


# problem 07
def primes(dimension=None):
    """Итерируемая функция генерация простых чисел"""
    start = 2 if dimension is None else 10 ** (dimension - 1) + 1
    ints = count(start)
    while True:
        p = next(ints)
        yield p
        ints = filter(p.__rmod__, ints)


# problem 08
def get_data(url, tag, n):
    """Возвращает чистый текст по n-ному заданному тегу и url"""
    return bs(get(url, timeout=3).text, 'lxml').find_all(tag)[n].text


def multiply_numbers(*numset):
    """Возвращет произведение чисел в заданной выборке"""
    return reduce((lambda x, y: int(x) * int(y)), numset)


def loadfiletolistnumbers(namefile):
    """Возвращает список из чисел заданного файла"""
    number = []
    with open(namefile) as f:
        while True:
            if (c := f.read(1)) == '': break
            elif c != '\n': number.append(c)
    return number


# problem 11
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


def product_multiply(matrix, n):
    """Возвращает список произведений n элементов в строках матрицы"""
    product = []
    for i in range(len(matrix[0]) - n + 1):
        for j in range(len(matrix)):
            num = 1
            for k in range(n):
                num *= matrix[j][i + k]
            product.append(num)
    return(product)


def product_multiply_diagonals(matrix, n):
    """Перемножает по n элементов матрицы по диагоналям и
    возвращает максимальное произведение (экономим память)"""
    max_product = 0
    for x in range(len(matrix[0]) - n + 1):
        for y in range(len(matrix[0]) - n + 1):
            # по диагонали вправо вниз
            num = 1
            for i in range(n):
                num *= int(matrix[x + i][y + i])
            if num > max_product: max_product = num

            # по диагонали вправо вверх
            num = 1
            for i in range(n):
                num *= int(matrix[x - i][y + i])
            if num > max_product: max_product = num

            # по диагонали влево вниз
            num = 1
            for i in range(n):
                num *= int(matrix[x + i][y - i])
            if num > max_product: max_product = num

            # по диагонали влево вверх
            num = 1
            for i in range(n):
                num *= int(matrix[x - i][y - i])
            if num > max_product: max_product = num
    return max_product


# problem 12
def all_factors_list(number, justcount=False):
    """Возвращает список делителей заданного числа, либо количество делителей
        Оптимальный алгоритм факторизации:
        1. Первоначальное количество делителей = 2
            (чтобы не перебирать 1 и само число)
        2. Делители рассматриваем в промежутке
            от 2 до квадратного корня числа.
        3. При нахождении делителя увеличиваем их
            количество на 2 (т.к делители всегда ходят парами)
        4. Если число представляет собой точный квадрат (имеет
        целый корень) уменьшаем результирующее количество делителей на 1.
    """
    divisor, divisor_list = 2, [1, number]
    for i in range(2, ceil(sqrt(number)) + 1):
        if number % i == 0:
            if justcount:
                divisor += 2
            else: 
                divisor_list.append(i)
                divisor_list.append(number // i)
    if justcount:
        return divisor - 1 if ceil(sqrt(number)) ** 2 == number else divisor
    else:
        return divisor_list[:-1] if ceil(sqrt(number)) ** 2 == number else divisor_list


def figurate_number(number, base=None):
    """ Возвращает number-ое многоугольное число по заданной базе угольности"""
    assert base >= 3
    return int(((base - 2) * number ** 2 - (base - 4) * number) / 2)


# problem 14
@lru_cache(2 ** 20)
def collatz(number: int):
    """Возвращает следующее число Коллатца"""
    return int(number / 2) if number % 2 == 0 else number * 3 + 1


def collatz_recursion(number, counter):
    """Возвращает счётчик шагов итого в рекурсивном алгоритме Коллатца"""
    if number == 1: return counter
    if number % 2 == 0: return collatz_recursion(int(number / 2), counter + 1)
    else: return collatz_recursion(3 * number + 1, counter + 1)


# problem 15
memory = {(1, 0): 1, (0, 1): 1}


@lru_cache(2 ** 20)
def func(x, y):
    """Возвращает словарь/матрицу весов путей"""
    if (x, y) not in memory:
        if x == 0: memory[(x, y)] = func(x, y - 1)
        elif y == 0: memory[(x, y)] = func(x - 1, y)
        else: memory[(x, y)] = func(x - 1, y) + func(x, y - 1)
    return memory[(x, y)]


# problem 17
def numerals(number):
    """Возвращет заданное число прописью"""
    assert number < 1_000_000
    numerals_number = []
    numbers = {1: 'one', 2: 'two', 3: 'three', 4: 'four',
               5: 'five', 6: 'six', 7: 'seven', 8: 'eight',
               9: 'nine', 10: 'ten', 11: 'eleven', 12: 'twelve',
               13: 'thirteen', 14: 'fourteen', 15: 'fifteen',
               16: 'sixteen', 17: 'seventeen', 18: 'eighteen',
               19: 'nineteen', 20: 'twenty', 30: 'thirty', 40: 'forty',
               50: 'fifty', 60: 'sixty', 70: 'seventy', 80: 'eighty',
               90: 'ninety', 100: "hundred", 1_000: "thousand"}
    morethanhundred = False
    for x in [1000, 100]:
        if number >= x:
            numerals_number.append(numbers[number // x])
            numerals_number.append(numbers[x])
            number = number - number // x * x
            morethanhundred = True
    if morethanhundred and number > 0:
        numerals_number.append('and')
    if number >= 20:
        numerals_number.append(numbers[number // 10 * 10])
        number = number - number // 10 * 10
    if number in numbers:
        numerals_number.append(numbers[number])
    return numerals_number


# problem 18
def msu(rows, n_line):
    """Возвращает максимальную сумму пути по треугольнику"""
    for i in range(len(rows[n_line])):
        rows[n_line][i] += max([rows[n_line + 1][i],
                                rows[n_line + 1][i + 1]])
    return rows[n_line][0] if len(rows[n_line]) == 1 else msu(rows, n_line - 1)


# problem 19
def isleap_year(year):
    """Проверяет високосный ли год"""
    return year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)


def counter_prime_weekday(year, weeknum):
    """Возвращает список количества дней в месяце, c 1900 года вплоть до year
    затем считает совпадения заданного дня недели c 1 днём месяца"""
    assert year >= 1900 and weeknum >= 1 and weeknum <= 7
    month30 = [4, 6, 9, 11]
    febrary = {'standard': 28, 'leap': 29}
    days_month,  sum_days = [], []
    for year in range(1900, year + 1):
        year_type = 'leap' if isleap_year(year) else 'standard'
        for month in range(1, 13):
            if month in month30: days_month.append(30)
            elif month == 2: days_month.append(febrary[year_type])
            else: days_month.append(31)
        sum_days += days_month
        days_month = []
    alldays = counter_prime = 0
    for x in sum_days:
        alldays += x
        counter_prime += 1 if (alldays + 1) % weeknum == 0 else 0
    return counter_prime


# problem 20
@lru_cache(2 ** 5)
def factorial_self(number):
    """Возвращает факториал заданного числа"""
    return 1 if number ==0 else reduce(lambda x, y: x * y, range(1, number + 1))


# problem 22
def names_points(*names):
    """Возвращает сумму очков отсортированных имен"""
    return sum(sum(ord(j) - 64
                   for j in list(names[i])) * (i + 1)
               for i in range(len(names)))


# problem 26
def repeat_inside(text):
    """Возвращает повторяющуюся подстроку через регулярные выражения"""
    match = findall(r'(?=((.+?)\2+))', text)
    return max((x[1] for x in match), key=len, default='')


# problem 30
def sum_power_of_digits(x, n):
    """Возвращает сумму цифр в заданной степени"""
    return sum(int(z) ** n for z in list(str(x)))


# problem 31
def num_sets(n, coins):
    """Возвращает количество вариантов расстановки суммы n,
    через список слагаемых coins"""
    if n < 0: return 0
    if n == 0: return 1
    if len(coins) == 1: return n % coins[0] == 0
    return num_sets(n - coins[0], coins) + num_sets(n, coins[1:])

# problem 32
def sqrt(x):
    """Возвращает максимально близкое число к корню от x"""
    assert x >= 0
    i = 1
    while i * i <= x:
        i *= 2
    y = 0
    while i > 0:
        if (y + i) ** 2 <= x: y += i
        i //= 2
    return y


def ispandigital_product(n):
    """Проверяет произведение на пан-цифры"""
    for i in range(1, sqrt(n) + 1):
        if n % i == 0:
            temp = str(n) + str(i) + str(n // i)
            if "".join(sorted(temp)) == "123456789":
                return True
    return False


# problem 34
def getpower(n, factorial_list):
    test, power = n - 1, 1
    while factorial_list[n - 1] * power > test:
        test = test * 10 + n - 1
        power += 1
    return power


def factorial_digit_sum(n, with_zeroes, without_zeroes):
    """Возвращет сумму списков факториалов"""
    result = 0
    while n >= 10_000:
        result += with_zeroes[n % 10_000]
        n //= 10_000
    return result + without_zeroes[n]


# problem 37
def del_digit_left_or_right(number):
    """Возвращает поочередно часть числа либо без правой,
    либо без левой цифры"""
    yield number
    number_str = str(number)
    for k in range(1, len(number_str)):
        yield int(number_str[k:])
        yield int(number_str[:-k])


# problem 44
def isfigurate_number(test_number, base=None):
    """ Проверяет является ли число многоугольным по заданной базе
    угольности"""
    assert base >= 3
    R = (8 * (base - 2) * test_number + (base - 4) ** 2) ** 0.5
    return ((R + base - 4) / (2 * base - 4)) % 1 == 0


# problem 49
def twelve_digit(pan_primes_check):
    for i in range(len(pan_primes_check)):
        for j in range(i + 1, len(pan_primes_check)):
            delta = pan_primes_check[j] - pan_primes_check[i]
            if pan_primes_check[j] + delta in pan_primes_check:
                return (str(pan_primes_check[i]) + str(pan_primes_check[j])
                        + str(pan_primes_check[j] + delta))
    return False

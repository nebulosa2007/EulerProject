# Найдите первые десять цифр суммы следующих ста 50-значных чисел.
# Ответ: 5537376230

from datetime import datetime

n = 100


def count_lines_in_file(filename, chunk_size=1 << 13):
    """ Определяет количество строк в файле.
        Возможно есть более лучшая реализация
    """
    with open(filename) as file:
        return sum(chunk.count('\n')
                   for chunk in iter(lambda: file.read(chunk_size), ''))


def loadfiletolist(filename, n=None):
    """ Загружает в список n раз данные построчно.
        Если n больше чем строк в файле - возвращает в списке все
        строки файла
    """
    n = None if isinstance(n, int) and count_lines_in_file(filename) < n else n
    with open(filename) as f:
        return [row.rstrip('\n')
            for row in f] if n is None \
            else [next(f).rstrip('\n') for x in range(n)]


def sum_long_number(long_number):
    max_key = max(x for x in long_number)
    max_lenght = max_key + len(str(long_number[max_key]))
    long_num = [0 for x in range(max_lenght + 1)]
    for i in range(max_lenght):
        for j in list(str(long_number[i])):
            for k in range(len(j)):
                long_num[max_lenght - k] = j[k] # !!! доделать сложение посимвольное
    print(long_num)
    return None


if __name__ == '__main__':
    # 1 вариант
    start_time = datetime.now()
    numbers = loadfiletolist("euler13.txt", n)
    sum_vertical, total, column_numbers = 0, 0, []
    for j in range(1, len(numbers[0]) + 1):
        for i in range(len(numbers)):
            sum_vertical += int(numbers[i][j * -1])
        total += sum_vertical * (10 ** (j - 1))  # хак ограниченный по ресам
        sum_vertical, column_numbers = 0, []
    print(str(total)[0:10])
    print(datetime.now() - start_time)

    # 2 вариант - todo, формирование числа через строку
    start_time = datetime.now()
    long_number = {}  # Скорее всего нужно использовать кортежи (сумма, смещение)
    for j in range(1, len(numbers[0]) + 1):
        for i in range(len(numbers)):
            column_numbers.append(int(numbers[i][j * -1]))
        long_number[j - 1] = sum(column_numbers)
    print(long_number)
    #print(sum_long_number(long_number))
    print(datetime.now() - start_time)

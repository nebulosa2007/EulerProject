# Найдите первые десять цифр суммы следующих ста 50-значных чисел.
# Ответ: 5537376230

from project_euler_defs import *

n = 10

# 1 вариант
start_time = datetime.now()
numbers = readmatrix("euler13.txt")
sum_vertical, total, column_numbers = 0, 0, []
for j in range(1, len(numbers[0]) + 1):
    for i in range(len(numbers)):
        sum_vertical += numbers[i][j * -1]
    total += sum_vertical * (10 ** (j - 1))
    sum_vertical, column_numbers = 0, []
print(str(total)[0:10])
print(len(str(total)), "", total)
print(datetime.now() - start_time)


def sum_long_number(long_number, digit):
    """Посимвольное сложение - todo!! """
    '''max_key = max(x for x in long_number)
    print(max_key)
    max_lenght = max_key + len(str(long_number[max_key]))
    print(max_lenght)
    long_num = [0 for x in range(max_lenght + 1)]
    for i in range(max_lenght):
        for j in list(str(long_number[i])):
            for k in range(len(j)):
                long_num[max_lenght - k] = j[k]  # доделать сложение символьное
    '''
    return None


# 2 вариант - todo, формирование числа через строку
start_time = datetime.now()
# url = 'https://euler.jakumo.org/problems/view/13.html'
# numbers = get_data(url, 'div', 9).strip().split("\n")
numbers = [str(_) for _ in sum(numbers, [])]
column_numbers, long_number = [], {}
for j in range(1, len(numbers[0]) + 1):
    for i in range(len(numbers)):
        column_numbers.append(int(numbers[i][j * -1]))
    long_number[j - 1] = sum(column_numbers)
    # column_numbers = []
print(long_number)
print(sum_long_number(long_number, 10))
print(datetime.now() - start_time)

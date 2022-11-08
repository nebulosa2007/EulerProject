# Найдите первые десять цифр суммы следующих ста 50-значных чисел.
# Ответ: 5537376230

from project_euler_defs import *

n = 100

# 1 вариант
start_time = datetime.now()
numbers = readmatrix("euler13.txt")
sum_vertical, total, column_numbers = 0, 0, []
for j in range(1, len(numbers[0]) + 1):
    for i in range(len(numbers)):
        sum_vertical += int(numbers[i][j * -1])
    total += sum_vertical * (10 ** (j - 1)) 
    sum_vertical, column_numbers = 0, []
print(str(total)[0:10])
print(datetime.now() - start_time)

# 2 вариант - todo, формирование числа через строку
start_time = datetime.now()
long_number = {}  # Нужно использовать кортежи (сумма, смещение)
url = 'https://euler.jakumo.org/problems/view/13.html'
numbers = get_data(url, 'div', 9).strip().split("\n")
for j in range(1, len(numbers[0]) + 1):
    for i in range(len(numbers)):
        column_numbers.append(int(numbers[i][j * -1]))
    long_number[j - 1] = sum(column_numbers)
print(long_number)
# print(sum_long_number(long_number))
print(datetime.now() - start_time)

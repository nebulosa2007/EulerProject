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
print(datetime.now() - start_time)

# 2 вариант
start_time = datetime.now()
url = 'https://euler.jakumo.org/problems/view/13.html'
numbers = get_data(url, 'div', 9).strip().split("\n")
column_numbers, long_number = [], {}
for j in range(1, len(numbers[0]) + 1):
    for i in range(len(numbers)):
        column_numbers.append(int(numbers[i][j * -1]))
    long_number[len(numbers[0]) - j] = sum(column_numbers)
    column_numbers = []
max_lenght = j - 1 + len(str(long_number[j - 1]))
total_num = [0 for x in range(max_lenght)]
for i in long_number.keys():
    for k, j in enumerate(list(str(long_number[i]))):
        total_num[i + k] += int(j)
        if total_num[i + k] > 9:
            total_num[i + k - 1] += total_num[i + k] // 10
            total_num[i + k] %= 10
else:
    print(''.join(str(_) for _ in total_num)[:10])
print(datetime.now() - start_time)

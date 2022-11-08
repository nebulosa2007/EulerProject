# Найдите наибольшее произведение тринадцати последовательных цифр в
# данном 1000-значном числе.

from project_euler_defs import *

n = 13

# 1 Вариант
number = loadfiletolistnumbers('euler08.txt')
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

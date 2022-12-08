# Найдите сумму всех чисел, которые могут быть записаны в виде
# суммы пятых степеней их цифр.

from project_euler_defs import *

n = 5  # n > 1

# 1 вариант
start_time = datetime.now()
num_list = []
for x in range(2, n * 9 ** n):
    narciss_numbers = sum_power_of_digits(x, n)
    if narciss_numbers == x: num_list.append(x)
print(sum(num_list))
print(datetime.now() - start_time)

# 2 вариант
start_time = datetime.now()
print(sum(i for i in range(2, n * 9 ** n)
          if sum_power_of_digits(i, n) == i))
print(datetime.now() - start_time)

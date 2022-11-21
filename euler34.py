# 145 является любопытным числом, поскольку 1! + 4! + 5! = 1 + 24 + 120 = 145.
# Найдите сумму всех чисел, каждое из которых равно сумме факториалов своих
# цифр. Примечание: поскольку 1! = 1 и 2! = 2 не являются суммами, учитывать
# их не следует.

from project_euler_defs import *

n = 10

# 1 вариант
start_time = datetime.now()
factorial_list = [factorial_self(i) for i in range(10)]

test, power = 9, 1
while factorial_list[9] * power > test:
    test = test * 10 + 9
    power += 1

curious_numbers = []
for i in range(3, n ** power):
    number_list = [int(i) for i in list(str(i))]
    sum_number_list = sum(factorial_list[i] for i in number_list)
    if sum_number_list > i:
        continue
    elif sum_number_list == i:
        curious_numbers.append(i)
else:
    print(sum(curious_numbers))
print(datetime.now() - start_time)

# 2 вариант
start_time = datetime.now()


def factorial_digit_sum(n):
    result = 0
    while n >= 10000:
        result += FACTORIAL_DIGITS_SUM_WITH_LEADING_ZEROS[n % 10000]
        n //= 10000
    return result + FACTORIAL_DIGITS_SUM_WITHOUT_LEADING_ZEROS[n]


FACTORIAL_DIGITS_SUM_WITHOUT_LEADING_ZEROS = [sum(factorial_self(int(c)) for c in str(i)) for i in range(10000)]
FACTORIAL_DIGITS_SUM_WITH_LEADING_ZEROS = [sum(factorial_self(int(c)) for c in str(i).zfill(4)) for i in range(10000)]

print(sum([i for i in range(3, 10 ** power) if i == factorial_digit_sum(i)]))
print(datetime.now() - start_time)

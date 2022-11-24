# Какое самое большое девятизначное пан-цифровое число можно образовать
# как объединенное произведение целого числа и (1,2, ... , n), где n > 1?

from project_euler_defs import *

n = 10

# 1 вариант
start_time = datetime.now()
pan_digits = []
template = [str(_) for _ in range(1, n)]
for y in range(n * 1000):
    pan_digit_check, x = str(y), 2
    while len(pan_digit_check + str(y * x)) < n:
        pan_digit_check += str(y * x)
        x += 1
    if sorted(pan_digit_check) == template:
        pan_digits.append(pan_digit_check)
print(max(pan_digits))
print(datetime.now() - start_time)

# 2 вариант
start_time = datetime.now()
pass
print(datetime.now() - start_time)

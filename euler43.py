# Найдите сумму всех пан-цифровых чисел из цифр от 0 до 9,
# обладающих данным свойством.

from project_euler_defs import *

n = 10

# 1 вариант
start_time = datetime.now()
pan_numbers = list(permutations([_ for _ in range(n)], n))
pan_numbers_sub, divisors = [], eratosfen_lists(18)
for i in pan_numbers:
    if i[0] != 0:
        check_pan_number = [100 * i[y] + 10 * i[y + 1] + i[y + 2]
                            for y in range(1, len(i) - 2)]
        if all([check_pan_number[z] % divisors[z] == 0
                for z in range(len(check_pan_number))]):
            pan_numbers_sub.append(int(''.join(str(_) for _ in i)))
else:
    print(sum(pan_numbers_sub))
print(datetime.now() - start_time)

# 2 вариант
start_time = datetime.now()
pass
print(datetime.now() - start_time)

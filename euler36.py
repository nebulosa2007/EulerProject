# Найдите сумму всех чисел меньше миллиона, являющихся палиндромами
# по основаниям 10 и 2.

from project_euler_defs import *

n = 1_000_000

# 1 вариант
start_time = datetime.now()
sum_db_palindromes = 0
for i in range(n):
    if check_palindrom(str(i)):
        if check_palindrom(str(bin(i)[2:])):
            sum_db_palindromes += i
else:
    print(sum_db_palindromes)
print(datetime.now() - start_time)

# 2 вариант
start_time = datetime.now()
print(sum([_ for _ in range(n)
           if check_palindrom(str(_)) and check_palindrom(str(bin(_)[2:]))]))
print(datetime.now() - start_time)

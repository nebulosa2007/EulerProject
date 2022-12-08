# Существует ровно 4 нетривиальных примера дробей подобного типа, которые
# меньше единицы и содержат двухзначные числа как в числителе, так и в
# знаменателе. Пусть произведение этих четырех дробей дано в виде несократимой
# дроби (числитель и знаменатель дроби не имеют общих сомножителей).
# Найдите знаменатель этой дроби.

from project_euler_defs import *

n = 100

# 1 вариант
start_time = datetime.now()
denominator_product, nominator_product = 1, 1
for denominator in range(10, n):
    for nominator in range(10, denominator):
        if nominator % 10 == 0 and denominator % 10 == 0: continue
        nominator_list = list(str(nominator))
        denominator_list = list(str(denominator))
        common = set(nominator_list[0] if nominator_list in denominator_list
                     else nominator_list[1]
                     if nominator_list[1] in denominator_list else [])
        if common != set():
            nominator_list = set(nominator_list[0]) if (x := set(nominator_list) - common) == set() else x
            denominator_list = set(denominator_list[0]) if (y := set(denominator_list) - common) == set() else y
            if denominator_list == {'0'}: continue
            if nominator / denominator == int(nominator_list.pop()) / int(denominator_list.pop()):
                nominator_product *= nominator
                denominator_product *= denominator
else:
    print(denominator_product // gcd(nominator_product, denominator_product))
print(datetime.now() - start_time)

# 2 вариант
start_time = datetime.now()
numer, denom = 1, 1
for d in range(10, n):
    for n in range(10, d):
        n0, n1, d0, d1 = n % 10, n // 10, d % 10, d // 10
        if (n1 == d0 and n0 * d == n * d1) or (n0 == d1 and n1 * d == n * d0):
            numer *= n
            denom *= d
print(str(denom // gcd(numer, denom)))
print(datetime.now() - start_time)

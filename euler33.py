# Существует ровно 4 нетривиальных примера дробей подобного типа, которые
# меньше единицы и содержат двухзначные числа как в числителе, так и в
# знаменателе. Пусть произведение этих четырех дробей дано в виде несократимой
# дроби (числитель и знаменатель дроби не имеют общих сомножителей).
# Найдите знаменатель этой дроби.

from project_euler_defs import *

n = 100

# 1 вариант
start_time = datetime.now()
fraction_list = []
nominator = 49
denominator = 98
# for nominator in range(10, n):
#    for denominator in range(10, n):
nominator_list = set(list(str(nominator)))
denominator_list = set(list(str(denominator)))
common = nominator_list & denominator_list
nominator_list = nominator_list - common
denominator_list = denominator_list - common
fraction1 = nominator / denominator
a = int(nominator_list.pop())
b = int(denominator_list.pop())
fraction2 =  a / b
if fraction1 == fraction2:
    fraction_list.append([a, b])
# if nominator / denominator_list
print(fraction_list)
print(datetime.now() - start_time)

# 2 вариант
start_time = datetime.now()
pass
print(datetime.now() - start_time)

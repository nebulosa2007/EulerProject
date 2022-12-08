# n-й член последовательности треугольных чисел задается как tn = ½n(n+1)
# Используя euler42.txt определите, сколько в нем треугольных слов,
# преобразовывая каждую букву в число, соответствующее ее порядковому номеру
# в алфавите и складывая эти значения

from project_euler_defs import *

n = "https://projecteuler.net/project/resources/p042_words.txt"

# 1 вариант
start_time = datetime.now()
print(len([_ for _ in readmatrix("euler42.txt", mode='text')
           if isfigurate_number(sum(ord(x) - 64 for x in _), 3)]))
print(datetime.now() - start_time)

# 2 вариант
start_time = datetime.now() 
if (response := get(n, timeout=3)).status_code != 200:
    exit()
words = response.content.decode().replace('"', '').split(',')
max_n = 0
for x in words:
    max_n = max(sum(ord(_) - 64 for _ in x), max_n)
else:
    triangle_numbers = [figurate_number(_, 3) for _ in range(1, max_n + 1)]
print(len([_ for _ in words
           if sum(ord(x) - 64 for x in _) in triangle_numbers]))
print(datetime.now() - start_time)

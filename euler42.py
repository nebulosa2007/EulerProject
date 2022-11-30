# n-й член последовательности треугольных чисел задается как tn = ½n(n+1)
# Используя euler42.txt определите, сколько в нем треугольных слов,
# преобразовывая каждую букву в число, соответствующее ее порядковому номеру
# в алфавите и складывая эти значения

from project_euler_defs import *

n = "https://projecteuler.net/project/resources/p042_words.txt"

# 1 вариант
start_time = datetime.now()
words = readmatrix("euler42.txt", mode='text')
max_n = len(max(words, key=len)) * (ord('Z') - 64)
triangle_numbers = [triangle_number(_) for _ in range(1, max_n + 1)]
triangle_words = []
for i in words:
    sum_letters = sum(ord(_) - 64 for _ in i)
    if sum_letters in triangle_numbers:
        triangle_words.append(i)
else:
    print(len(triangle_words))
print(datetime.now() - start_time)

# 2 вариант
start_time = datetime.now()
response = get(n, timeout=3)
if response.status_code != 200:
    exit()
words = response.content.decode().replace('"', '').split(',')
max_n = 0
for x in words:
    max_n = max(sum(ord(_) - 64 for _ in x), max_n)
else:
    triangle_numbers = [triangle_number(_) for _ in range(1, max_n + 1)]
print(len([_ for _ in words
           if sum(ord(x) - 64 for x in _) in triangle_numbers]))
print(datetime.now() - start_time)

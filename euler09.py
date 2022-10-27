# Существует только одна тройка Пифагора, для которой a + b + c = 1000.
# Найдите произведение abc.

from datetime import datetime

n = 1_000

# 1 Вариант
start_time = datetime.now()
for a in range(n // 3):
    for b in range(a + 1, (n - a) // 2):
        c = n - a - b
        if a * a + b * b == c * c:
            print(a * b * c)
print(datetime.now() - start_time)

# 2 Вариант
start_time = datetime.now()
pass
print(datetime.now() - start_time)

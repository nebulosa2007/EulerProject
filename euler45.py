# Можно убедиться в том, что T285 = P165 = H143 = 40755
# Найдите следующее треугольное число, являющееся также пятиугольным и
# шестиугольным

from project_euler_defs import *

n = 143

# 1 вариант
start_time = datetime.now()
test_number = figurate_number(i := n + 1, 6)
while not isfigurate_number(test_number, 5):
    test_number = figurate_number(i := i + 1, 6)
print(figurate_number(i * 2 - 1, 3))
print(datetime.now() - start_time)

# 2 вариант
start_time = datetime.now()
pass
print(datetime.now() - start_time)

# Сколько различных членов имеет последовательность a^b для
# 2 ≤ a ≤ 100 и 2 ≤ b ≤ 100?

from project_euler_defs import *

n = 100

# 1 вариант
start_time = datetime.now()
powers = []
for a in range(2, n + 1):
    for b in range(2, n + 1):
        if (x := a ** b) not in powers:
            powers.append(x)
print(len(powers))
print(datetime.now() - start_time)

# 2 вариант
start_time = datetime.now()
powers = set([a ** b for a in range(2, n + 1) for b in range(2, n + 1)])
print(len(powers))
print(datetime.now() - start_time)

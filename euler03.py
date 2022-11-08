# Каков самый большой делитель числа 600 851 475 143,
# являющийся простым числом?

from project_euler_defs import *

n = 600_851_475_143

# 1 вариант
start_time = datetime.now()
print(max(maxcommondivisors(n)))
print(datetime.now() - start_time)

# 2 вариант
start_time = datetime.now()
pass
print(datetime.now() - start_time)

# Найдите сумму всех пан-цифровых произведений, для которых равенство
# "множимое × множитель = произведение" можно записать цифрами от 1 до 9,
# используя каждую цифру только один раз.

from project_euler_defs import *

n = 10

# 1 вариант
start_time = datetime.now()
pan_product = {}
template = [_ for _ in range(1, n)]
for a in range(99, 1, -1):
    for b in range(9999, 1, -1):
        digits = [int(_) for _ in sorted(list(str(a))
                                         + list(str(b))
                                         + list(str(a * b)))]
        if (digits == template and a * b not in pan_product.values()):
            pan_product[a, b] = a * b
else:
    print(sum(sorted(pan_product.values())))
print(datetime.now() - start_time)

# 2 вариант
start_time = datetime.now()
print(sum(i for i in range(1, 10_000) if ispandigital_product(i)))
print(datetime.now() - start_time)

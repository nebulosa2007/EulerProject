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


# Given integer x, this returns the integer floor(sqrt(x)).
def sqrt(x):
    assert x >= 0
    i = 1
    while i * i <= x:
        i *= 2
    y = 0
    while i > 0:
        if (y + i)**2 <= x:
            y += i
        i //= 2
    return y


def has_pandigital_product(n):
    for i in range(1, sqrt(n) + 1):
        if n % i == 0:
            temp = str(n) + str(i) + str(n // i)
            if "".join(sorted(temp)) == "123456789":
                return True
    return False


print(sum(i for i in range(1, 10000) if has_pandigital_product(i)))
print(datetime.now() - start_time)

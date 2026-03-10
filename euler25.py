# Каков порядковый номер первого члена последовательности
# Фибоначчи, содержащего 1000 цифр?

from datetime import datetime


def fibonacci(f1=0, f2=1):
    """Итерируемая функция вычисления следующего числа Фибоначчи"""
    while True:
        yield f1
        f1, f2 = f2, f1 + f2


def euler25():
    n = 1_000

    # 1 вариант
    start_time = datetime.now()
    fb_counter = 0
    iterator = fibonacci()
    fb_num = next(iterator)
    while len(str(fb_num)) < n:
        fb_counter += 1
        fb_num = next(iterator)
    print(fb_counter)
    print(datetime.now() - start_time)

    # 2 вариант
    start_time = datetime.now()
    fb_counter = 0
    for i in fibonacci():
        if len(str(i)) == n: break
        fb_counter += 1
    print(fb_counter)
    print(datetime.now() - start_time)


if __name__ == "__main__":
    euler25()

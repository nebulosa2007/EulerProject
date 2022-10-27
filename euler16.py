# Какова сумма цифр числа 2 в степени 1000?

from datetime import datetime

n = 1_000

if __name__ == '__main__':
    # 1 вариант
    start_time = datetime.now()
    print(sum(int(x) for x in list(str(2 ** n))))
    print(datetime.now() - start_time)

    # 2 вариант
    start_time = datetime.now()
    print(sum(map(int, str(2**1000))))
    print(datetime.now() - start_time)
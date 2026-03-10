# Сколько букв понадобится для записи всех чисел от 1 до 1000
# (one thousand) включительно?

from datetime import datetime

n = 1_000


def numerals(number):
    """Возвращет заданное число прописью"""
    assert number < 1_000_000
    numerals_number = []
    numbers = {1: 'one', 2: 'two', 3: 'three', 4: 'four',
               5: 'five', 6: 'six', 7: 'seven', 8: 'eight',
               9: 'nine', 10: 'ten', 11: 'eleven', 12: 'twelve',
               13: 'thirteen', 14: 'fourteen', 15: 'fifteen',
               16: 'sixteen', 17: 'seventeen', 18: 'eighteen',
               19: 'nineteen', 20: 'twenty', 30: 'thirty', 40: 'forty',
               50: 'fifty', 60: 'sixty', 70: 'seventy', 80: 'eighty',
               90: 'ninety', 100: "hundred", 1_000: "thousand"}
    morethanhundred = False
    for x in [1000, 100]:
        if number >= x:
            numerals_number.append(numbers[number // x])
            numerals_number.append(numbers[x])
            number = number - number // x * x
            morethanhundred = True
    if morethanhundred and number > 0:
        numerals_number.append('and')
    if number >= 20:
        numerals_number.append(numbers[number // 10 * 10])
        number = number - number // 10 * 10
    if number in numbers:
        numerals_number.append(numbers[number])
    return numerals_number

# 1 вариант
start_time = datetime.now()
print(f'From 1 to {n} sum symbols is:',
      sum(len(''.join(numerals(x))) for x in range(1, n + 1)))
print(datetime.now() - start_time)

# 2 вариант
start_time = datetime.now()
pass
print(datetime.now() - start_time)

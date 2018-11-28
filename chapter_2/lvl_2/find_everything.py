import math
from functools import reduce


def get_everything(number):
    tens = math.floor(number / 10)
    units = number % 10
    list_of_digits = [int(d) for d in str(number)]
    sum_of_digits = sum(list_of_digits)
    multiple = reduce(lambda x, y: x*y, list_of_digits)
    return tens, units, sum_of_digits, multiple


# https://www.codewars.com/kata/54c27a33fb7da0db0100040e/train/python

import math
def is_square(n):
    if n<0: return False
    else: return n == math.isqrt(n) ** 2

#print(is_square(144))

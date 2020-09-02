# https://www.codewars.com/kata/54c27a33fb7da0db0100040e/train/python

import math
def is_square(n):
    if n<0: return False
    else:
        num=math.sqrt(n)
        mylist=str(num).split(".")
        if int(mylist[1])>0:
            return False
        else: return True

#print(is_square(144))
#print(is_square(14))

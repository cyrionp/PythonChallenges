# https://www.codewars.com/kata/55f2b110f61eb01779000053/train/python

def get_sum(a,b):
    sum=0
    higher=b if b>a else a
    lower=a if b>a else b
    while lower<=higher:
        sum+=lower
        lower+=1
    return sum

print(get_sum(-1,2))

# https://www.codewars.com/kata/571d42206414b103dc0006a1/train/python

def arr(n=0):
    # [ the numbers 0 to N-1 ]
    numList=[]
    if n==None:return []
    elif n==1: return [0]
    else:
        for i in range (0,int(n)): numList.append(i)
        if len(numList)<2: return []
        else: return numList

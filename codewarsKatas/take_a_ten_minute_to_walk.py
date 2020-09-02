# https://www.codewars.com/kata/54da539698b8a2ad76000228/train/python

def is_valid_walk(walk):
    step=walk[0]
    walk.pop(0)
    flag=None
    flag2=0

    if len(walk)+1!=10: flag=False
    else:
        for i in walk:
            if i==step:
                step=i
                flag2+=1
        if flag2>0:flag=False

    return True if flag==True else False

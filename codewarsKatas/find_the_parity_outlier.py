# https://www.codewars.com/kata/5526fc09a1bbd946250002dc/train/python

def find_outlier(integers):
    even,odd,val_even,val_odd=0,0,0,0
    for num in integers:
        if num%2==0:
            val_even=num
            even+=1
        else:
            val_odd=num
            odd+=1
    return val_even if odd>even else val_odd

#print(find_outlier([1,2,3,5,7]))

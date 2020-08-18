# https://www.codewars.com/kata/541c8630095125aba6000c00/train/python

def digital_root(n):
    list_n=[char for char in str(n)]
    while True:
        sum=0
        if len(list_n)>1:
            for num in list_n: sum+=int(num)
            list_n=[char for char in str(sum)]
        else: break
    result=""
    for num in list_n: result+=num
    return int(result)

#number=int(input("Number: "))
#print(digital_root(number))

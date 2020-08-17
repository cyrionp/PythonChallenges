# https://www.codewars.com/kata/5467e4d82edf8bbf40000155/train/python

def descending_order(num):
    list_number=[char for char in str(num)]
    highestNumber=""
    k=len(str(num))
    for i in range(len(str(num))):
        highestNumber+=list_number[k-1]
        k-=1
    return highestNumber

number=int(input("Number: "))
print(descending_order(number))

#### NOT FINISHED YET ####

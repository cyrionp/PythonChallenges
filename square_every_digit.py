# https://www.codewars.com/kata/546e2562b03326a88e000020/train/python

def square_digits(num):
    list_num=[]
    new_num=""
    for n in str(num): list_num.append(int(n))
    for number in list_num: new_num+=str(number**2)
    return int(new_num)

#number=int(input("Number: "))
#print(square_digits(number))

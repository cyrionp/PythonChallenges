# https://www.codewars.com/kata/525f50e3b73515a6db000b83/train/python

def create_phone_number(n):
    first,second,third="","",""
    for i in n[:3]: first+=str(i)
    for i in n[3:6]: second+=str(i)
    for i in n[6:]: third+=str(i)
    return f"({first}) {second}-{third}"

#number=[0,2,4,2,3,5,6,3,8,9]
#print(create_phone_number(number))

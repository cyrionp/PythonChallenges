# https://www.codewars.com/kata/55908aad6620c066bc00002a/train/python

def xo(s):
    counter_x,counter_o,myList=0,0,[char for char in s.lower()]
    for letter in myList:
        if letter=="x": counter_x+=1
        elif letter=="o": counter_o+=1
    return True if counter_x==counter_o else False


#myStr=input("String: ")
#print(xo(myStr))

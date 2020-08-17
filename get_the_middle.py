# https://www.codewars.com/kata/56747fd5cb988479af000028/train/python

def get_middle(s): return s[int(len(s)/2)] if len(s)%2!=0 else s[int(len(s)/2-1)]+s[int(len(s)/2)]

#myString=input("String: ")
#print(get_middle(myString))

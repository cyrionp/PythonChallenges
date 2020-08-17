# https://www.codewars.com/kata/5667e8f4e3f572a8f2000039/train/python

#Take each letters index
#Add to string each letters multiplied by its index (first letter must be uppercase and others lowercase)
#Add - between each set

def accum(s):
    accummedStr=s[0].upper()
    for i in range(1,len(s)): accummedStr+="-"+s[i].upper()+(s[i].lower()*i)
    return accummedStr

#myStr=input("String: ")
#print(accum(myStr))

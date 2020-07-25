def longest(s1, s2):
    myStr=""
    myCharList=[]
    for char in list(s1):
        if char in myCharList:
            i=0
        else:
            myCharList.append(char)
    for char in list(s2):
        if char in myCharList:
            i=0
        else:
            myCharList.append(char)

    myCharList.sort()
    for char in myCharList:
        myStr+=char

    return myStr

s1=input("Girin: ")
s2=input("Girin: ")
print(longest(s1,s2))

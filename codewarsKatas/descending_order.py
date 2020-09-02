# https://www.codewars.com/kata/5467e4d82edf8bbf40000155/train/python

'''
def Convert(string):
    list1=[]
    list1[:0]=string
    list1.sort()
    list1.reverse()
    print(list1)
    return list1

def descending_order(num):
    myList=Convert(str(num))
    orderedList=[]
    orderedList.append(myList[0])
    max=orderedList[-1]
    for i in myList:
        if int(i)>int(max):
            max=i
            orderedList.append(max)
    result=""
    for i in orderedList:
        result+=i
    return result

print(descending_order(1223))
'''

def Convert(string):
    list1=[]
    list1[:0]=string
    list1.sort()
    list1.reverse()
    return list1

def descending_order(num):
    myList=Convert(str(num))
    print(myList)
    result=""
    for i in myList:
        result+=i
    return int(result)

#print(descending_order(124553))

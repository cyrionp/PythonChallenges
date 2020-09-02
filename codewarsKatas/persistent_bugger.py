def Convert(string):
    list1=[]
    list1[:0]=string
    return list1

def MultiplyList(myList):
    resultNum=1
    for num in myList:
        resultNum*=int(num)
    result=str(resultNum)
    return Convert(result)

def persistence(n):
    list_num=Convert(n)
    counter=0
    while True:
        if len(list_num)>1:
            list_num=MultiplyList(list_num)
            counter+=1
        else:
            break
    return counter



number=input("Number: ")
print(persistence(number))

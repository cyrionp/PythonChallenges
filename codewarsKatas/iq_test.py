def iq_test(numbers):
    myStr=numbers.split(" ")
    map_object = map(int, myStr)
    myStr = list(map_object)
    even,odd=0,0

    for num in myStr:
        if num%2==0: #number is even
            even+=1
        else:
            odd+=1

    if even==1 and odd>1:
        i=1
        for num in myStr:
            if num%2==0:
                return i
            else:
                i+=1

    elif even>1 and odd==1:
        i=1
        for num in myStr:
            if num%2==0:
                i+=1
            else:
                return i

sayilar=input("Sayıları boşluklu olarak girin: ") #kodda yok
print(iq_test(sayilar)) #kodda yok

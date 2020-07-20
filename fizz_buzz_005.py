#Kullanıcıdan alınan değer uzunluktaki bir dizi içindeki üçün katları için "Fizz", beşin katları için "Buzz",
#hem beş hem de üçün katları için "FizzBuzz", her üçü de değilse sayının kendisini yazdırır.

def fizzbuzz(number):
    if number%3==0 and number%5==0:
        return "FIZZBUZZ !"
    elif number%3==0 and number%5!=0:
        return "Fizz"
    elif number%3!=0 and number%5==0:
        return "Buzz"
    else:
        return "Your input is not valid for fizz/buzz calculation"

while True:
    num=int(input("\nWrite a number: "))
    print(fizzbuzz(num))
    print("")
    isContinue=int(input("Do you want to calculate again?\n1) Yes OTHERS) No\nYour choice: "))
    if isContinue!=1:
        break

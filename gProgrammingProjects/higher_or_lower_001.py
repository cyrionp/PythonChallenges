def Compare(first,second):
    if first>second:
        print(f"{first} is higher than {second}")
    elif first<second:
        print(f"{first} is lower than {second}")
    else:
        print("They are equal")

while True:
    num1=int(input("Enter first number: "))
    num2=int(input("Enter second number: "))

    Compare(num1,num2)

    isContinue=int(input("Do you want to compare different numbers?\n1)Yes Others)No\nYour choice: "))
    if isContinue!=1:
        break

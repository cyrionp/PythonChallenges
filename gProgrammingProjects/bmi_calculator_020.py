def BMI(length,weigth):
    bmi=weigth/(length*length)
    print(f"\nYou BMI is {bmi}")

    if bmi<18.5:
        print("Underweight")
    elif bmi>=18.5 and bmi<25:
        print("Normal weight")
    elif bmi>=25 and bmi<30:
        print("Overweight")
    else:
        print("Obesity")

while True:
    length=float(input("Your length (like 1.75) : "))
    weigth=float(input("Your weigth: (in kg) : "))
    BMI(length,weigth)
    isContinue=int(input("\nDo you want to calculate again?\n1) Yes OTHERS) No\nYour choice: "))
    if isContinue!=1:
        break

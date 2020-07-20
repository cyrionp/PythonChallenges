def Converter(selection,degree,convertedDegree=0):
    while True:
        if selection==1:
            convertedDegree=(degree*1.8)+32
            print(f"{degree} °C is equals {convertedDegree} °F")
            break
        elif selection==2:
            convertedDegree=(degree-32)/1.8
            print(f"{degree} °F is equals {convertedDegree} °C")
            break
        else:
            print("You have to select 1 or 2")

while True:
    print("1) Celcius to Fahrenheit")
    print("2) Fahrenheit to Celcius")

    selection=int(input("Your choice: "))
    degree=float(input("Enter a degree: "))

    Converter(selection,degree)

    isContinue=int(input("Do you want to convert again?\n1) Yes OTHERS) No\nYour cohice: "))
    if isContinue!=1:
        break

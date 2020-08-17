from datetime import *

def AgeCalculator():
    while True:
        while True:
            try:
                global birthdate
                birthdate = datetime.strptime(input("\nYour birth date (d.m.Y): "), "%d.%m.%Y")
                break
            except:
                print("\nYou have to write a date in correct way (DD.MM.YYYY)\n")

        age = datetime.now() - birthdate
        print(f"\nYou lived for {age.total_seconds()} seconds until now.")

        isContinue=int(input("\nDo you want to calculate again?\n1) Yes OTHERS) No\nYour choice: "))
        if isContinue!=1:
            break
AgeCalculator()

import random

def App():
    choices=["Rock","Paper","Scissors"]
    pointUser=0
    pointMachine=0
    pointTotal=int(input("How many points do you want to finish the game at?\nYour choice: "))
    while True:
        print(f"1) {choices[0]} or 2) {choices[1]} or 3) {choices[2]}: ")
        number=int(input("Your choice: "))
        if number==1 or number==2 or number==3:
            break
        else:
            print("You have to select 1-2-3")

    while True:
        if pointUser>=pointTotal or pointMachine>=pointTotal:
            print("Game is over")
            print(f"You: {pointUser} Machine: {pointMachine}")
            if pointUser>pointMachine:
                print("YOU WON WHOLE MATCH!")
                break
            elif pointMachine>pointUser:
                print("MACHINE WON WHOLE MATCH!")
                break

        user=choices[number-1]
        machine=random.choice(choices)

        print(f"Your choice: {user}\nMachine's choice: {machine}")

        if user==machine:
            print("DRAW")
        elif user==choices[0]:
            if machine==choices[1]:
                print("Machine won!")
                pointMachine+=1
            elif machine==choices[2]:
                print("You won!")
                pointUser+=1
        elif user==choices[1]:
            if machine==choices[0]:
                print("You won!")
                pointUser+=1
            elif machine==choices[2]:
                print("Machine won!")
                pointMachine+=1
        elif user==choices[2]:
            if machine==choices[0]:
                print("Machine won!")
                pointMachine+=1
            elif machine==choices[1]:
                print("You won!")
                pointUser+=1

while True:
    App()
    isContinue=int(input("Do you want to play again?\n1) Yes OTHERS) No\nYour choice: "))
    if isContinue!=1:
        break

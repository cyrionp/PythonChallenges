def LoveCalculator(yourname,matesname):
    love = len(yourname) + len(matesname)
    if len(yourname) > len(matesname):
        love -= 5
    else:
        love += 3

    love *= 42
    love = love / (100 + len(matesname))
    love = 10 if love > 10 else round(love, 0)

    print(f"Love score between {yourname} and {matesname} is:\n{love}/10")

while True:
    while True:
        print("Love Calculator")
        yourname=input("Your name: ")
        matesname=input("Your gf/bf's name: ")
        if len(yourname)<=1 or len(matesname)<=1:
            print("Names are invalid")
        else:
            break

    LoveCalculator(yourname,matesname)
    isContinue=int(input("Do you want to calculate again?\n1) Yes OTHERS) No\nYour choice: "))
    if isContinue!=1:
        break

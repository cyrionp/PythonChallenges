import random
import string

def PasswordGenerator(length):
    letters=string.ascii_letters
    digits=string.digits
    punctuation=string.punctuation
    level=int(input("1)Low 2)Mid 3)High\nChoose password safety level: "))
    if level==1:
        password = "".join(random.choice(letters) for x in range(length))
        print(password)
    elif level==2:
        password = "".join(random.choice(letters+digits) for x in range(length))
        print(password)
    elif level==3:
        password = "".join(random.choice(letters+digits+punctuation) for x in range(length))
        print(password)

while True:
    print("Welcome to Password Generator!")
    length=int(input("Password has to have chars: "))
    PasswordGenerator(length)
    isContinue=int(input("Do you want to generate again?\n1) Yes OTHERS) No\nYour choice: "))
    if isContinue!=1:
        break

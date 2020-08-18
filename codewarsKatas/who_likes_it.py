# https://www.codewars.com/kata/5266876b8f4bf2da9b000362/train/python

def likes(names):
    counter=0
    for name in names:
        counter+=1

    if counter==0:
        return("no one likes this")

    elif counter==1:
        return(f"{names[0]} likes this")

    elif counter==2:
        return(f"{names[0]} and {names[1]} like this")

    elif counter==3:
        return(f"{names[0]}, {names[1]} and {names[2]} like this")

    elif counter>3:
        return(f"{names[0]}, {names[1]} and {counter-2} others like this")

#names=input("Names: ")
#print(likes(names))

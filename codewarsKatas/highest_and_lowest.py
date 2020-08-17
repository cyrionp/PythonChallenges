# https://www.codewars.com/kata/554b4ac871d6813a03000035/train/python

def high_and_low(numbers):
    list_numbers=numbers.split()
    global highest, lowest
    highest,lowest=list_numbers[0],list_numbers[0]
    for num in list_numbers:
        if int(num)>int(highest): highest=num
        if int(num)<int(lowest): lowest=num
    return highest+" "+lowest

givenNumbers=input("Numbers: ")
print(high_and_low(givenNumbers))

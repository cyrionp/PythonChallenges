def CountVowels(myStr):
    counter=0
    chars_vowels="aeıioöuüAEIİOÖUÜ" #Turkish alphabet's vowels
    for char in myStr:
        if char in chars_vowels:
            counter+=1
    if counter<=1:
        print(f"There is {counter} vowel")
    else:
        print(f"There are {counter} vowels")

while True:
    countThatString=input("\nWrite a string to find vowels: ")
    CountVowels(countThatString)
    isContinue=int(input("\nDo you want to count again?\n1) Yes OTHERS) No\nYour choice: "))
    if isContinue!=1:
        break

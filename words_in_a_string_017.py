def CountWords(myStr):
    words=myStr.split(" ")
    counter=len(words)
    if counter<=1:
        print(f"There is {counter} word")
    else:
        print(f"There are {counter} words")

while True:
    inputString=input("\nWrite a string to count words: ")
    CountWords(inputString)
    isContinue=int(input("\nDo you want to count again?\n1) Yes OTHERS) No\nYour choice: "))
    if isContinue!=1:
        break

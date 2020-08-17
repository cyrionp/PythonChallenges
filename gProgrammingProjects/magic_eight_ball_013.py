import random

def Magic8Ball():
    while True:
        while True:
            invalidQuestion="Why don't you write your question?.Can't you write honey?.Please gimme a question :(.Are you an alien?".split(".")
            validQuestion="I say for this, YES.Sorry pal, it can't be.Maybe yes, maybe no.My sources tell me YES.No way!.Look, it depends.Bzzz, c-can you sa-say it again?".split(".")
            question=input("\nQuestion: ")
            if len(question)<3:
                print(f"\nMagic 8 Ball: {random.choice(invalidQuestion)}")
            else:
                print(f"\nMagic 8 Ball: {random.choice(validQuestion)}")
                break
        isContinue=int(input("\nDo you want to shake it again?\n1) Yes OTHERS) No\nYour choice: "))
        if isContinue!=1:
            break

Magic8Ball()

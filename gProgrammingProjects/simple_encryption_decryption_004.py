def encrypt(text, value, output=""):
    for char in text:
        output = "{}{}".format(output, chr(ord(char) + value))
    return output


def decrypt(text, value, output=""):
    for char in text:
        output = "{}{}".format(output, chr(ord(char) - value))
    return output

while True:
    print("")
    print("*"*30)
    print("")
    print("1) Encryption\n2) Decryption")
    selection=int(input("\nYour choice: "))

    if selection==1:
        i = int(input("\nIncrement value: "))
        text = input("\nType your text: ")
        print("\nEncrypted text: {}".format(encrypt(text, i)))
        isContinue=int(input("\nDo you want to do it again?\n1) Yes OTHERS) No\nYour choice: "))
        if isContinue!=1:
            break

    elif selection==2:
        i = int(input("\nIncrement value: "))
        text = input("\nType for decrypt: ")
        print("\nDecrypted text: {}".format(decrypt(text, i)))
        isContinue=int(input("\nDo you want to do it again?\n1) Yes OTHERS) No\nYour choice: "))
        if isContinue!=1:
            break

    else:
        print("\nYou have to select 1 or 2")

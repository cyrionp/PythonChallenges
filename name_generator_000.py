import random

def name_generator():
    firstNames=["Ahmet","Ali","Ayşe","Adem","Aslı","Berna","Ceren","Ceyhun","Deniz","Elif","Ersin","Faruk","Fatma","Gamze","Zehra","Zeynel"]
    lastNames=["Durmaz","Yılmaz","Kaya","Güngör","Çelik","Sarı","Nergüz","Özdemir","Demir","Kara","Mavi","Ak","Ağaoğlu","Karahan","Ünlü"]
    return f"{random.choice(firstNames)} {random.choice(lastNames)}"

times=int(input("How many names do you want to generate: "))

for i in range(times):
    print(name_generator())

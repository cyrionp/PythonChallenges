# https://www.codewars.com/kata/52fba66badcd10859f00097e/train/python

def disemvowel(troll):
    list_vowels="aeiouAEIOU"
    trollback=""
    for i in range(len(troll)):
        if troll[i] not in list_vowels: trollback=trollback+troll[i]
        i+=1
    return trollback

#print(disemvowel("Seni PisLIk"))

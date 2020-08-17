# https://www.codewars.com/kata/54ff3102c1bad923760001f3/train/python

def get_count(input_str):
    num_vowels = 0
    list_vowels=["a","e","i","o","u"]
    for i in range(len(input_str)):
        if input_str[i] in list_vowels: num_vowels+=1
        i+=1
    return num_vowels

#sentence=input("Sentence: ")
#print(get_count(sentence))

# https://www.codewars.com/kata/57cebe1dc6fdc20c57000ac9/train/python

#Return the length of the shortest word

def find_short(s):
    list_words=s.split(" ")
    shortest=len(list_words[0])
    for word in list_words:
        if len(word)<shortest: shortest=len(word)
    return shortest

#myStr=input("String: ")
#print(find_short(myStr))

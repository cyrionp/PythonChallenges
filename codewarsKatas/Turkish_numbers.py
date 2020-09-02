# https://www.codewars.com/kata/5ebd53ea50d0680031190b96/train/python

def get_turkish_number(num):
    firstletter,secondletter,returnedstring="","",""
    dict_tens={1:"on",2:"yirmi",3:"otuz",4:"kırk",5:"elli",6:"altmış",7:"yetmiş",8:"seksen",9:"doksan"}
    dict_numbers={1:"bir",2:"iki",3:"üç",4:"dört",5:"beş",6:"altı",7:"yedi",8:"sekiz",9:"dokuz"}

    firstletter=str(num)[0]
    returnedstring+=dict_numbers[firstletter]
    if len(str(num))==2: secondletter=str(num)[1]
    returnedstring+=dict_numbers[secondletter]
    return returnedstring

print(get_turkish_number(12))

# https://www.codewars.com/kata/5262119038c0985a5b00029f/train/python

def is_prime(num):
    counter=0
    for i in range (1,int(num)+1):
        if num%i==0: counter+=1

    return True if counter==2 else False

# TIME OUT, NEE TO BE A SHORTHER ALGORITHM

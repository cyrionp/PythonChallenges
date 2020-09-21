# https://www.codewars.com/kata/571e9af407363dbf5700067c/train/python

from random import random
myList=[]

def squares(n):
    for i in range(1,n+1): myList.append(i**2)
    return myList

def num_range(n, start, step):
    counter=0
    myList.append(start)
    while True:
        start+=n
        myList.append(start)
        counter+=1
        if step==counter: break
    return myList

def rand_range(n, mn, mx):
    while True:
        myList.append(random(mn,mx))
        if len(myList)==n: break
    return myList

def primes(n):
    while True:
        i=2
        if n%i==0:
            myList.append(i)
            i+=1
        if n==i:break
    return myList

# DOESN'T WORK

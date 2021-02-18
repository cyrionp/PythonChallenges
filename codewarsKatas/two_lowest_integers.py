# https://www.codewars.com/kata/558fc85d8fd1938afb000014/train/python

def sum_two_smallest_numbers(numbers):
    numbers.sort()
    return numbers[0]+numbers[1]

print(sum_two_smallest_numbers())

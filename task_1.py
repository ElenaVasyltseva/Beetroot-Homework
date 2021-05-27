#  Task 1
#  The greatest number
#  Write a Python program to get the largest number
#  from a list of random numbers with the length of 10
#  Constraints: use only while loop and random module to generate numbers

import random

list_of_numbers = []

count = 0
while count < 10:
    number = random.randrange(0, 100, 10)
    list_of_numbers.append(number)
    count += 1
print(max(list_of_numbers))

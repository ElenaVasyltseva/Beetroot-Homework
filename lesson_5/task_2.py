#  Task 2
#  Exclusive common numbers.
#  Generate 2 lists with the length of 10 with random integers from 1 to 10,
#  and make a third list containing the common integers
#  between the 2 initial lists without any duplicates.
#  Constraints: use only while loop and random module to generate numbers

import random

first_list = []
second_list = []

count = 0

while count < 10:
    num_for_first_list = random.randint(1, 10)
    first_list.append(num_for_first_list)
    num_for_second_list = random.randint(1, 10)
    second_list.append(num_for_second_list)
    count += 1

result_list = list(set(first_list + second_list))
print(result_list)

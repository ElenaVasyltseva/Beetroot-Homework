#  Task 3
#  Extracting numbers.
#  Make a list that contains all integers from 1 to 100,
#  then find all integers from the list that are divisible by 7
#  but not a multiple of 5, and store them in a separate list. Finally, print the list.
#  Constraint: use only while loop for iteration

integers_list = list(range(1, 101))
extracting_list = []
count = 0

while count < len(integers_list):
    if integers_list[count] % 7 == 0 and integers_list[count] % 5 != 0:
        extracting_list.append(integers_list[count])
    count += 1
print(extracting_list)
print(integers_list)

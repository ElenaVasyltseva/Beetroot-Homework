#  The valid phone number program.
#  Make a program that checks if a string is in the right format
#  for a phone number. The program should check that the string contains
#  only numerical characters and is only 10 characters long.
#  Print a suitable message depending on the outcome of the string evaluation.

while True:
    phone_number = input("Please, enter your phone number, without country's code:")
    if phone_number.isdigit() and len(phone_number) == 10:
        print('Great, thanks!')
        break
    else:
        print('Something wrong :( Try again!')
        continue


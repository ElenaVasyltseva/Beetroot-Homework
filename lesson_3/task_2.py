#  checking the right format for a phone number.

while True:
    phone_number = input("Please, enter your phone number, without country's code:")
    if phone_number.isdecimal() and len(phone_number) == 10:
        print('Great, thanks!')
        break
    else:
        print('Something wrong :( Try again!')
        continue

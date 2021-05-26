#  Task 2
#  The birthday greeting program.
#  Write a program that takes your name as input,
#  and then your age as input and greets you with the following:
#  “Hello <name>, on your next birthday you’ll be <age+1> years”
while True:
    user_name = input('Hello! Please, enter your name:')
    user_age = input('Please, enter your age:')
    if user_name.isalpha() and user_age.isdigit():
        print(f'Hello {user_name}, on your next birthday you\'ll be {int(user_age)+1} years')
        break
    else:
        print('Please, enter correct information')
        continue

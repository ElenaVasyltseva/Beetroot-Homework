#  Task 1
#  The Guessing Game.
#  Write a program that generates a random number between 1 and 10
#  and lets the user guess what number was generated.
#  The result should be sent back to the user via a print statement.

import random

print('I thought of a number, from 1 to 10, guess what?')
print('You have three attempts!')
print('If you want to stop, enter: 0')
hidden_number = random.randint(1, 10)
count = 1
while count < 4:
    user_number = int(input('Enter a number:'))
    count += 1
    if user_number == hidden_number:
        print(f'You win! The hidden number was: {hidden_number}')
        break
    elif user_number == 0:
        print('End games')
    else:
        print('Sorry you didn\'t guess! Try again!')
        continue
if count == 4 and user_number != 0 and user_number != hidden_number:
    print('You lose!')

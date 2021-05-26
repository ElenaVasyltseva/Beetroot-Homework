#  Task 4
#  The math quiz program
#  Write a program that asks the answer for a mathematical expression,
#  checks whether the user is right or wrong,
#  and then responds with a message accordingly.
import random

print('Hello! It\'s The math quiz!')
a = random.randint(6, 10)
b = random.randint(1, 5)

count = 0
while True:
    print(f'First question: {a} + {b} ?')
    user_answer1 = input('Your answer here:')
    if user_answer1.isdigit() and int(user_answer1) == a + b:
        print(f'Yes! Answer is {a+b}!')
        count += 1
    else:
        print('Wrong answer or incorrect input. Next question!')

    print(f'Second question: {a} - {b} ?')
    user_answer2 = input('Your answer here:')
    if user_answer2.isdigit() and int(user_answer2) == a - b:
        print(f'Yes! Answer is {a - b}!')
        count += 1
    else:
        print('Wrong answer or incorrect input. Next question!')

    print(f'Second question: {a} * {b} ?')
    user_answer3 = input('Your answer here:')
    if user_answer3.isdigit() and int(user_answer3) == a*b:
        print(f'Yes! Answer is {a*b}!')
        count += 1
    else:
        print('Wrong answer or incorrect input.')
    break
if count == 3:
    print('Wow! You have a super brain! 3 of 3 points!')
elif count == 2:
    print('It\'s a good result! 2 of 3 points!')
elif count == 1:
    print('Next time you can do better! 1 of 3 points!')
else:
    print('Today is not your day! 0 of 3 points!')

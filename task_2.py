#  Task 2
#  Write a function that takes in two numbers from the user via input(),
#  call the numbers a and b, and then returns the value of squared a divided by b,
#  construct a try-except block which raises an exception if the two values given
#  by the input function were not numbers, and if value b was zero (cannot divide by zero).

def math_func():
    try:
        a = int(input('Please enter an integer value:'))
        b = int(input('Please enter an integer value:'))
        return a**2/b
    except ValueError:
        print('You should have entered an integer value!')
    except ZeroDivisionError:
        print('You can\'t divide by zero!')


math_func()
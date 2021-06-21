#  Task 2
#  Write a Python program to access a function inside a function
#  (Tips: use function, which returns another function)


def goal():
   print('a goal scored')

def passed():
    print('made a pass')


def play_football(text):
    if text == 'ronaldo has a ball':
        return passed
    elif text == 'morato has a ball':
        return goal


play_football('ronaldo has a ball')()
play_football('morato has a ball')()
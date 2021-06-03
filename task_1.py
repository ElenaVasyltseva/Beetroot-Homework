#  Task 1
#  Write a function called oops that explicitly raises an IndexError exception when called.
#  Then write another function that calls oops inside a try/except statement to catch the error.
#  What happens if you change oops to raise KeyError instead of IndexError?

def oops():
    raise IndexError('sorry, it is wrong')
    #  raise KeyError('example')


def no_oops():
    try:
        oops()
    except IndexError:
        print('continue to work')


no_oops()

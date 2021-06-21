#  Task 1
#  Write a Python program to detect the number of local variables declared in a function.


def foo_1(x):
    y = 2
    return x+y


def count_of_variables(n):
    foo_1(n)
    return len(dir())


print(count_of_variables(5))

# or


def foo(x):
    y = 2
    return x+y


def count_variables(n):
    a = foo_1(n)
    return a


print(count_variables.__code__.co_nlocals)

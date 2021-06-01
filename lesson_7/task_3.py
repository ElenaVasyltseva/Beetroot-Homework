#  Task 3
#  A simple calculator.
#  Create a function called make_operation, which takes in a simple arithmetic operator
#  as a  first parameter(to keep things simple let it only be ‘+’, ‘-’ or ‘ * ’) and
#  an arbitrary number of arguments(only numbers) as the second parameter.
#  Then return the sum or product of all the numbers in the arbitrary parameter.For example:
#  the all make_operation(‘+’, 7, 7, 2) should return 16
#  the call make_operation(‘-’, 5, 5, -10, -20) should return 30
#  the call make_operation(‘ * ’, 7, 6) should return 42

def make_operation(arithmetic_operation, *args):
    if arithmetic_operation == '+':
        result_add = 0
        for num in args:
            result_add += num
        return result_add
    if arithmetic_operation == '-':
        result_sub = args[0]
        for num in args[1:]:
            result_sub -= num
        return result_sub
    if arithmetic_operation == '*':
        result_mul = 1
        for num in args:
            result_mul *= num
        return result_mul
    if arithmetic_operation == '/':
        result_div = args[0]
        for num in args[1:]:
            result_div /= num
        return int(result_div)


print(make_operation('+', 7, 7, 2))
print(make_operation('-', 5, 5, -10, -20))
print(make_operation('*', 7, 6))
print(make_operation('/', 12, 2, 3))

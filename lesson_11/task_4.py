#   Task 4
#   Custom exception
#   Create your custom exception named `CustomException`, you can inherit from base Exception class,
#   but extend its functionality to log every error message to a file named `logs.txt`.
#   Tips: Use __init__ method to extend functionality for saving messages to file

class CustomException(Exception):
    def __init__(self, msg):
        self.msg = msg
        with open('log.txt', 'a') as file_error:
            file_error.write(self.msg)


try:
    error_1 = CustomException('Error_ 1 --> Check user input. ')
    error_2 = CustomException('Error_ 2 --> Check if the string is correct. ')
except OSError:
    print("Checking 'log.txt' file")

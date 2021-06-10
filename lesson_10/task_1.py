#  Task 1
#  A Person class
#  Make a class called Person. Make the __init__() method take firstname,
#  lastname, and age as parameters and add them as attributes.
#  Make another method called talk() which makes prints a greeting from the person containing,
#  for example like this: “Hello, my name is Carl Johnson and I’m 26 years old”.

class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.validate_data_str(first_name)
        self.validate_data_str(last_name)
        self.validate_data_int(age)

    def validate_data_str(self, value):
        """checking string arguments """
        if len(value) > 2 and value.isalpha():
            return value
        else:
            raise ValueError('Проверьте коректность значений текстовых аргументов')

    def validate_data_int(self, value):
        """checking integer arguments """
        if type(value) == int and value > 0:
            return value
        else:
            raise ValueError('Проверьте коректность значений числовых аргументов')

    def talk(self):
        """ prints a greeting """
        print(f'Hello, my name is {self.first_name} {self.last_name} and I\'m {self.age} years old')


first_person = Person('John', 'Dou', 26)
#  first_person = Person('John', 'Do', 26)
#  first_person = Person('John', 'Dou', -26)
first_person.talk()

#  Task 2
#  Doggy age
#  Create a class Dog with class attribute `age_factor` equals to 7.
#  Make __init__() which takes values for a dog’s age.
#  Then create a method `human_age` which returns the dog’s age in human equivalent.

class Dog:
    age_factor = 7

    def __init__(self, dog_age):
        self.dog_age = self.validate_data_int(dog_age)

    def validate_data_int(self, value):
        """checking integer arguments """
        if type(value) == int and value > 0:
            return value
        else:
            raise ValueError('Check the passed arguments')

    def human_age(self):
        """prints dog's age in human equivalent"""
        print(f'The dog\'s age in human equivalent equals to {self.dog_age * self.age_factor}')


some_dog = Dog(3)
#  some_dog = Dog(-3)
#  some_dog = Dog('3')
some_dog.human_age()

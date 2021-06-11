#  Task 1
#  School
#  Make a class structure in python representing people at school.
#  Make a base class called Person, a class called Student, and another one called Teacher.
#  Try to find as many methods and attributes as you can which belong to different classes,
#  and keep in mind which are common and which are not. For example,
#  the name should be a Person attribute,  while salary should only be available to the teacher.

class Person:
    def __init__(self, last_name, first_name, age, ipn):
        self.last_name = self.validate_str(last_name)
        self.first_name = self.validate_str(first_name)
        self.age = self.validate_int(age)
        self.ipn = self.validate_ipn(ipn)

    def validate_ipn(self, value):
        """checking correctly input ipn-number"""
        if type(value) == str and value.isdigit() and len(value) == 10:
            return value
        else:
            raise ValueError('IPN-number must be contain 10 (only) numbers')

    def validate_int(self, value):
        """checking correctly input integer values"""
        if type(value) == int and value > 0:
            return value
        else:
            raise ValueError('This value must be contain only numbers, more than 0')

    def validate_str(self, value):
        """checking correctly input string parameters"""
        if len(value) >= 2 and value.isalpha():
            return value
        else:
            raise ValueError('Input must be contain only letters and at least two letters')

    def validate_allowance(self, value):
        if type(value) == int and value >= 0:
            return value
        else:
            raise ValueError('This value must be contain only numbers, positive or equal to 0')

    def description_person(self):
        """Prints information about Person"""
        print(f'''
            Имя: {self.first_name}
            Фамилия: {self.last_name}
            Возраст: {self.age}
            ИПН: {self.ipn}
        ''')


class Student(Person):
    """Aspects for student"""
    def __init__(self, last_name, first_name, age, ipn, study_group):
        super().__init__(last_name, first_name, age, ipn)
        self.study_group = self.validate_int(study_group)

    def description_person(self):
        """Prints information about student
        Overriding the parent method"""
        print(f'''
        Студент:
            Имя: {self.first_name}
            Фамилия: {self.last_name}
            Возраст: {self.age}
            ИПН: {self.ipn}
            Группа: {self.study_group}   
        ''')

    def scholarship(self, r1, r2):
        """calculation of the scholarship. r1 - increased allowance. r2 - presidential allowance"""
        r1 = self.validate_allowance(r1)
        r2 = self.validate_allowance(r2)
        base_rate = 1000
        sum_of_scholarship = base_rate + r1 + r2
        print(f'Сумма стипендии: {sum_of_scholarship}')


class Teacher(Person):
    """Aspects for teacher"""
    def __init__(self, last_name, first_name, age, ipn, academic_subject):
        super().__init__(last_name, first_name, age, ipn)
        self.academic_subject = self.validate_str(academic_subject)

    def description_person(self):
        """Prints information about teacher
        Overriding the parent method"""
        print(f'''
        Преподаватель:
            Имя: {self.first_name}
            Фамилия: {self.last_name}
            Возраст: {self.age}
            ИПН: {self.ipn}
            Предмет: {self.academic_subject}   
        ''')


person_1 = Student('Иванов', 'Иван', 18, '3356985782', 214)

#  person_1 = Student('Иванов', 'Иван', 0, '3356985782', 214)      #  test
#  person_1 = Student('Иванов', 'Иван', 18, 3356985782, 214)       #  test
#  person_1 = Student('3454', 'Иван', 18, '3356985782', 214)       #  test
#  person_1 = Student('Иванов', 'Иван', 18, '3356985782', '214')   #  test

person_1.description_person()

person_1.scholarship(500, 0)
#  person_1.scholarship(-1, 0)      #  test
#  person_1.scholarship('0', 0)     #  test


person_2 = Teacher('Петров', 'Петр', 35, '4561237895', 'Информатика')
#  person_2 = Teacher('Петров', 'Петр', 35, '4561', 'Информатика')    #  test
#  person_2 = Teacher('Петров', 'Петр', 35, '4561237895', '101')      #  test

person_2.description_person()

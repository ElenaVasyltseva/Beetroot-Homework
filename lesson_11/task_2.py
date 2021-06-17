#  Task 2
#  Mathematician
#  Implement a class Mathematician which is a helper class for doing math operations on lists
#  The class doesn't take any attributes and only has methods:
#  square_nums (takes a list of integers and returns the list of squares)
#  remove_positives (takes a list of integers and returns it without positive numbers
#  filter_leaps (takes a list of dates (integers) and removes those that are not 'leap years'


class Mathematician:
    def if_list_of_numbers_empty(self, list_of_numbers):
        """Checking parameter list of numbers, if list is empty - raise ValueError"""
        if len(list_of_numbers) != 0:
            return list_of_numbers
        else:
            raise ValueError('List of numbers is empty')

    def square_nums(self, list_of_numbers):
        """takes a list of integers and returns the list of squares"""
        self.if_list_of_numbers_empty(list_of_numbers)
        square_nums_list = []
        for i in list_of_numbers:
            square_nums_list.append(i * i)
        return square_nums_list

    def remove_positives(self, list_of_numbers):
        """takes a list of integers and returns it without positive numbers"""
        self.if_list_of_numbers_empty(list_of_numbers)
        remove_positives_list = []
        for i in list_of_numbers:
            if i < 0:
                remove_positives_list.append(i)
        return remove_positives_list

    def filter_leaps(self, list_of_numbers):
        """takes a list of dates (integers) and removes those that are not 'leap years'"""
        self.if_list_of_numbers_empty(list_of_numbers)
        leap_years_list = []
        for i in list_of_numbers:
            if (i % 4 == 0) and (i % 100 != 0) or (i % 400 == 0):
                leap_years_list.append(i)
        return leap_years_list


m = Mathematician()

print(m.square_nums([7, 11, 5, 4]))                             # [49, 121, 25, 16]
#  print(m.square_nums([]))                                     #  test
print(m.remove_positives([26, -11, -8, 13, -90]))               # [-11, -8, -90]
#  print(m.remove_positives([]))                                # test
print(m.filter_leaps([2001, 1884, 1995, 2003, 2020]))           # [1884, 2020]
#  print(m.filter_leaps([]))                                    # test

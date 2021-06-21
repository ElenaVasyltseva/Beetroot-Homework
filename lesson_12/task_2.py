#  Task 2
#  Library
#  Write a class structure that implements a library. Classes:
#  1) Library - name, books = [], authors = []
#  2) Book - name, year, author (author must be an instance of Author class)
#  3) Author - name, country, birthday, books = []
#  Library class
#  Methods:
#  - new_book(name: str, year: int, author: Author) -
#  returns an instance of Book class and adds the book to the books list for the current library.
#  - group_by_author(author: Author) - returns a list of all books grouped by the specified author
#  - group_by_year(year: int) - returns a list of all the books grouped by the specified year
#  All 3 classes must have a readable __repr__ and __str__ methods.
#  Also, the book class should have a class variable which holds the amount of all existing books

class Book:
    book_count = 0

    def __init__(self, name, year, author):
        self.name = self.validate_data_str(name)
        self.year = self.validate_data_int(year)
        self.author = self.validate_data_class_Author(author)

    def validate_data_int(self, value):
        """checking integer arguments """
        if type(value) == int and value > 0:
            return value
        else:
            raise ValueError('Check integer arguments ')

    def validate_data_class_Author(self, value):
        if isinstance(value, Author):
            return value
        else:
            raise ValueError('There must be class Author')

    def validate_data_str(self, value):
        """checking string arguments """
        if len(value) > 2 and type(value) == str:
            return value
        else:
            raise ValueError('Проверьте коректность значений текстовых аргументов')

    def __repr__(self):
       return f'{self.name}, {self.year}, {self.author}'

    def __str__(self):
        return f'{self.name}, {self.year}, {self.author}'


class Author:
    def __init__(self, name, country, birthday):
        self.name = self.validate_data_str(name)
        self.country = self.validate_data_str(country)
        self.birthday = self.validate_data_int(birthday)
        self.author_books = []

    def validate_data_int(self, value):
        """checking integer arguments """
        if type(value) == int and value > 0:
            return value
        else:
            raise ValueError('Проверьте коректность значений числовых аргументов')

    def validate_data_str(self, value):
        """checking string arguments """
        if len(value) > 2 and type(value) == str:
            return value
        else:
            raise ValueError('Проверьте коректность значений текстовых аргументов')

    def if_list_empty(self, value):
        """checking if list of channels is empty"""
        if len(value) == 0:
            raise ValueError('Library is empty')
        else:
            return value

    def validate_data_class_Book(self, value):
        if isinstance(value, Book):
            return value
        else:
            raise ValueError('There must be class Book')

    def add_book_author(self, book):
        """add book in list a certain author"""
        self.validate_data_class_Book(book)
        self.author_books.append(book)

    def get_book_author(self):
        """get all books of author"""
        self.if_list_empty(self.author_books)
        return self.author_books

    def __repr__(self):
        return f'{self.name}, {self.country}, {self.birthday}'

    def __str__(self):
        return f'{self.name}, {self.country}, {self.birthday}'


class Library:
    books = []
    authors = []

    def __init__(self, name):
        self.name = name

    def if_list_empty(self, value):
        """checking if list of channels is empty"""
        if len(value) == 0:
            raise ValueError('Library is empty')
        else:
            return value

    def validate_data_int(self, value):
        """checking integer arguments """
        if type(value) == int and value > 0:
            return value
        else:
            raise ValueError('Проверьте коректность значений числовых аргументов')

    def validate_data_str(self, value):
        """checking string arguments """
        if len(value) > 2 and type(value) == str:
            return value
        else:
            raise ValueError('Проверьте коректность значений текстовых аргументов')

    def validate_data_class_Author(self, value):
        if isinstance(value, Author):
            return value
        else:
            raise ValueError('There must be class Author')

    def new_book(self, name, year, author):
        """returns an instance of Book class and adds the book to the books list for the current library."""
        self.validate_data_str(name)
        self.validate_data_int(year)
        self.validate_data_class_Author(author)

        a = Book(name, year, author)
        Library.books.append(a)
        if author not in Library.authors:
            Library.authors.append(author)
        author.add_book_author(a)
        Book.book_count += 1
        print(f'New book added: {a}')

    def __repr__(self):
        return f'{self.name}'

    def __str__(self):
        return f'{self.name}'

    def group_by_author(self, author):
        """returns a list of all books grouped by the specified author"""
        if isinstance(author, Author):
            print(author.get_book_author())

    def group_by_year(self, year):
        """returns a list of all the books grouped by the specified year"""
        self.if_list_empty(Library.books)
        self.validate_data_int(year)
        for book in Library.books:
            if year == book.year:
                print(book)


library = Library('The Great Library')

pushkin = Author('Pushkin', 'Russia', 1799)
gogol = Author('Gogol', 'Ukraine', 1809)
tolstoy = Author('Tolstoy', 'Russia', 1828)

library.new_book('War or peace', 1867, tolstoy)
library.new_book('Hadgy-Murat', 1912, tolstoy)

library.new_book('Dead souls', 1842, gogol)
library.new_book('Taras Bulba', 1842, gogol)

library.new_book('Captain\'s daughter', 1836, pushkin)
library.new_book('Ruslan and Ludmila', 1820, pushkin)

# print(Book.book_count)
# print(Library.authors)
# print(Library.books)
#
# library.group_by_author(gogol)
# library.group_by_author(pushkin)
# library.group_by_author(tolstoy)
#
# library.group_by_year(1820)
# library.group_by_year(1836)
# library.group_by_year(1842)


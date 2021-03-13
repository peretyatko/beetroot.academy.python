'''Task 2
Library
Write a class structure that implements a library. Classes:
1) Library - name, books = [], authors = []
2) Book - name, year, author (author must be an instance of Author class)
3) Author - name, country, birthday, books = []
Library class
Methods:
- new_book(name: str, year: int, author: Author) - returns an instance of Book class and adds the book to the books list for the current library.
- group_by_author(author: Author) - returns a list of all books grouped by the specified author
- group_by_year(year: int) - returns a list of all the books grouped by the specified year
All 3 classes must have a readable __repr__ and __str__ methods.
Also, the book class should have a class variable which holds the amount of all existing books
class Library:
    pass
class Book:
    pass
class Author:
    pass'''

# Пока не могу понять в каком классе какой метод вызвать запуталась

class Library:
    books = []
    authors = []
    name = str

    def __init__(self, name):
        self.name = name




    def __repr__(self):
        return (self.books + ',' + str(self.year) + ',' + self.author)

    def __str__(self):
        return (self.books + ',' + str(self.year) + ',' + self.author)


class Book(Library):
    def __init__(self, name, year, Author):
        super().__init__(name)
        self.name = name
        self.year = year

        book = [self.name, self.year, Author]
        Library.books.append(book)


class Author(Book):

    def __init__(self, name, country, birthday):
        super().__init__(name, country, birthday)
        self.birthday = birthday
        self.country = country

    def new_book(self):
        books

    # def books_by_author(self):
    #     books_by_author = []
    #     books_by_author.append()




    def __repr__(self):
        return (self.books + ',' + str(self.year) + ',' + self.author)

    def __str__(self):
        return (self.books + ',' + str(self.year) + ',' + self.author)


Author('Joseph Gallian', 'USA', 1941)
Book('Contemporary Abstract Algebra', 1974, 'Joseph Gallian')

print(repr(Library.books))


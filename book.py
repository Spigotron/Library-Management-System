# This module contains the Book class and its subclasses.

class Book():
    def __init__(self, title, author, isbn, genre, publication_date):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.genre = genre
        self.publication_date = publication_date
        self.available = True
    
    def check_out(self):
        if self.available:
            self.available = False
            return True
        return False
    
    def make_book_available(self):
        self.available = True

class Fiction(Book):
    def __init__(self, genre):
        self.genre = "Fiction"

class NonFiction(Book):
    def __init__(self, genre):
        self.genre = "Non-fiction"

class Mystery(Book):
    def __init__(self, genre):
        self.genre = "Mystery"
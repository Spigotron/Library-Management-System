# This module contains the User class.

class User():
    def __init__(self, name, library_id):
        self.name = name
        self.__library_id = library_id
        self.borrowed_books = []

    def get_library_id(self):
        return self.__library_id
    
    def set_library_id(self, new_library_id):
        self.__library_id = (new_library_id)

    def borrow_book(self, book):
        self.borrowed_books.append(book)

    def return_book(self, book):
        self.borrowed_books.remove(book)
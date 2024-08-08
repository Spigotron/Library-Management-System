# This module contains the Library class and all of the core functions of the Library Management System.

from book import Book
from user import User
from author import Author

class Library():
    def __init__(self):
        self.books = []
        self.users = []
        self.authors = []

    def add_book(self):
        title = input("Enter the title of the book: ")
        author = input("Enter the author of the book: ")
        isbn = input("Enter the ISBN of the book: ")
        genre = input("Enter the genre of the book: ")
        publication_date = input("Enter the publication date of the book: ")
        new_book = Book(title, author, isbn, genre, publication_date)
        self.books.append(new_book)
        print(f"{new_book.title} has been added to the library.")

    def borrow_book(self, title):
        listed_book = self.find_book(title)
        if listed_book and listed_book.check_out():
            user = input("Enter the name of the user who is borrowing the book: ")
            user_not_found = True
            for listed_user in self.users:
                if user == listed_user.name:
                    user_not_found = False
                    listed_user.borrow_book(listed_book)
                    print(f"{title} has been checked out by {listed_user.name}.")
            if user_not_found:
                print(f"Sorry, {listed_user.name} is not a library user.")
        else:
            print(f"Sorry, {title} is not available to be checked out.")

    def return_book(self, title):
            listed_book = self.find_book(title)
            if listed_book:
                user = input("Enter the name of the user who is returning the book: ")
                user_not_found = True
                for listed_user in self.users:
                    if user == listed_user.name:
                        user_not_found = False
                        listed_user.return_book(listed_book)
                        listed_book.make_book_available()
                        print(f"{listed_book.title} has been returned by {listed_user.name}")
                if user_not_found:
                    print(f"Sorry, {listed_user.name} is not a library user.")
            else:
                print(f"Sorry, {listed_book.title} is not in the library")

    def find_book(self, title):
        if not self.books:
            print(f"Sorry, there are no books in the library.")
        for listed_book in self.books:
            if listed_book.title == title:
                print(f"Title: {listed_book.title}\nAuthor: {listed_book.author}\nISBN: {listed_book.isbn}\nGenre: {listed_book.genre}\nPublication Date: {listed_book.publication_date}\nAvailable: {listed_book.available}")
                return listed_book
            else:
                print(f"Sorry, {title} is not in the library.")

    def display_all_books(self):
        if not self.books:
            print(f"Sorry, there are no books in the library.")
        else:
            print(f"Here is a list of all the books in the library:")
            for listed_book in self.books:
                    print(f"Title: {listed_book.title}")
                    print(f"\tAuthor: {listed_book.author}")
                    print(f"\tISBN: {listed_book.isbn}")
                    print(f"\tGenre: {listed_book.genre}")
                    print(f"\tPublication Date: {listed_book.publication_date}")
                    print(f"\tAvailable: {listed_book.available}")

    def add_user(self):
        name = input("Enter the user's name: ")
        library_id = input("Enter the user's library ID: ")
        new_user = User(name, library_id)
        self.users.append(new_user)
        print(f"{new_user.name} has been added to the list of library users.")

    def view_user_details(self, name):
        if not self.users:
            print(f"Sorry, there are no library users in the system.")
        for listed_user in self.users:
            if listed_user.name == name:
                print(f"Name: {listed_user.name}\nLibrary ID: {listed_user.get_library_id()}\nBorrowed Books:")
                for book in listed_user.borrowed_books:
                    print(f"\tTitle: {book.title}")
                    print(f"\tAuthor: {book.author}")
                    print(f"\tISBN: {book.isbn}")
                    print(f"\tGenre: {book.genre}")
                    print(f"\tPublication Date: {book.publication_date}")
                return listed_user
            else:
                print(f"Sorry, {name} is not a library user.")

    def display_all_users(self):
        if not self.users:
            print(f"Sorry, there are no library users in the system.")
        else:
            print(f"Here is a list of all the library users:")
            for listed_user in self.users:
                print(f"Name: {listed_user.name}\nLibrary ID: {listed_user.get_library_id()}\nBorrowed Books:")
                for book in listed_user.borrowed_books:
                    print(f"\tTitle: {book.title}")
                    print(f"\tAuthor: {book.author}")
                    print(f"\tISBN: {book.isbn}")
                    print(f"\tGenre: {book.genre}")
                    print(f"\tPublication Date: {book.publication_date}")

    def add_author(self):
        name = input("Enter the author's name: ")
        biography = input("Enter the title of the author's biography: ")
        new_author = Author(name, biography)
        self.authors.append(new_author)
        print(f"{new_author.name} has been added to the list of authors.")

    def view_author_details(self, name):
        if not self.authors:
           print(f"Sorry, there are no authors in the system.")
        else:
            for listed_author in self.authors:
                if listed_author.name == name:
                    print(f"Name: {listed_author.name}")
                    print(f"Biography: {listed_author.biography}")
                else:
                    print(f"Sorry, {name} is not in the system.")

    def display_all_authors(self):
        if not self.authors:
            print(f"Sorry, there are no authors in the system.")
        else:
            print(f"Here are all the authors in our database:")
            for listed_author in self.authors:
                print(f"Name: {listed_author.name}")
                print(f"\tBiography: {listed_author.biography}")
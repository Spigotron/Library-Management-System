# This module is the "base of operations" for the Library Management System.

from library import Library

def lms():
    library = Library()

    while True:
        main_menu = input("""
                    
        Welcome to the Library Management System!

        Main Menu:
                            
        1. Book Operations
        2. User Operations
        3. Author Operations
        4. Quit

        Enter a selection: """)
        
        if main_menu == "1":
            book_menu_completed = False
            while not book_menu_completed:
                book_menu = input("""
                                    
                Book Operations:
                                    
                1. Add a new book
                2. Borrow a book
                3. Return a book
                4. Search for a book
                5. Display all books
                                    
                Enter a selection: """)
                    
                if book_menu == "1":
                    library.add_book()
                elif book_menu == "2":
                    library.borrow_book(input("Enter the title of the book you would like to borrow: "))
                elif book_menu == "3":
                    library.return_book(input("Enter the title of the book you would like to return: "))
                elif book_menu == "4":
                    library.find_book(input("Enter the title of the book you would like to find: "))
                elif book_menu == "5":
                    library.display_all_books()
                else:
                    print("Sorry, that is not a valid selection.")
                book_menu_completed = True

        elif main_menu == "2":
            user_menu_completed = False
            while not user_menu_completed:
                user_menu = input("""
                    
                User Operations:
                                  
                1. Add a new user
                2. View user details
                3. Display all users
                                    
                Enter a selection: """)

                if user_menu == "1":
                    library.add_user()
                elif user_menu == "2":
                    library.view_user_details(input("Enter the name of the user whose details you would like to view: "))
                elif user_menu == "3":
                    library.display_all_users()
                else:
                    print("Sorry, that is not a valid selection.")
                user_menu_completed = True
                
        elif main_menu == "3":
            author_menu_completed = False
            while not author_menu_completed:
                author_menu = input("""
                                    
                Author Operations:
                                    
                1. Add a new author
                2. View author details
                3. Display all authors
                                    
                Enter a selection: """)

                if author_menu == "1":
                    library.add_author()
                elif author_menu == "2":
                    library.view_author_details(input("Enter the name of the author whose details you would live to view: "))
                elif author_menu == "3":
                    library.display_all_authors()
                else:
                    print("Sorry, that is not a valid selection.")
                author_menu_completed = True
        elif main_menu == "4":
            print("Thank you for using the Library Management System. Have a nice day!")
            break
        else:
            print("Sorry, that is not a valid selection..")

lms()
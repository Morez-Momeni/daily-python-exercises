"""
Problem #4: Library Management System (Updated Version)
Date: 2026-02-18

A simple library management system with enhanced functionality:
- Create books with title, author, category, and random ISBN
- Track borrow status
- Add multiple books to library
- Display all books with their authors
- Show all ISBNs
- Search books by author or ISBN with interactive menu
- Check and borrow books by title
"""

import random
import string


class Book:
    
    def __init__(self, title, author, category ,is_borrow = False):
        
        self.title = title
        self.author = author
        self.isbn = "".join(random.choices(string.ascii_letters, k=10))
        self.is_borrow = is_borrow
        self.category = category



class Library:
    
    def __init__(self):
        
        self.books = []
    def add_books(self,book):
        
        self.books.append(book) 
    
    def show_books(self):

        for book in self.books:
            print(f"Books: {book.title} <---> {book.author}")
    

    def check_lsbn(self):

        for book in self.books:
            print(f"{book.isbn} for book :{book.title}")


    def search (self):
       
        while True:
            
            print("Do you want search with wich options: \n1)author\n2)ISBN\n3)Exit")
            user_choise = int(input("Enter your number : "))
            if user_choise == 1 :
                author_name = input("author name : ").strip().lower()
                for book in self.books:
                    if book.author == author_name:
                        print(f"book name {book.title} and author {book.author} and ISBN is {book.isbn}")

                    else:
                        print("Dosent Exists")
                
                print("\ncontinue ? ")
                yes_or_no = input("yes or no ? ").lower().strip()
                if yes_or_no == "yes":
                        continue
                else:
                    break

            elif  user_choise == 2:
                user_isbn = input("isbn : ").strip()
                for book in self.books:
                    if book.isbn == user_isbn:
                        print(f"book name {book.title} and author {book.author} and ISBN is {book.isbn}")
                    else:
                        print("Dosent Exists")
                
                print("\ncontinue ? ")
                yes_or_no = input("yes or no ? ").lower().strip()
                if yes_or_no == "yes":
                        continue
                else:
                    break
            
            elif user_choise == 3 :

                break

            else:
                print("Invalid number")
                continue
        
    def check_borrow(self):

        book_name = input("Enter book name to check : ").strip().lower()
        for book in self.books:
            if book.title == book_name:
                for i in self.books:
                    if i.is_borrow:
                        return f"The book {i.title} was borrowed"
                    else:
                        print(f"you can borrow book: {i.title}")
                        print("Do you want borrow it?")
                        answer = input("yes/no: ").strip().lower()
                        if answer == "yes":
                            i.is_borrow = True
                            return "you have it"
                        else:
                          return "ok, goodluck"
        else:

            return "wrong name use search method"
        

if __name__ == "__main__":

    my_library = Library()
    
    sample_books = [
        Book("Python Basics", "John Smith", "Programming"),
        Book("Learning OOP", "Jane Doe", "Programming", True), 
        Book("The Alchemist", "Paulo Coelho", "Fiction"),
        Book("Clean Code", "Robert Martin", "Programming"),
        Book("1984", "George Orwell", "Fiction"),
        Book("Sapiens", "Yuval Harari", "History")
    ]
    

    for book in sample_books:
        my_library.add_books(book)
    
    print("=" * 50)
    print("LIBRARY MANAGEMENT SYSTEM")
    print("=" * 50)
    
    my_library.show_books()
    
    my_library.check_isbn()
    
    my_library.search()
    
    print("\n" + "=" * 50)
    print("BORROWING SECTION")
    print("=" * 50)
    result = my_library.check_borrow()
    print(result)





   

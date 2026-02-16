"""
Problem #4: Library Management System
Status: MVP (Minimum Viable Product) - Will be improved over time

A simple library management system with basic functionality:
- Create books with title, author, and random ISBN
- Track borrow status
- Add books to library
- Display all books
- Search books by ISBN
"""

import random
import string


class Book:
    
    def __init__(self, title, author, is_borrow=False):
        
        self.title = title
        self.author = author
        self.isbn = "".join(random.choices(string.ascii_letters, k=10))
        self.is_borrow = is_borrow

    def check_borrow(self):

        if self.is_borrow:
            return f"The book {self.title} was borrowed"
        else:
            print(f"you can borrow book: {self.title}")
            print("Do you want borrow it?")
            answer = input("yes/no: ")
            if answer.lower() == "yes":
                self.is_borrow = True
                return "you have it"
            else:
                return "ok, goodluck"

    def show_isbn(self):
        return f"isbn is {self.isbn}"


class Library:
    
    def __init__(self):

        self.books = []

    def add_book(self, book):
    
        self.books.append(book)

    def show_books(self):
        
        for book in self.books:
            print(book.title + "--->" + "isbn: " + book.isbn)

    def search_book(self, isbn):
        
        for book in self.books:
            if book.isbn == isbn:
                return f"The book is {book.title}"
        return f"book with {isbn} doesn't exist"



if __name__ == "__main__":

    book1 = Book("one", "ali")
    book2 = Book("two", "mohammad", True)
    
    lab = Library()
    lab.add_book(book1)
    lab.add_book(book2)
    
    print("\nAll Books")
    lab.show_books()
    
    print("\nSearch Tests")
    x = book1.isbn
    print(lab.search_book(x))           
    print(lab.search_book("abcdefgh")) 
    
    print("\nBorrow Test")
    print(book1.check_borrow())         
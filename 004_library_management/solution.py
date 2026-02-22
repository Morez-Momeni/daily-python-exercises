"""
Problem #4: Library Management System (Current Version)
Date: 2026-02-22

A simple library management system using modular design.
Books and Users are stored in dictionaries with auto-generated IDs.
Interactive menu allows adding, showing, and removing books.
"""

from books import Book
from users import User
import random
import string



class Library :
    
    def __init__(self):
        
        self.books = {}
        self.users = {}
    
    def add_book(self,book):

        letters = "".join(random.choices(string.ascii_letters,k=10))
        self.books[letters] = book
        return self.books

    def remove_book(self,code):
        
        if self.books.get(code):
            self.books.pop(code)
            
        return self.books

    def show_books(self):

        for i,j in self.books.items():
            print(f"id: {i}, name: {j.title}")


    def add_user(self,user):
        letters = "".join(random.choices(string.ascii_letters,k=10))
        self.users[letters] = user 
        return self.users



lab = Library()

b = Book("Harry Potter","J.K. Rowling","Story")
a = Book("fantastic beats","J.K. Rowling","Story")

while True:
    print("1)add_book\n2)show_book\n3)remove_book\n4)Exit")

    user_choise = int(input("Enter your choise: "))
    if user_choise == 1:
        lab.add_book(a)
        lab.add_book(b)
        print("\ncontinue:  ")
        yes_or_no = input("yes or no ? ").lower().strip()
        if yes_or_no == "yes":
            continue
        else:
            break
    elif user_choise == 2:
        lab.show_books()
        print("\ncontinue:  ")
        yes_or_no = input("yes or no ? ").lower().strip()
        if yes_or_no == "yes":
            continue
        else:
            break
    elif user_choise == 3 :
        book_id = input("Enter book_id: ").strip()
        lab.remove_book(book_id)
        print("\ncontinue:  ")
        yes_or_no = input("yes or no ? ").lower().strip()
        if yes_or_no == "yes":
            continue
        else:
            break
    elif user_choise == 4 :
        break
    else:
        continue



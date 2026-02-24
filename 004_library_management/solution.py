"""
Problem #4: Library Management System (Current Version)
Date: 2026-02-22

A simple library management system using modular design.
Books and Users are stored in dictionaries with auto-generated IDs.
Interactive menu allows adding, showing, and removing books and users.
"""

from books import Book
from users import User
import random
import string
import os


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

        for id,name in self.books.items():
            print(f"id: {id}, name: {name.title}")


    def add_user(self,user):
        letters = "".join(random.choices(string.ascii_letters,k=10))
        self.users[letters] = user 
        return self.users

    def remove_user(self,code):
        
        if self.users.get(code):
            self.users.pop(code)
            
        return self.users

    def show_users(self):

        for id,name in self.users.items():
            print(f"id: {id}, name: {name.name}")
    
    def search(self,name_book):
        flag = False
        for book in self.books.values():
            if book.title == name_book:
                flag = True
        if flag == False:
            return f"{name_book} dosent exists"
        return flag
                
                
        



lab = Library()

while True:
    print('='*20)
    print("1)Add_book\n2)Show_book\n3)Remove_book\n4)Add_user\n5)Show_user\n6)Remove_user\n7)Search\n8)Exit")
    print('='*20)
    user_choise = int(input("Enter your choise: "))
    if user_choise == 1 :
        add_book_number = int(input("Enter number of book you want add: "))
        for un in range(add_book_number):
            title = input(f"{un+1})Book name: ")
            author = input(f"{un+1})Author name: ")
            category = input(f"{un+1})Category: ")
            book = Book(title,author,category)
            lab.add_book(book)
            print('='*20)
        
        print('='*20)
        print("\ncontinue:  ")
        yes_or_no = input("yes or no ? ").lower().strip()
        if yes_or_no == "yes":
            os.system("cls")
            continue
        else:
            break
    elif user_choise == 2 :
        lab.show_books()
        print('='*20)
        print("\ncontinue:  ")
        yes_or_no = input("yes or no ? ").lower().strip()
        if yes_or_no == "yes":
            os.system("cls")
            continue
        else:
            break
    elif user_choise == 3 :
        print('='*20)
        book_id = input("Enter book_id: ").strip()
        lab.remove_book(book_id)
        print('='*20)
        print("\ncontinue:  ")
        yes_or_no = input("yes or no ? ").lower().strip()
        if yes_or_no == "yes":
            os.system("cls")
            continue
        else:
            break
    elif user_choise == 4 :
        add_user_number = int(input("Enter number of user you want add: "))
        for un in range(add_user_number):
            name = input(f"{un+1})User name: ")
            lastname = input(f"{un+1})User last-name: ")
            age = int(input(f"{un+1})age: "))
            n_id = int(input("Enter user national id: "))
            user = User(name,lastname,age,n_id)
            lab.add_user(user)
            print('='*20)
        print('='*20)
        print("\ncontinue:  ")
        yes_or_no = input("yes or no ? ").lower().strip()
        if yes_or_no == "yes":
            os.system("cls")
            continue
        else:
            break
    elif user_choise == 5 :
        lab.show_users()
        print('='*20)
        print("\ncontinue:  ")
        yes_or_no = input("yes or no ? ").lower().strip()
        if yes_or_no == "yes":
            os.system("cls")
            continue
        else:
            break
        
    elif user_choise == 6 :
        print('='*20)
        user_id = input("Enter user_id: ").strip()
        lab.remove_user(user_id)
        print('='*20)
        print("\ncontinue:  ")
        yes_or_no = input("yes or no ? ").lower().strip()
        if yes_or_no == "yes":
            os.system("cls")
            continue
        else:
            break
    elif user_choise == 7 :
        book_name = input("Enter book name: ").lower().strip()
        print(lab.search(book_name))
        print('='*20)
        print("\ncontinue:  ")
        yes_or_no = input("yes or no ? ").lower().strip()
        if yes_or_no == "yes":
            os.system("cls")
            continue
        else:
            break
    
    elif user_choise == 8 :
        break
    
    else:
        continue



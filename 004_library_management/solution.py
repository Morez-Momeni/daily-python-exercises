"""
Problem #4: Library Management System 


 simple library management system with enhanced functionality:
- Create books with title, author, category, and random ISBN
- Track borrow status
- Add multiple books to library
- Display all books with their authors
- Show all ISBNs
- Search books by author, ISBN, or title with interactive menu
- List all available (not borrowed) books

Current version improvements:
- Fixed check_borrow: now lists all books that are available for borrowing
- Search menu improved with flag variables and proper "not found" messages
- Input normalization with .strip().lower() for consistency

"""

import random
import string


class Book:
    
    def __init__(self, title, author, category ,is_borrow = False):
        
        self.title = title.strip().lower()
        self.author = author.strip().lower()
        self.isbn = "".join(random.choices(string.ascii_letters, k=10))
        self.is_borrow = is_borrow
        self.category = category.strip().lower()



class Library:
    
    def __init__(self):
        
        self.books = []
    def add_books(self,book):
        
        self.books.append(book) 
    
    def show_books(self):

        for book in self.books:
            print(f"Books: {book.title} <---> {book.author}")
    

    def check_isbn(self):

        for book in self.books:
            print(f"{book.isbn} for book :{book.title}")


    def search (self):
       
        while True:
            
            print("Do you want search with wich options: \n1)Author\n2)ISBN\n3)Book name\n4)Exit")
            user_choise = int(input("Enter your number : "))
            if user_choise == 1 :
                
                flag = False
                author_name = input("author name : ").strip().lower()
                for book in self.books:
                    if book.author == author_name:
                        print(f"book name {book.title} and author {book.author} and ISBN is {book.isbn}")
                        flag = True
                    else:
                        continue
                else:
                    if flag == False:
                        print("dosent exist")
                 
                print("\ncontinue ? ")
                yes_or_no = input("yes or no ? ").lower().strip()
                if yes_or_no == "yes":
                        continue
                else:
                    break

            elif  user_choise == 2:
                flag = False
                user_isbn = input("isbn : ").strip()
                for book in self.books:
                    if book.isbn == user_isbn:
                        print(f"book name {book.title} and author {book.author} and ISBN is {book.isbn}")
                        flag = True
                    else:
                        continue
                if flag == False:
                    print("dosent exist")
                    
                print("\ncontinue ? ")
                yes_or_no = input("yes or no ? ").lower().strip()
                if yes_or_no == "yes":
                        continue
                else:
                    break
            
            elif user_choise == 3 :
                flag = False
                book_name = input("book name : ").strip().lower()
                for book in self.books:
                    if book.title == book_name:
                        print(f"book name {book.title} and author {book.author} and ISBN is {book.isbn}")
                        flag = True
                    else:
                        continue
                if flag == False:
                    
                    print("dosent exist")
                    
                
                print("\ncontinue ? ")
                yes_or_no = input("yes or no ? ").lower().strip()
                if yes_or_no == "yes":
                        continue
                else:
                    break
            
            elif user_choise == 4 :

                break
            else:
                print("Invalid number")
                continue
        
    def check_borrow(self):
        flag = False
        not_borrow = []
        for book in self.books:
            if book.is_borrow == False:
                not_borrow.append(book.title)
                flag = True
        if flag == False:
            text = "all book was borrowed"
            return text
        
        for sh in range(len(not_borrow)):
            print(f"{sh+1}){not_borrow[sh]}")
        

if __name__ == "__main__":

    my_library = Library()
    
    sample_books = [
        Book("Python Basics", "John Smith", "Programming"),
        Book("Learning OOP", "Jane Doe", "Programming", True), 
        Book("The Alchemist", "Paulo Coelho", "Fiction"),
        Book("Clean Code", "Robert Martin", "Programming"),
        Book("1984", "George Orwell", "Fiction"),
        Book("Sapiens", "Yuval Harari", "History"),
        Book("mio", "Yuval Harari", "History"),
        Book("mio", "Yuval Harari", "History"),
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
    my_library.check_borrow()
    





   

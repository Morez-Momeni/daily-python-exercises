# Problem 4: Library Management System

## Project Overview
This is a beginner-friendly library management system built with Python. It demonstrates basic object-oriented programming concepts and serves as a foundation for a more advanced system.

**This is simple version** – a working prototype that will be improved over time as I learn more.

---

## Current Features
- Create books with title, author, and random ISBN
- Track whether a book is borrowed
- Add books to a library collection
- Display all books in the library
- Search for a book by ISBN
- Simple borrow functionality with user input

---

## Class Design

### `Book` Class
| Method | What it does |
|--------|--------------|
| `__init__(title, author, is_borrow)` | Creates a new book with random ISBN |
| `check_borrow()` | Checks status and handles borrowing |
| `show_isbn()` | Returns the ISBN |

### `Library` Class
| Method | What it does |
|--------|--------------|
| `__init__()` | Creates an empty library |
| `add_book(book)` | Adds a book to the collection |
| `show_books()` | Displays all books |
| `search_book(isbn)` | Finds a book by ISBN |

---

## What I Learned

### Object-Oriented Programming Basics
- Creating classes with `__init__` constructor
- Defining methods that operate on object data
- Using `self` to access instance attributes

### Random Data Generation
- Using `random.choices()` and `string.ascii_letters` to generate random ISBNs
- Good enough for simulation, but real ISBNs follow specific rules

### List Management
- Storing objects in a list (`self.books = []`)
- Iterating through objects and accessing their attributes

### User Interaction
- Simple input/output flow in `check_borrow()` method
- Making decisions based on user response

---

## Current Limitations 

1. **No data persistence** – Books disappear when program ends
2. **Simple search** – Only searches by ISBN, not by title/author
3. **Borrow logic inside Book class** – Should be handled by Library
4. **No duplicate checking** – Same book can be added multiple times
5. **Random ISBNs** – Not realistic, may have collisions
6. **No error handling** – User input is not validated
7. **Mixed responsibilities** – Book class handles borrowing UI

---

## Future Improvements

- [ ] Save/load data to JSON file
- [ ] Add search by title and author
- [ ] Move borrow logic to Library class
- [ ] Prevent duplicate books
- [ ] Generate proper ISBN format
- [ ] Add input validation
- [ ] Create separate files for each class
- [ ] Add member registration
- [ ] Implement return book functionality
- [ ] Add due dates and fine calculation
- [ ] Create a proper CLI menu

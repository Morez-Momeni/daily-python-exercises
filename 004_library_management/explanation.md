# Project 4: Library Management System 

## Project Overview

A simple, modular library management system built with Python. This project demonstrates:

- Object‑oriented programming with separate classes for Book and User.

- Dictionary‑based storage with auto‑generated IDs.

- A basic CLI menu to add, view, and remove books and users.

> (2026‑02‑24) - now includes book search and screen management.
---

## Features 

- **Add books** 
- **Show books** 
- **Remove books** 
- **Add users** 
- **Show users** 
- **Remove users**
- **Search books** 
- **Modular design**  

---
## How to Run
- Place main.py, books.py, and users.py in the same folder.
- Run the main script:

``` python
python main.py

```
---
## Class Design (Library)

| # | Method       | Description                | 
|---|------------|------------------------|
| 1 | **__init__()** | Initialises empty dictionaries for books and users.    |      
| 2 | **add_book(book)** | Adds a book with a random ID. |
| 3 | **remove_book(code)** | Removes a book by its ID (safe existence check). |
| 4 | **show_books()** | Prints all books with their IDs and titles. |
| 5 | **add_user(user)** | Adds a user with a random ID. |
| 6 | **remove_user(code)** | Removes a user by ID. |
| 7 | **show_users()**| Prints all users with their IDs and names. |
| 8 | **search(name_book)** | Returns True if a book with the given title exists, otherwise a message. |

---

**This is simple version** – a working prototype that will be improved over time as I learn more.
> (Updated: 2026-02-24) 

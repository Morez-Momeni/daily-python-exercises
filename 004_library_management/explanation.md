# Project 4: Library Management System 

## Project Overview
This is a simple library management system built with Python, designed as a beginner-friendly project to practice object-oriented programming. The system allows adding books, searching by author, ISBN, or title, viewing all books, and borrowing them. This version focuses on improving the search functionality and user interaction.

---

## Features 

- **Book creation** with title, author, category, and a randomly generated ISBN.
- **Borrow status** tracking (is_borrow flag).
- **Add multiple books** to the library.
- **Display all books** with their titles and authors.
- **Show all ISBNs** with corresponding book titles.
- **Interactive search menu** allowing searches by:
  - Author name (case‑insensitive, shows all matching books)
  - ISBN (exact match)
  - Book title (case‑insensitive, shows all matching books)
- **Borrow functionality** – check availability by book title and borrow if available 

---

## Class Design

### `Book` Class
| Attribute | Description |
|-----------|-------------|
| `title`   | Book title (stripped and lowercased) |
| `author`  | Author name (stripped and lowercased) |
| `category`| Genre/category (stripped and lowercased) |
| `isbn`    | Random 10‑character string |
| `is_borrow` | `True` if borrowed, `False` otherwise |

### `Library` Class
| Method | Description |
|--------|-------------|
| `__init__()` | Initialises an empty book list |
| `add_books(book)` | Adds a `Book` object to the collection |
| `show_books()` | Prints all books with title and author |
| `check_Isbn()` | Lists every ISBN with its book title |
| `search()` | Interactive menu to search by author, ISBN, or title |
| `check_borrow()` | **New** Lists all available (not borrowed) books |

---

## What's New 

- **Title search added** – users can now search by book title.
- **Fixed the "d" bug** – previously the `for...else` structure always printed an unwanted message. Now a `flag` variable ensures messages appear only when appropriate.
- **Improved input handling** – all user inputs are stripped and lowercased for consistent matching.
- **Better user flow** – after each search, the user is asked whether to continue, making the interaction smoother.
- **Error handling for menu input** – a `try-except` prevents crashes on non‑numeric input.

---

**This is simple version** – a working prototype that will be improved over time as I learn more.
> (Updated: 2026-02-19) 

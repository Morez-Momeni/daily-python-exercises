# Problem 4: Library Management System

## Project Overview
This is a beginner-friendly library management system built with Python. It demonstrates basic object-oriented programming concepts and serves as a foundation for a more advanced system.


---

## Current Features
- Create books with title, author, category, and a randomly generated ISBN.
- Track whether a book is borrowed
- Add books to a library collection
- Display all books in the library
- View all ISBNs alongside their corresponding book titles.
- Interactive search menu allowing searches by: Author name and ISBN
- Borrow functionality – check availability by book title and borrow if available.

---

## Class Design

### `Book` Class
| Attribute | Description |
|--------|--------------|
| `title`| Title of the book |
| `author` | Author's name |
| `category` | Returns the ISBN |
| `is_borrow` | True if borrowed, False otherwise |
| `isbn` | Random 10‑character string (simulated) |

### `Library` Class
| Method | What it does |
|--------|--------------|
| `__init__()` | Creates an empty library |
| `add_books(book)` | Adds a book to the collection |
| `show_books()` | Displays all books |
| `search()` | Provides an interactive menu to search by author or ISBN |
| `check_isbn()` | Lists every ISBN with its corresponding book title |
| `check_borrow()` | Prompts for a book title, checks availability, and allows borrowing |

---

**This is simple version** – a working prototype that will be improved over time as I learn more.
> (Updated: 2026‑02‑18)

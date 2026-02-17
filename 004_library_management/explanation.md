# Problem 4: Library Management System

## Project Overview
This is a beginner-friendly library management system built with Python. It demonstrates basic object-oriented programming concepts and serves as a foundation for a more advanced system.


---

## Current Features

### Book Class
- Title, author, category, and ISBN (randomly generated)
- Borrow status tracking

### Library Class
- Add multiple books to collection
- Display all books with details
- Show ISBN registry
- **Interactive search** by:
  - Author name
  - ISBN
- **Borrow functionality** with availability check
- User-friendly menu system

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

## What's New In (Updated: 2026‑02‑18)

### Improvements from Previous Version
1. **Added book category**
2. **Enhanced search functionality** 
3. **Better user experience** 
4. **Improved error handling** 
5. **Case-insensitive search** 
6. **Multiple search attempts** 

---

###  New Methods Added
- `check_isbn()` 
- Improved `search()` 
- Enhanced `check_borrow()` 

---
**This is simple version** – a working prototype that will be improved over time as I learn more.
> (Updated: 2026‑02‑18)

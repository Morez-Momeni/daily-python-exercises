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
1. **Added book category** – More detailed book information
2. **Enhanced search functionality** – Interactive menu with multiple options
3. **Better user experience** – Clear prompts and feedback messages
4. **Improved error handling** – Prevents crashes from invalid input
5. **Empty collection handling** – Graceful messages when no books exist
6. **Case-insensitive search** – More user-friendly
7. **Multiple search attempts** – Users can search repeatedly without restarting
8. **Visual enhancements** – Emojis and formatting for better readability

###  New Methods Added
- `check_isbn()` – Separate method to view all ISBNs
- Improved `search()` with interactive menu
- Enhanced `check_borrow()` with better user feedback

---




---
**This is simple version** – a working prototype that will be improved over time as I learn more.
> (Updated: 2026‑02‑18)

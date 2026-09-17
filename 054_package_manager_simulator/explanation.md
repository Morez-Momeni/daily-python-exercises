## Problem
Build a simple **package manager simulator** on top of a doubly linked list. Each node represents a package with:

- `filename` – the name of the package.
- `size` – the size of the package (in some unit).
- `status` – `True` if downloaded, `False` otherwise.
- `next` / `prev` – linked list pointers.

The manager (`MorezPkgManager`) should support:
- **add** – append a new package.
- **delete** – remove a package by name.
- **complete** – mark a package as downloaded.
- **display** – print all packages with their download status.
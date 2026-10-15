# Problem 72: Recursive File Finder

## Problem
Write a program that recursively searches a directory tree for a file with a given name and returns a list of all paths where that file was found.

**Input:**
- A directory path
- A target filename

**Output:**
- A list of full paths (strings) to every matching file.

## My Solution

I used `os.listdir()` and `os.path.isdir()` to traverse the directory tree recursively.
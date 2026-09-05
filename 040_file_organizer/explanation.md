# Problem 40: Automatic File Organizer

## Problem
Write a script that automatically organizes files in a directory (e.g., Downloads) by moving them into subfolders based on their file extensions. The script should create category folders (Documents, Images, Videos, etc.) and move each file into the appropriate folder.

## My Solution (Current Version)

I used `pathlib` to traverse the directory, check file extensions against a predefined dictionary, and move files accordingly using the `move_into()` method.
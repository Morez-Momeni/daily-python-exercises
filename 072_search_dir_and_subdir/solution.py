"""
Problem #72: Recursive File Finder
Date: 2026-10-16

Recursively searches a directory tree for a file with a given name
and returns a list of full paths where it was found.
"""

import os


def is_directory(parent_path, entry_name):
    if os.path.isdir(f"{parent_path}/{entry_name}"):
        return True
    return False


def find_file(directory_path, target_filename):
    directory_contents = os.listdir(directory_path)

    result_paths = []
    subdirectories = []
    filenames = []

    for entry in directory_contents:
        if is_directory(directory_path, entry):
            subdirectories.append(entry)
        else:
            filenames.append(entry)

    if target_filename in filenames:
        result_paths.append(f"{directory_path}/{target_filename}")

    for subdirectory in subdirectories:
        current_path = f"{directory_path}/{subdirectory}"

        if target_filename in os.listdir(current_path):
            result_paths.append(f"{current_path}/{target_filename}")

        for entry in os.listdir(current_path):
            if is_directory(current_path, entry):
                nested_path = f"{current_path}/{entry}"
                result_paths.extend(find_file(nested_path, target_filename))

    return result_paths


directory_path = input("Enter directory path: ")
target_filename = input("Enter filename: ")

print(find_file(directory_path, target_filename))
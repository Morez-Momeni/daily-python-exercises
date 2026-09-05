"""
Problem #40: Automatic File Organizer
Date: 2026-09-06

This script scans a directory (e.g., ~/Downloads) and moves files into subfolders
based on their file extensions, using a predefined category mapping.

"""


from pathlib import Path


base_dir = Path(r"/home/morez/Downloads")

target_dir = base_dir / "sorted"

FILE_CATEGORIES = {
    "documents": [
        ".pdf",
        ".doc",
        ".docx",
        ".txt",
        ".md",
        ".rtf",
    ],

    "images": [
        ".jpg",
        ".jpeg",
        ".png",
        ".gif",
        ".webp",
        ".svg",
    ],

    "videos": [
        ".mp4",
        ".mkv",
        ".avi",
        ".mov",
        ".webm",
    ],

    "audio": [
        ".mp3",
        ".wav",
        ".flac",
        ".aac",
        ".ogg",
    ],

    "archives": [
        ".zip",
        ".rar",
        ".7z",
        ".tar",
        ".gz",
        ".bz2",
    ],

    "code": [
        ".py",
        ".js",
        ".ts",
        ".cpp",
        ".c",
        ".h",
        ".java",
        ".rs",
        ".go",
        ".html",
        ".css",
        ".json",
        ".yaml",
        ".yml",
    ],

    "executables": [
        ".exe",
        ".msi",
        ".deb",
        ".rpm",
        ".appimage",
    ],

    "fonts": [
        ".ttf",
        ".otf",
        ".woff",
        ".woff2",
    ],

    "spreadsheets": [
        ".xls",
        ".xlsx",
        ".csv",
    ],

    "presentations": [
        ".ppt",
        ".pptx",
    ],
}


def create_category_directories():
    for category , _ in FILE_CATEGORIES.items():
        (target_dir / category).mkdir(parents=True , exist_ok=True)


def search_categories_files():
    for file in base_dir.rglob("*"):
        for category, extention in FILE_CATEGORIES.items():
            if file.suffix in extention:
                try:
                    file.move_into(target_dir / category)
                except OSError:
                    pass

create_category_directories()
search_categories_files()
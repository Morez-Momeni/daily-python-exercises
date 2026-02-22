class Book:
    
    def __init__(self, title, author, category ,is_borrow = False):
        
        self.title = title.strip().lower()
        self.author = author.strip().lower()
        self.is_borrow = is_borrow
        self.category = category.strip().lower()


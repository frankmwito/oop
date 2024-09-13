# class Book with attributes title, author and pages. Create instances of the class and print their attributes

class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
        
    def __str__(self):
        return f"Title: {self.title}, Author: {self.author}, Pages: {self.pages}"
        
book1 = Book("Can't hurt me", "David Goggins", 480)
book2 = Book("constitution","kenya", 482)

print(book1)
print(book2)
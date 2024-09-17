# Define a class library that tracks the books available in a library
# create methods add_book() to add books to the library, borrow_book() to borrow books(if available), and return_book() to return a borrowed book.
# use a list to store the books available and a dictionary to track borrowed books.

class Library:
    def __init__(self):
        self.books = []
        self.books1 = {}
        
    def add_book(self, book_name, author, year):
        num_of_books = int(input("Enter the exact amount of books to be added: "))
        for i in range(num_of_books):
            books1 = {"name": book_name, "author": author, "year": year}
            self.books.append(books1)
    def borrow_book(self, borrower_name, book_name):
        found_book = None
        for book in self.books:
            if book["name"].lower() == book_name.lower():
                found_book = book
                break
            
        if found_book:
            self.books.remove(found_book)
            self.books1[book_name] == borrower_name
            print(f'Book "{book_name}" has been borrowed by {borrower_name}.')
        else:
            print(f'Sorry, the book "{book_name}" is either not available or already borrowed.')

                
    
    def return_book(self, book_name):
        """Return a borrowed book."""
        if book_name in self.borrowed_books:
            borrower_name = self.borrowed_books.pop(book_name)
            self.books.append({"name": book_name, "author": "Unknown", "year": "Unknown"})
            print(f'Book "{book_name}" has been returned by {borrower_name}.')
        else:
            print(f'The book "{book_name}" was not borrowed from this library.')

    def show_books(self):
        """Display all available books."""
        if not self.books:
            print("No books are currently available in the library.")
        else:
            print("Available books in the library:")
            for book in self.books:
                print(f'{book["name"]} by {book["author"]} ({book["year"]})')

    def show_borrowed_books(self):
        """Display all borrowed books."""
        if not self.borrowed_books:
            print("No books are currently borrowed.")
        else:
            print("Borrowed books:")
            for book_name, borrower_name in self.borrowed_books.items():
                print(f'{book_name} is borrowed by {borrower_name}')


# Example usage
library = Library()

# Add books to the library
library.add_book(input("Enter the book name: "), input("Enter the author's name: "), int(input("Enter the year: ")))
library.add_book(input("Enter the book name: "), input("Enter the author's name: "), int(input("Enter the year: ")))
library.add_book(input("Enter the book name: "), input("Enter the author's name: "), int(input("Enter the year: ")))

# Show available books
library.show_books()

# Borrow a book
library.borrow_book(input("Enter the book year to borrow: "), input("Enter the borrowers name: "))

# Show available and borrowed books
library.show_books()
library.show_borrowed_books()

# Return a book
library.return_book(input("Enter the book year borrowed: "))

# Show updated lists
library.show_books()
library.show_borrowed_books()              
                

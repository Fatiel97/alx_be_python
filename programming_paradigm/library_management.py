# library_management.py

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False  # Private attribute to track availability

    def check_out(self):
        """Mark the book as checked out."""
        if not self._is_checked_out:
            self._is_checked_out = True
        else:
            raise ValueError(f"'{self.title}' is already checked out.")

    def return_book(self):
        """Mark the book as returned."""
        if self._is_checked_out:
            self._is_checked_out = False
        else:
            raise ValueError(f"'{self.title}' is not checked out.")

    def is_available(self):
        """Return True if the book is available, False otherwise."""
        return not self._is_checked_out

    def __str__(self):
        return f"{self.title} by {self.author}"


class Library:
    def __init__(self):
        self._books = []  # Private list to store books

    def add_book(self, book):
        """Add a book to the library."""
        if isinstance(book, Book):
            self._books.append(book)
        else:
            raise TypeError("Only instances of Book can be added to the library.")

    def check_out_book(self, title):
        """Check out a book by its title."""
        book = self._find_book(title)
        if book and book.is_available():
            book.check_out()
        elif book:
            raise ValueError(f"'{title}' is already checked out.")
        else:
            raise ValueError(f"'{title}' not found in the library.")

    def return_book(self, title):
        """Return a book to the library."""
        book = self._find_book(title)
        if book:
            book.return_book()
        else:
            raise ValueError(f"'{title}' not found in the library.")

    def list_available_books(self):
        """List all available books in the library."""
        available_books = [str(book) for book in self._books if book.is_available()]
        if available_books:
            for book in available_books:
                print(book)
        else:
            print("No available books.")

    def _find_book(self, title):
        """Find and return a book by its title. Return None if not found."""
        for book in self._books:
            if book.title == title:
                return book
        return None

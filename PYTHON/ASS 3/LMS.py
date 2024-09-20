class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_available = True

    def __str__(self):
        return f"{self.title} by {self.author} (ISBN: {self.isbn})"

class Member:
    def __init__(self, name, membership_id):
        self.name = name
        self.membership_id = membership_id
        self.borrowed_books = []

    def __str__(self):
        return f"{self.name} (Membership ID: {self.membership_id})"

class Library:
    def __init__(self):
        self.books = []
        self.members = []

    def add_book(self, book):
        self.books.append(book)

    def register_member(self, member):
        self.members.append(member)

    def borrow_book(self, book, member):
        if book.is_available:
            member.borrowed_books.append(book)
            book.is_available = False
            print(f"{member.name} borrowed {book.title}.")
        else:
            print(f"{book.title} is not available.")

    def return_book(self, book, member):
        if book in member.borrowed_books:
            member.borrowed_books.remove(book)
            book.is_available = True
            print(f"{member.name} returned {book.title}.")
        else:
            print(f"{member.name} does not have {book.title} borrowed.")

    def list_available_books(self):
        print("Available Books:")
        for book in self.books:
            if book.is_available:
                print(book)

    def list_borrowed_books(self, member):
        print(f"{member.name}'s Borrowed Books:")
        for book in member.borrowed_books:
            print(book)

# Create some sample books and members
books = [
    Book("To Kill a Mockingbird", "Harper Lee", "9780446310789"),
    Book("1984", "George Orwell", "9780451524935"),
    Book("Pride and Prejudice", "Jane Austen", "9780553583252"),
    Book("The Great Gatsby", "F. Scott Fitzgerald", "9780743273563"),
    Book("The Lord of the Rings", "J.R.R. Tolkien", "9780547936053")
]

members = [
    Member("Alice Smith", "1234"),
    Member("Bob Johnson", "5678"),
    Member("Charlie Brown", "9012")
]

# Create a library and add books and members
library = Library()
for book in books:
    library.add_book(book)
for member in members:
    library.register_member(member)

# Borrow and return books
library.borrow_book(books[0], members[0])
library.borrow_book(books[1], members[1])
library.borrow_book(books[2], members[0])
library.return_book(books[0], members[0])
library.borrow_book(books[3], members[2])

# List available and borrowed books
library.list_available_books()
library.list_borrowed_books(members[0])
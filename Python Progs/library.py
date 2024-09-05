import datetime

def display_menu():
    print("Library Management System")
    print("1. Add Book")
    print("2. Check Out Book")
    print("3. Return Book")
    print("4. Display Available Books")
    print("5. Display Overdue Books")
    print("6. Display Most Borrowed Books")
    print("7. Quit")

def add_book(books):
    title = input("Enter the book title: ")
    author = input("Enter the author: ")
    books.append({"title": title, "author": author, "checked_out": False, "due_date": None})
    print("Book added successfully!")

def check_out_book(books):
    title = input("Enter the book title: ")
    for book in books:
        if book["title"] == title and not book["checked_out"]:
            book["checked_out"] = True
            book["due_date"] = datetime.datetime.now() + datetime.timedelta(days=14)
            print("Book checked out successfully!")
            return
    print("Book not found or already checked out.")

def return_book(books):
    title = input("Enter the book title: ")
    for book in books:
        if book["title"] == title and book["checked_out"]:
            book["checked_out"] = False
            book["due_date"] = None
            print("Book returned successfully!")
            return
    print("Book not found or not checked out.")

def display_available_books(books):
    print("Available Books:")
    for book in books:
        if not book["checked_out"]:
            print(f"{book['title']} by {book['author']}")

def display_overdue_books(books):
    print("Overdue Books:")
    for book in books:
        if book["checked_out"] and book["due_date"] < datetime.datetime.now():
            print(f"{book['title']} by {book['author']} (Due: {book['due_date'].strftime('%Y-%m-%d')})")

def display_most_borrowed_books(books):
    borrowed_count = {}
    for book in books:
        if book["checked_out"]:
            borrowed_count[book["title"]] = borrowed_count.get(book["title"], 0) + 1
    most_borrowed = max(borrowed_count, key=borrowed_count.get)
    print("Most Borrowed Book:", most_borrowed)

# Sample book data
books = [
    {"title": "To Kill a Mockingbird", "author": "Harper Lee", "checked_out": False, "due_date": None},
    {"title": "1984", "author": "George Orwell", "checked_out": False, "due_date": None},
    {"title": "Pride and Prejudice", "author": "Jane Austen", "checked_out": False, "due_date": None},
    {"title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "checked_out": False, "due_date": None},
    {"title": "The Lord of the Rings", "author": "J.R.R. Tolkien", "checked_out": False, "due_date": None}
]

while True:
    display_menu()
    choice = int(input("Enter your choice: "))

    if choice == 1:
        add_book(books)
    elif choice == 2:
        check_out_book(books)
    elif choice == 3:
        return_book(books)
    elif choice == 4:
        display_available_books(books)
    elif choice == 5:
        display_overdue_books(books)
    elif choice == 6:
        display_most_borrowed_books(books)
    elif choice == 7:
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
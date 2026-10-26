# Library Management System using OOP

class Book:
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.available = True


class Patron:
    def __init__(self, patron_id, name):
        self.patron_id = patron_id
        self.name = name
        self.borrowed_books = []


class Library:
    def __init__(self):
        self.books = []
        self.patrons = []

    # Add a new book
    def add_book(self, book):
        self.books.append(book)
        print("Book added successfully!")

    # Register a new patron
    def register_patron(self, patron):
        self.patrons.append(patron)
        print("Patron registered successfully!")

    # Borrow a book
    def borrow_book(self, patron_id, book_id):
        patron = None
        book = None

        for p in self.patrons:
            if p.patron_id == patron_id:
                patron = p
                break

        for b in self.books:
            if b.book_id == book_id:
                book = b
                break

        if patron is None:
            print("Patron not found!")
        elif book is None:
            print("Book not found!")
        elif not book.available:
            print("Book is already borrowed!")
        else:
            book.available = False
            patron.borrowed_books.append(book)
            print("Book borrowed successfully!")

    # Return a book
    def return_book(self, patron_id, book_id):
        patron = None

        for p in self.patrons:
            if p.patron_id == patron_id:
                patron = p
                break

        if patron is None:
            print("Patron not found!")
            return

        for book in patron.borrowed_books:
            if book.book_id == book_id:
                book.available = True
                patron.borrowed_books.remove(book)
                print("Book returned successfully!")
                return

        print("This book was not borrowed by this patron.")

    # Display all books
    def display_books(self):
        print("\n--- Library Books ---")

        if not self.books:
            print("No books available.")
            return

        for book in self.books:
            status = "Available" if book.available else "Borrowed"
            print(
                f"ID: {book.book_id}, "
                f"Title: {book.title}, "
                f"Author: {book.author}, "
                f"Status: {status}"
            )

    # Display all patrons
    def display_patrons(self):
        print("\n--- Registered Patrons ---")

        if not self.patrons:
            print("No patrons registered.")
            return

        for patron in self.patrons:
            print(
                f"ID: {patron.patron_id}, "
                f"Name: {patron.name}"
            )


# Main Program
library = Library()

while True:
    print("\n===== Library Management System =====")
    print("1. Add Book")
    print("2. Register Patron")
    print("3. Borrow Book")
    print("4. Return Book")
    print("5. Display Books")
    print("6. Display Patrons")
    print("7. Exit")

    try:
        choice = int(input("Enter your choice: "))

        if choice == 1:
            book_id = int(input("Enter Book ID: "))
            title = input("Enter Book Title: ")
            author = input("Enter Author Name: ")

            book = Book(book_id, title, author)
            library.add_book(book)

        elif choice == 2:
            patron_id = int(input("Enter Patron ID: "))
            name = input("Enter Patron Name: ")

            patron = Patron(patron_id, name)
            library.register_patron(patron)

        elif choice == 3:
            patron_id = int(input("Enter Patron ID: "))
            book_id = int(input("Enter Book ID: "))
            library.borrow_book(patron_id, book_id)

        elif choice == 4:
            patron_id = int(input("Enter Patron ID: "))
            book_id = int(input("Enter Book ID: "))
            library.return_book(patron_id, book_id)

        elif choice == 5:
            library.display_books()

        elif choice == 6:
            library.display_patrons()

        elif choice == 7:
            print("Thank you for using the Library Management System!")
            break

        else:
            print("Invalid choice! Please select 1 to 7.")

    except ValueError:
        print("Invalid input! Please enter a valid number.")
from model import Book, Library

def validate_non_empty(prompt):
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("Input cannot be empty!")

def menu():
    print("\n===== Library Management System =====")
    print("1. Add Book")
    print("2. Issue Book")
    print("3. Return Book")
    print("4. Delete Book")
    print("5. View Available Books")
    print("6. Exit")

def print_table(books):
    if not books:
        print("No books found.")
        return

    # Exact header format
    print("\nBook ID  Title                Author          Issued To       Return Status")
    print("--------------------------------------------------------------------------------")

    # Rows
    for book in books:
        issued_to = book.issued_to if book.issued_to else "Available"
        return_status = "Not Returned" if book.issued_to else "--"

        print(f"{book.book_id:<8} "
              f"{book.title:<20} "
              f"{book.author:<15} "
              f"{issued_to:<15} "
              f"{return_status:<15}")

def main():
    library = Library("data.txt")

    while True:
        menu()
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            book_id = validate_non_empty("Enter Book ID: ")
            title = validate_non_empty("Enter Book Title: ")
            author = validate_non_empty("Enter Author Name: ")

            book = Book(book_id, title, author)
            if library.add_book(book):
                print("Book added successfully!")
            else:
                print("Book ID already exists!")

        elif choice == "2":
            book_id = validate_non_empty("Enter Book ID to issue: ")
            student = validate_non_empty("Enter Student Name: ")

            result = library.issue_book(book_id, student)
            if result == "issued":
                print("Book issued successfully!")
            elif result == "already_issued":
                print("Book is already issued!")
            else:
                print("Book not found!")

        elif choice == "3":
            book_id = validate_non_empty("Enter Book ID to return: ")
            result = library.return_book(book_id)

            if result == "returned":
                print("Book returned successfully!")
            elif result == "not_issued":
                print("Book was not issued!")
            else:
                print("Book not found!")

        elif choice == "4":
            book_id = validate_non_empty("Enter Book ID to delete: ")
            if library.delete_book(book_id):
                print("Book deleted successfully!")
            else:
                print("Book not found!")

        elif choice == "5":
            print_table(library.books)

        elif choice == "6":
            print("Exiting program...")
            break

        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
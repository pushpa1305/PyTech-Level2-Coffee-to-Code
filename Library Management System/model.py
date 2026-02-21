class Book:
    def __init__(self, book_id, title, author, issued_to=""):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.issued_to = issued_to


class Library:
    def __init__(self, filename):
        self.filename = filename
        self.books = self.load_books()

    def load_books(self):
        books = []
        try:
            with open(self.filename, "r") as file:
                lines = file.readlines()[2:]  # skip header

                for line in lines:
                    if line.strip():
                        book_id = line[0:8].strip()
                        title = line[8:28].strip()
                        author = line[28:43].strip()
                        issued_to = line[43:58].strip()

                        if issued_to == "Available":
                            issued_to = ""

                        books.append(Book(book_id, title, author, issued_to))
        except FileNotFoundError:
            open(self.filename, "w").close()

        return books

    def save_books(self):
        with open(self.filename, "w") as file:
            file.write("Book ID  Title                Author          Issued To       Return Status\n")
            file.write("--------------------------------------------------------------------------------\n")

            for book in self.books:
                issued_to = book.issued_to if book.issued_to else "Available"
                return_status = "Not Returned" if book.issued_to else "--"

                file.write(f"{book.book_id:<8}{book.title:<20}{book.author:<15}{issued_to:<15}{return_status:<15}\n")

    def add_book(self, book):
        if any(b.book_id == book.book_id for b in self.books):
            return False
        self.books.append(book)
        self.save_books()
        return True

    def issue_book(self, book_id, student_name):
        for book in self.books:
            if book.book_id == book_id:
                if book.issued_to:
                    return "already_issued"
                book.issued_to = student_name
                self.save_books()
                return "issued"
        return "not_found"

    def return_book(self, book_id):
        for book in self.books:
            if book.book_id == book_id:
                if book.issued_to == "":
                    return "not_issued"
                book.issued_to = ""   # Clear issuer
                self.save_books()     # SAVE AFTER CLEARING
                return "returned"
        return "not_found"

    def delete_book(self, book_id):
        for book in self.books:
            if book.book_id == book_id:
                self.books.remove(book)
                self.save_books()
                return True
        return False
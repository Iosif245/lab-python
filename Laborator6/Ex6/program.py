class LibraryItem:
    def __init__(self, title, year):
        self.title = title
        self.year = year
        self.checked_out = False

    def check_out(self):
        if not self.checked_out:
            self.checked_out = True
            return f"{self.title} has been checked out."
        else:
            return f"{self.title} is already checked out."

    def return_item(self):
        if self.checked_out:
            self.checked_out = False
            return f"{self.title} has been returned."
        else:
            return f"{self.title} was not checked out."

class Book(LibraryItem):
    def __init__(self, title, year, author):
        super().__init__(title, year)
        self.author = author

    def display_info(self):
        return f"Book: {self.title}, Author: {self.author}, Year: {self.year}"

class DVD(LibraryItem):
    def __init__(self, title, year, director):
        super().__init__(title, year)
        self.director = director

    def display_info(self):
        return f"DVD: {self.title}, Director: {self.director}, Year: {self.year}"

class Magazine(LibraryItem):
    def __init__(self, title, year, issue_number):
        super().__init__(title, year)
        self.issue_number = issue_number

    def display_info(self):
        return f"Magazine: {self.title}, Issue No.: {self.issue_number}, Year: {self.year}"

book = Book(title="1984", year=1949, author="George Orwell")
dvd = DVD(title="Inception", year=2010, director="Christopher Nolan")
magazine = Magazine(title="National Geographic", year=2023, issue_number=42)

print("Book Information:")
print(book.display_info())
print(book.check_out())
print(book.return_item())

print("\nDVD Information:")
print(dvd.display_info())
print(dvd.check_out())
print(dvd.return_item())

print("\nMagazine Information:")
print(magazine.display_info())
print(magazine.check_out())
print(magazine.return_item())
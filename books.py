class Library:
    def __init__(self, list_of_books):
        self.books = list_of_books

    def display_available_books(self):
        print("Available Books are: ")
        for book in self.books:
            print("  *", book)

    def borrowBooks(self):
        book = input("Enter the book you want to borrow\n")
        if book != "":
            if book in self.books:
                print(f"Congratulations, you have successfully borrowed {book}.")
                self.books.remove(book)
            else:
                print("Sorry the book is not available at the moment")
        else:
            print("Please enter valid name of the book")

    def returnBooks(self):
        book = input("Which book you want to return?\n")
        if book != "":
            self.books.append(book)
            print(f"You have successfully added {book} in the library")
        else:
            print("Please enter valid name of the book")


class Student:
    pass

def Start():
    WRC_Library = Library(["EDC", "DSA", "ECT", "COA", "Data Mining"])
    while True:
        choice = int(input('''
        ---*** Welcome to Library ***---
        Please Enter your Choice
        1. Display Books
        2. Borrow Books
        3. Return Books
        4. Exit
        '''))

        if choice == 1:
            WRC_Library.display_available_books()

        elif choice == 2:
            WRC_Library.borrowBooks()

        elif choice == 3:
            WRC_Library.returnBooks()

        elif choice == 4:
            print("Thanks for visiting our Library...!!!")
            break

        else:
            print("Please enter valid choice...!!!")


Start()
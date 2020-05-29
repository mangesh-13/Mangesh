'''
Create a menu driven program for library management. It will include 6 options :-
    1 - student registration
    2 - lend book to student
    3 - return book to library
    4 - display available books
    5 - display all books issued to students
    6 - exit
We will have 2 classes, i.e student and library. These class will have following mandatory methods.
Student class will have methods registration, requestBook and returnBook
Library class will have methods displayAllBooks, lendBook,addNewBook
(If required, you can write additional methods as well.)
'''
import sys
class Library:
    issued_books=[]
    def __init__(self,totalNoOfBooks):
        self.totalNoOfBook=totalNoOfBooks

    def displayAllBooks(self):
        if self.totalNoOfBook != []:
            for i in self.totalNoOfBook:
                print(i)
        else:
            print("All books are issued")

    def lendBook(self,book):

        if book not in self.totalNoOfBook and self.totalNoOfBook==[]:
            print("All books are issued.Please Try after some time !!")

        else:
            self.totalNoOfBook.remove(book)
            Library.issued_books.append(book)

    def Book_issued(self):

        if Library.issued_books != []:
            print("The issued books are:")
            for i in Library.issued_books:
                print(i)
        else:
            print("No Books issued")

    def addNewBook(self,retuned_book):
        self.totalNoOfBook.append(retuned_book)
        print("The book returned to the library is:",retuned_book)

class Student:
    def __init__(self,students):
        self.students=students

    def registration(self):
        student=input("Enter student name:")

        if student in self.students:
            print("You are allowed to issue the book.")
        else:
            print("You are not a valid student")
            sys.exit()

    def requestBook(self):
        self.registration()
        print("Enter the name of the book you want to issue:")
        self.book=input()
        return self.book

    def returnBook(self):
        if Library.issued_books != [] :
            print("Enter the book you have to return:")
            self.book=input()

            if self.book in Library.issued_books:
                Library.issued_books.remove(self.book)
                return self.book
            else:
                print("This is not our Library book.Please enter the correct Book.")
                # sys.exit()
                return(self.returnBook())

        else:
            print("First issue book from Library.")
            sys.exit()




List_of_books=["Physics","Mathematics","Java","Python","R programming"]
List_of_registered_students=["Mangesh","Mukund","Dinesh","Mayur","Rahul","Nikhil"]
l=Library(List_of_books)
s=Student(List_of_registered_students)

while True:
    print("Enter the operation you want to perform:\n1 - student registration\n2 - lend book to student\n3 - return book to library\n4 - display available books\n5 - display all books issued to students\n6 - exit")
    option=int(input("Choose the correct option:"))
    if option == 1 :
        s.registration()
        pass

    elif option == 2:

        l.lendBook(s.requestBook())

    elif option == 3:
        l.addNewBook(s.returnBook())

    elif option == 4:
        l.displayAllBooks()

    elif option == 5:
        l.Book_issued()

    elif option == 6:
        print("Thanks for visiting library!!!")
        sys.exit()
    else:
        print("Please provide the correct option")



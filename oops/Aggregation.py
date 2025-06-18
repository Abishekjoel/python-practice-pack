class library:
    def __init__(self,name):
        self.name=name
        self.books=[]

    def add_book(self,book):
        self.books.append(book)

    def list_books(self):
        return [f"{book.title},{book.pages}" for book in self.books]

class book:
    def __init__(self,title,pages):
        self.title=title
        self.pages=pages

lib=library("THE GREAT LIBRARY")

book1=book("Harry Potter",206)
book2=book("Intersteller",307)
book3=book("The Hobbit",432)

lib.add_book(book1)
lib.add_book(book2)
lib.add_book(book3)

print(lib.name)
print(lib.list_books())
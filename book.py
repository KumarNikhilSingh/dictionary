class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages


    def book(self):
        print(f"The {self.title} Book which is written by {self.author} contains {self.pages} pages.")

book = Book("Five Point Someone", "Chetan Bhagat", 270)
book.book()
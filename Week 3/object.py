class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def display(self):
        print(f"{self.title} by {self.author}")

my_book = object.__new__(Book)
my_book.__init__("1984", "George Orwell")
my_book.display()

another_book = Book("Dune", "Frank Herbert")
another_book.display()
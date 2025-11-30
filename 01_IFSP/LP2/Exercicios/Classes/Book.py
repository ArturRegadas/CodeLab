class Book:
    def __init__(self, title: str, author: str, num_pages: int):
        self.title = title
        self.author = author
        self.num_pages = num_pages

    def details(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Pages: {self.num_pages}")
        print("-" * 30)


books = [
    Book("The Hobbit", "J.R.R. Tolkien", 310),
    Book("1984", "George Orwell", 328),
    Book("Dom Casmurro", "Machado de Assis", 256)
]

for b in books:
    b.details()

from database import Database
from model import BookModel

db = Database(database="S201", collection="livros")
db.resetDatabase()
book_model = BookModel(db)

# Create book:
id_book01 = book_model.create_book("The Little Prince", "Antoine de Saint-Exupéry", 1943, 29.90)
id_book02 = book_model.create_book("Animal Farm", "George Orwell", 1945, 34.99)
id_book03 = book_model.create_book("The Hitchhiker's Guide to the Galaxy", "Douglas Adams", 1979, 27.50)

# Read book:
book1 = book_model.read_book_by_id(id_book01)
book2 = book_model.read_book_by_id(id_book02)
book3 = book_model.read_book_by_id(id_book03)

# Update 3 book:
book_model.update_book(id_book01, "To Kill a Mockingbird", "Harper Lee", 1960, 15.99)
book_model.update_book(id_book02, "1984", "George Orwell", 1949, 12.50)
book_model.update_book(id_book03, "Pride and Prejudice", "Jane Austen", 1813, 9.99)


# Read book:
book_1 = book_model.read_book_by_id(id_book01)
book_2 = book_model.read_book_by_id(id_book02)

# Delete book:
book_model.delete_book(id_book01)
book_model.delete_book(id_book02)
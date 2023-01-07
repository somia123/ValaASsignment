import random
import string
import unittest
from utils import database

file_name = "library.txt"
class TestBookLibrary(unittest.TestCase):

    def test_sorted_books(self):
        books = database.get_all_books_sorted(file_name)
        sorted_books = [book.split('/') for book in books]
        sorted_books = sorted(sorted_books, key=lambda x:x[3])
        sorted_books = ['/'.join(sorted_book) for sorted_book in sorted_books]
        self.assertEqual(books,sorted_books)
        
    def test_book_details_addition(self):
        name = ''.join(random.sample((string.ascii_uppercase),6))
        author = ''.join(random.sample((string.ascii_uppercase),6))
        isbn = random.randint(19400283032,20223237289)
        year = random.randint(1940,2023)
        book=f'{name}/{author}/{isbn}/{year}'
        database.add_book_details_to_database(file_name,book)
        with open(file_name) as file:
            if book in file.read():
                present="True"
        self.assertTrue(present)
       
if __name__=='__main__':
	unittest.main()

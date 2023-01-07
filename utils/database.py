"""
Concerned with storing and returning books from a text file
"""     
"""
Add book details to the database
"""      
def add_book_details_to_database(file_name,book_data):
    with open(file_name, 'a') as file:
        file.write(f'{book_data}\n')
    books=get_all_books_sorted(file_name)
    with open(file_name, 'w') as file:
        for book in books:
            file.write(f'{book}\n')    
"""
Sort books in the ascending order
"""            
def get_all_books_sorted(file_name):
    with open(file_name, 'r') as file:
        books = [line.strip().split('/') for line in file.readlines()]
    books = sorted(books, key=lambda x:x[3])
    books = ['/'.join(book) for book in books]
    return books
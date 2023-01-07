# Main App -- Storing books in files.
import sys
from utils import database

file_name = sys.argv[1]
USER_CHOICE_1 = """
Enter following for : 
- '1' to Add new book.
- '2' to Print current database content in ascending order by publishing year.
- 'Q' to Exit the program
Your Choice : """

USER_CHOICE_2 = """
Do you want to update the database? 
- 'Y' to Update the database.
- 'N' to Return to the main menu
Your Choice : """


def menu():
    user_input = input(USER_CHOICE_1)

    while user_input.upper() != 'Q':
        if user_input == '1':
            book=prompt_add_book()
            user_input = input(USER_CHOICE_2)
            while user_input.upper() != 'N':
                if(user_input.upper()=='Y'):
                    database.add_book_details_to_database(file_name,book)
                    print("Book details added to database successfully..!!")
                    break       
                else:
                    print('Unknown Command. Please Try Again..!!')
                    user_input = input(USER_CHOICE_2)   
                    
        elif user_input == '2':
            list_books()
        else:
            print('Unknown Command. Please Try Again..!!')

        user_input = input(USER_CHOICE_1)
        
"""
User is prompted to provide book details to be added to the database.Keyword returns the the book details provided which can later be added to the database.
""" 
def prompt_add_book():
    name = input('Enter the Name of the Book : ')
    author = input('Enter the Name of the Author : ')
    isbn = input('Enter the ISBN : ')
    year=  inputNumber("Enter the Year of Publishing:")
    book=f'{name}/{author}/{isbn}/{year}'
    print_book_details(book)
    return book

"""
Prints the details of all the books in the ascending order from database  on screen.
""" 
def  list_books():
    books = database.get_all_books_sorted(file_name)
    for book in books:
        print_book_details(book)
"""
Prints the details of the book provided as an argument on the screen.
""" 
def print_book_details(book):
    book=book.split('/')
    print(f''''Name':{book[0]}, 'Author':{book[1]}, 'ISBN':{book[2]}, 'Year of Publishing':{book[3]}''')

def inputNumber(message):
    while True:
        try:
            userInput=int(input(message))
        except ValueError:
            print("Not an Integer! Try again.")
            continue
        else:
            return userInput
            break
    
menu()

from utils import database

USER_CHOICE= """
Enter: 
- 'a' to add a new book
- 'l' to list a book
- 'r' to mark a book as read
- 'd' to delete a book
- 'q' to quit
your choice: """

def menu():
    database.create_book_table()
    user_input= input(USER_CHOICE)
    while user_input != 'q' :
        if user_input== 'a' :
            prompt_add_book()
        elif user_input=='l':
            list_books()
        elif user_input=='r':
            read_book()
        elif user_input=='d':
            prompt_delete_book()
        else:
            print("unknown command! please type carefully.")

        user_input= input(USER_CHOICE)

def prompt_add_book():
    name= input("Enter the new book name: ")
    author= input("Enter author name of new book: ")

    database.add_book(name,author)

def list_books():
    books=database.get_all_books()
    for book in books:
        read='YES' if book['read'] else 'NO'
        print(f"{book['name']}, by {book['author']}, read:{read}")

def read_book():
    name=input("Enter the name of the book that you finished reading: ")

    database.mark_as_read(name)

def prompt_delete_book():
    name= input("Enter the name of book you wish to delete: ")

    database.delete_book(name)


print("search feature started.")
menu()

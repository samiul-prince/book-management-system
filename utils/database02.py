import json

""" concerned with storing and retrieving book from json file

[
  {  name, author, read
     name, author, read
     name, author, read
     }
]
"""

books_file= 'books.json'

def create_book_table():
    with open(books_file, 'w') as file:
        json.dump([], file) # just to make sure that file is there.....

def add_book(name, author):
    books=get_all_books()
    books.append({'name': name, 'author': author, 'read': False}) # normally as list in this code
    _save_all_books(books)


def get_all_books():
    with open(books_file, 'r') as file:
       return json.load(file)  # read file and turn into dictionaries...

def _save_all_books(books):
    with open(books_file,'w') as file:
        json.dump(books, file)  # write details on file....


def mark_as_read(name):
    books= get_all_books()
    for book in books:
        if book['name']== name:
         book['read'] = True

    _save_all_books(books)


def delete_book(name):
    books= get_all_books()
    # books= [book for book in books  if book['name']!= name]  (alternate)
    for book in books:
        if book['name']==name:
            books.remove(book)
    _save_all_books(books)



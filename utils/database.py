from .database_connection import DatabaseConnection

""" concerned with storing and retrieving book from a database...

"""

def create_book_table():
    # connection=sqlite3.connect('data.db')
    with DatabaseConnection ('data.db') as connection:

        cursor= connection.cursor()
        cursor.execute('CREATE TABLE books (name text primary key, author text, read integer)')

def add_book(name, author):
    with DatabaseConnection('data.db') as connection:

         cursor = connection.cursor()
         cursor.execute('INSERT INTO books VALUES (?, ?, 0)', (name, author) )


def get_all_books():
    with DatabaseConnection('data.db') as connection:

         cursor = connection.cursor()

         cursor.execute('SELECT * FROM books')
         books= [{'name': row[0], 'author': row[1], 'read': row[2]} for row in cursor.fetchall()] # [ (name, author, read), (name, author, read) ]

    return books

def mark_as_read(name):
    with DatabaseConnection('data.db') as connection:

         cursor=connection.cursor()
         cursor.execute('UPDATE books SET read=1 WHERE name=?',(name,))



def delete_book(name):
    with DatabaseConnection('data.db') as connection:

         cursor = connection.cursor()
         cursor.execute('DELETE FROM books WHERE name=?', (name,))





import mysql.connector
from decimal import Decimal, InvalidOperation

# Change credentials according your configuration.
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Parola121502690",
    database="libraries"
)
mycursor = mydb.cursor()


def to_decimal(ui_id):
    try:
        return Decimal(ui_id)
    except InvalidOperation:
        print('Invalid input. Please, enter a number.')
        return


class Library:
    def __init__(self, pk, name, location):
        self.pk = pk
        self.name = name
        self.location = location

    def __str__(self):
        return f'{self.name}'

    def __repr__(self):
        return f'{self.name}'

    @staticmethod
    def get_library_catalogue(libr_id):
        print("\nID\t Book Title \tAuthor \tGenre")
        sql = "SELECT * FROM books WHERE library_id = %s"
        mycursor.execute(sql, [libr_id])
        myresult = mycursor.fetchall()
        if myresult:
            for x in myresult:
                print(f"{x[0]}\t {x[1]}\t {x[2]}\t {x[3]}")

    @staticmethod
    def get_library(libr_id):
        libr_id = to_decimal(libr_id)
        sql = "SELECT * FROM libraries WHERE id = %s"
        mycursor.execute(sql, [libr_id])
        myresult = mycursor.fetchone()
        if myresult:
            return Library(*myresult)

    @staticmethod
    def print_library_list():
        print("\nID\t Library Name")
        sql = "SELECT id,name FROM libraries"
        mycursor.execute(sql)
        myresult = mycursor.fetchall()
        for x in myresult:
            print(f"{x[0]}\t {x[1]}")

class Book:

    def __init__(self, pk, title, author, genre, publisher, library_id):
        self.pk = pk
        self.title = title
        self.author = author
        self.genre = genre
        self.publisher = publisher
        self.library_id = library_id

    def __str__(self):
        return f'{self.title} {self.author}'

    def __repr__(self):
        return f'{self.title} {self.author}'

    @staticmethod
    def get_book(book_id, libr_id):
        book_id = to_decimal(book_id)
        sql = "SELECT * FROM books WHERE id = %s AND library_id = %s"
        mycursor.execute(sql, [book_id, libr_id])
        myresult = mycursor.fetchall()
        for x in myresult:
            return Book(*x)

    def show_book_info(self, book_id):
        book_id = to_decimal(book_id)
        sql = "SELECT * FROM books WHERE id = %s"
        mycursor.execute(sql, [book_id])
        myresult = mycursor.fetchall()
        if myresult:
            for x in myresult:
                print(f"id \t\t\t {x[0]} \n"
                      f"title \t\t {x[1]} \n"
                      f"author \t\t {x[2]} \n"
                      f"genre \t\t {x[3]} \n"
                      f"publisher \t {x[4]} \n"
                      f"library_id \t {x[5]}")

    @staticmethod
    def add_book(title, author, genre, publisher, library_id):
        sql = f"INSERT INTO books (id, title, author, genre, publisher, library_id) VALUES (NULL, %s, %s, %s, %s, %s)"
        val = (title, author, genre, publisher, library_id)
        mycursor.execute(sql, val)
        mydb.commit()
        print(f'Book "{title}" added successfully to library {library_id}.')

    def delete_book(self, book_id):
        book_id = to_decimal(book_id)
        if self.pk == book_id:
            sql = "DELETE FROM books WHERE id = %s"
            mycursor.execute(sql, [book_id])
            mydb.commit()
            print(f'Book {self.title} with {book_id} successfully deleted.')
        else:
            print('You entered a nonexistent book ID. Please, try again.')

    def redact_book(self, key, value):
        sql = f"UPDATE books SET {key} = %s WHERE id = {self.pk}"
        mycursor.execute(sql, [value])
        mydb.commit()
        print(f'Book "{self.title}" redacted successfully with new %s - %s.' % (key, value))

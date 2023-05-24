import csv
import mysql.connector

def load_data_from_csv(file_path):

    with open(file_path, newline='') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)
        return list(reader)

# Change credentials according your configuration.
connector = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Parola121502690',
    port=3306,
)

cursor = connector.cursor()

cursor.execute('CREATE DATABASE IF NOT EXISTS libraries')
cursor.execute('USE libraries')
cursor.execute('''
CREATE TABLE IF NOT EXISTS libraries(  
    id INT NOT NULL AUTO_INCREMENT,  
    name VARCHAR(50),  
    location VARCHAR(50),  
    PRIMARY KEY (id)  
);
''')

libraries = load_data_from_csv('libraries.csv')
sql = "INSERT INTO libraries (id, name, location) VALUES (%s, %s, %s)"
cursor.executemany(sql, libraries)

connector.commit()

cursor.execute('''
CREATE TABLE IF NOT EXISTS books(  
    id INT NOT NULL AUTO_INCREMENT,  
    title VARCHAR(100),  
    author VARCHAR(50),  
    genre VARCHAR(50),  
    publisher VARCHAR(50),  
    library_id INT(4) NOT NULL,
    PRIMARY KEY (id), 
    FOREIGN KEY (library_id) REFERENCES libraries(id)
);
''')

books = load_data_from_csv('books.csv')
sql = "INSERT INTO books (id, title, author, genre, publisher, library_id) VALUES (%s, %s, %s, %s, %s, %s)"
cursor.executemany(sql, books)

connector.commit()


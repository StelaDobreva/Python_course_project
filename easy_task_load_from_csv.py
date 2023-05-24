import pandas as pd


libraries = pd.read_csv('libraries.csv', index_col=['id'])
books = pd.read_csv('books.csv', index_col=['id'])

ui_libr = input(f"From the following catalogue of libraries: \n{libraries.to_string(columns=['name'])} "
                f"\nchoose a library by ID: ")

if ui_libr.isdigit():
    ui_libr = int(ui_libr)
    if ui_libr in libraries.index:
        _filter = books['library_id'] == ui_libr
        filtered_books = books[_filter]
        ui_book = input(f"From the following catalogue of books: \n{filtered_books.to_string(columns=['title'])} "
                        f"\nchoose a book ID for more information about the book or E for exit: ")
        if ui_book.lower() == "e":
            exit()
        elif ui_book.isdigit():
            ui_book = int(ui_book)
            if ui_book in filtered_books.index:
                chosen_book = filtered_books.query(f"id == {ui_book}")
                print(f"{chosen_book.to_string()}")
            else:
                print("Invalid book ID.")
        else:
            print("Invalid book ID.")
    else:
        print("Invalid library ID.")
else:
    print("Invalid library ID.")


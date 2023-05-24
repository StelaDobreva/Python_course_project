from hard_task import Library, Book

print("Welcome to the library system!")

Library.print_library_list()

libr_id = input("Enter library ID to see a list of available books. Enter your choice: ")

user_libr = Library.get_library(libr_id)

if user_libr:
    user_libr.get_library_catalogue(libr_id)
    while True:
        print("")
        action = input('Enter a number to choose action: \n'
                       '1 for book details \n'
                       '2 to add new book \n'
                       '3 to redact book details \n'
                       '4 to delete book \n'
                       '5 to exit\n'
                       'Enter your choice: ')
        if action == '1':
            user_libr.get_library_catalogue(libr_id=libr_id)
            ui_book_id = input("Enter book ID to proceed: ")
            user_book = Book.get_book(book_id=ui_book_id, libr_id=libr_id)
            try:
                user_book.show_book_info(book_id=ui_book_id)
            except AttributeError:
                print(f"\nNo book with ID {ui_book_id} is found in library {user_libr.name}.")
        elif action == '2':
            ui = input("To add a new book enter the following data in the specified order separated by "
                       "comma: title, author, genre, publisher. \nEnter data: ")
            ui = [x.strip() for x in ui.split(',')]
            Book.add_book(title=ui[0], author=ui[1], genre=ui[2], publisher=ui[3], library_id=libr_id)
        elif action == '3':
            user_libr.get_library_catalogue(libr_id)
            ui_book_id = input("Enter book ID to proceed: ")
            user_book = Book.get_book(book_id=ui_book_id, libr_id=libr_id)
            try:
                ui = input(
                    "To redact book information enter data e.g. parameter = new value. \n"
                    "Allowed parameter are: title / author / "
                    "genre / publisher /library_id. \nEnter data:")
                ui = [x.strip() for x in ui.split('=')]
                user_book.redact_book(key=ui[0], value=ui[1])
            except AttributeError:
                print(f"\nNo book with ID {ui_book_id} is found in library {user_libr.name}.")
        elif action == '4':
            user_libr.get_library_catalogue(libr_id)
            ui_book_id = input("Enter book ID to proceed: ")
            user_book = Book.get_book(book_id=ui_book_id, libr_id=libr_id)
            try:
                user_book.delete_book(ui_book_id)
            except AttributeError:
                print(f"\nNo book with ID {ui_book_id} is found in library {user_libr.name}.")
        elif action == '5':
            break
        else:
            print('Invalid action.')
else:
    print("Invalid library ID.")

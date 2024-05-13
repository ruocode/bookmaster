import sys, re

# basic validation, check that the right amount of columns are present and have the right type of data, check year length
def validate_data(book):
    return bool(re.match(r'^\w.*/\w.*/\d+/\d{1,4}$', book))

# pretty print/format book info for human readers
def pretty_info(book):
    return book.replace('/', ' - ')

print("Bookmaster 1.0 initializing.")
with open(sys.argv[1], 'r') as file:
    book_db = file.readlines()

while True:
    user_input = input("1: List database contents\n2: Add new book\nQ: Quit programm\n")

    if user_input == '1':
        print("TITLE - AUTHOR - ISBN - YEAR")
        for line in book_db:
            print(pretty_info(line), end='')
    elif user_input  == '2':
        new_book = input("Enter new book data as a single line in the following format: TITLE/AUTHOR/ISBN/YEAR\n")
        if not new_book.strip():
            print("Empty input.")
        elif not validate_data(new_book):
            print("Invalid book data format.")
        else:
            confirm_new = input("Enter Y to confirm adding new book to database:\n" + pretty_info(new_book) + "\n")
            if confirm_new.upper() == 'Y':
                print("Saving book data.")
                book_db.append(new_book + '\n')
                book_db.sort(key=lambda x: x.split('/')[-1].rstrip())  # sort by year
                with open(sys.argv[1], 'w') as file:
                    for book in book_db:
                        file.write(book)
                 
            else:
                print("Cancelled saving new book data.")
    elif user_input.upper() == 'Q':
        break
    else:
        print("Invalid input.")

print("Bookmaster exiting.")    
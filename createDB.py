import sqlite3

# Create database or connect to an existing one
myDB = sqlite3.connect('address_book.db')

# Create a cursor
dbCursor = myDB.cursor()

# Create a table
dbCursor.execute("""CREATE TABLE addresses (
                    first_name text,
                    last_name text,
                    address text,
                    city text,
                    state text,
                    zipcode integer
                    )""")

myDB.commit()
myDB.close()





# In this code you can find how to use tkinter in databases
from tkinter import *
import sqlite3
from tkinter import messagebox

root = Tk()
root.title("Database Form")

# create a database or connect to a database
connection = sqlite3.connect('address_book.db')

# create a cursor
cursor = connection.cursor()

# we want to be able to submit entries to our database and thats the function below

def submit():
    # to modify stuff in our database we have to stay connected
    connection = sqlite3.connect('address_book.db')
    # create a cursor
    connection_cursor = connection.cursor()

    # insert into table
    connection.execute("INSERT INTO addresses VALUES (:first, :last, :address, :city, :state, :zipcode)",
                       {
                           'first': first_name.get(),
                           'last': last_name.get(),
                           'address': address.get(),
                           'city': city.get(),
                           'state': state.get(),
                           'zipcode': zipcode.get()
                       })
    # commit change
    connection.commit()
    # close connection
    connection.close()



    # clear text boxes
    first_name.delete(0, END)
    last_name.delete(0, END)
    address.delete(0, END)
    city.delete(0, END)
    state.delete(0, END)
    zipcode.delete(0, END)

# create query function

def query():
    # to modify stuff in our database we have to stay connected
    connection = sqlite3.connect('address_book.db')
    # create a cursor
    connection_cursor = connection.cursor()

    # querying the database
    connection_cursor.execute("SELECT *, oid FROM addresses")
    entries = connection_cursor.fetchall()
    # print(entries) #to see what being done

    # lets take a look at what is our table addresses
    print_entry = ''
    for entry in entries:
        print_entry += str(entry[0]) + " " +str(entry[1]) + "\t"+ str(entry[-1]) + "\n"
        # this gives you (the sql created) id first last name for each entry

    query_label = Label(root, text=print_entry)
    query_label.grid(row=12, column=0, columnspan=2)

    # commit change
    connection.commit()
    # close connection
    connection.close()

# create a delete function
def delete():
    # to modify stuff in our database we have to stay connected
    connection = sqlite3.connect('address_book.db')
    # create a cursor
    connection_cursor = connection.cursor()

    connection_cursor.execute("DELETE FROM addresses WHERE oid =" + delete_box.get())

    # commit change
    connection.commit()
    # close connection
    connection.close()

def save():
    # to modify stuff in our database we have to stay connected
    connection = sqlite3.connect('address_book.db')
    # create a cursor
    connection_cursor = connection.cursor()

    entry_id = delete_box.get()
    connection_cursor.execute("""UPDATE addresses SET
                            first_name = :first,
                            last_name = :last,
                            address = :address,
                            city = :city,
                            state = :state,
                            zipcode = :zipcode 
                            
                        
                        WHERE oid = :oid""",

                        {
                            'first': first_name_update.get(),
                            'last': last_name_update.get(),
                            'address': address_update.get(),
                            'city': city_update.get(),
                            'state': state_update.get(),
                            'zipcode': zipcode_update.get(),
                            'oid': entry_id
                        })

    # commit change
    connection.commit()
    # close connection1
    connection.close()
    root2.destroy()
    messagebox.showinfo("Information", "Update successful!")

# This will be our update function and what it will do is open a new window with all our fields
# so we can update those we want to update


def update():
    global root2
    root2 = Tk()
    root2.title("Update Entry")

    # this is a bit messy but we need to define our fields as global so they can be called from
    # more that one function

    global first_name_update
    global last_name_update
    global address_update
    global city_update
    global state_update
    global zipcode_update

    # create text boxes
    first_name_update = Entry(root2, width=30)
    first_name_update.grid(row=0, column=1, padx=20, pady=(10, 0))

    last_name_update = Entry(root2, width=30)
    last_name_update.grid(row=1, column=1, padx=20)

    address_update = Entry(root2, width=30)
    address_update.grid(row=2, column=1, padx=40)

    city_update = Entry(root2, width=30)
    city_update.grid(row=3, column=1, padx=20)

    state_update = Entry(root2, width=30)
    state_update.grid(row=4, column=1, padx=20)

    zipcode_update = Entry(root2, width=30)
    zipcode_update.grid(row=5, column=1, padx=20)

    # text box labels

    first_name_update_label = Label(root2, text="Enter user's first name")
    first_name_update_label.grid(row=0, column=0, pady=(10, 0))

    last_name_update_label = Label(root2, text="Enter user's last name")
    last_name_update_label.grid(row=1, column=0)

    address_update_label = Label(root2, text="Enter user's address")
    address_update_label.grid(row=2, column=0)

    city_update_label = Label(root2, text="Enter user's city of residence")
    city_update_label.grid(row=3, column=0)

    state_update_label = Label(root2, text="Enter user's state")
    state_update_label.grid(row=4, column=0)

    zipcode_update_label = Label(root2, text="Enter user's address zipcode")
    zipcode_update_label.grid(row=5, column=0)


    # to modify stuff in our database we have to stay connected
    connection = sqlite3.connect('address_book.db')
    # create a cursor
    connection_cursor = connection.cursor()

    entry_id = delete_box.get()
    connection_cursor.execute("SELECT * FROM addresses WHERE oid =" + entry_id)
    entries = connection_cursor.fetchall()
    # we go through what we have
    for entry in entries:
        first_name_update.insert(0, entry[0])
        last_name_update.insert(0, entry[1])
        address_update.insert(0, entry[2])
        city_update.insert(0, entry[3])
        state_update.insert(0, entry[4])
        zipcode_update.insert(0, entry[5])

    # we need a button which we can click to save the changes we want to make
    save_button = Button(root2, text="Save", command=save)
    save_button.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=137)


############################################################
# create a table
'''
cursor.execute(""" CREATE TABLE addresses (
                first_name text,
                last_name text,
                address text,
                city text,
                state text,
                zipcode integer
                ) """)
''' # the table was created so no need to have this line running everytime we run this program

# create text boxes
first_name = Entry(root, width=30)
first_name.grid(row=0, column=1, padx=20, pady=(10,0))

last_name = Entry(root, width=30)
last_name.grid(row=1, column=1, padx=20)

address = Entry(root, width=30)
address.grid(row=2, column=1, padx=40)

city = Entry(root, width=30)
city.grid(row=3, column=1, padx=20)

state = Entry(root, width=30)
state.grid(row=4, column=1, padx=20)

zipcode = Entry(root, width=30)
zipcode.grid(row=5, column=1, padx=20)

delete_box = Entry(root, width=30)
delete_box.grid(row=9, column=1, padx=20)

# text box labels

first_name_label = Label(root, text = "Enter user's first name")
first_name_label.grid(row=0, column=0,pady=(10,0))

last_name_label = Label(root, text = "Enter user's last name")
last_name_label.grid(row=1, column=0)

address_label = Label(root, text = "Enter user's address")
address_label.grid(row=2, column=0)

city_label = Label(root, text = "Enter user's city of residence")
city_label.grid(row=3, column=0)

state_label = Label(root, text = "Enter user's state")
state_label.grid(row=4, column=0)

zipcode_label = Label(root, text = "Enter user's address zipcode")
zipcode_label.grid(row=5, column=0)

delete_label = Label(root, text = "Select an entry with ID number")
delete_label.grid(row=9, column=0, pady =5, padx = 5)

# create a submit button
submit_button = Button(root, text = "Add an entry to the database", command = submit)
submit_button.grid(row=6, column = 0, columnspan = 2, pady = 10, padx = 10, ipadx = 100)

# create a query button
query_button = Button(root, text = "Show entries", command = query)
query_button.grid(row=7, column=0, columnspan=2, pady=10, padx=10, ipadx=137)

# create a delete button

delete_button = Button(root, text = "Delete entry", command = delete)
delete_button.grid(row=10, column=0, columnspan=2, pady=10, padx=10, ipadx=137)

# create an update buttor

update_button = Button(root, text = "Update entry", command = update)
update_button.grid(row=11, column=0, columnspan=2, pady=10, padx=10, ipadx=137)







# commit changes
connection.commit()

# close connection
connection.close()


mainloop()

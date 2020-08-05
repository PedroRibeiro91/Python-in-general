from tkinter import *
from tkinter import messagebox
import sqlite3

root = Tk()
root.title("User Form")


def save():
    # Create database or connect to an existing one
    myDB = sqlite3.connect('address_book.db')

    # Create a cursor
    dbCursor = myDB.cursor()

    # save the changes
    user_id = select_id.get()
    dbCursor.execute("""UPDATE addresses SET 
                first_name = :first,
                last_name = :last,
                address = :address,
                city = :city,
                state = :state,
                zipcode = :zipcode
                
                WHERE oid = :oid""",
                {'first':fn_updated.get(),
                 'last':ln_updated.get(),
                 'address': address_updated.get(),
                 'city': city_updated.get(),
                 'state': state_updated.get(),
                 'zipcode': zip_updated.get(),
                 'oid': user_id
                 })

    myDB.commit()
    myDB.close()
    messagebox.showinfo("Notification", "Update Sucessfull!!")
    root2.destroy()

    # after we click save we want to close the second window that opens on update


def update():
    global root2
    root2 = Tk()
    root2.title("Update Window")

    # Create database or connect to an existing one
    myDB = sqlite3.connect('address_book.db')

    # Create a cursor
    dbCursor = myDB.cursor()

    user_id = select_id.get()
    dbCursor.execute("SELECT * FROM addresses WHERE oid = " + user_id)


    # Create our form text boxes
    # first name
    # all of these will need to be global so we can call them on the save function
    global fn_updated
    global ln_updated
    global address_updated
    global city_updated
    global state_updated
    global zip_updated

    fn_updated = Entry(root2, width=30)
    fn_updated.grid(row=0, column=1, padx=20, pady=(10, 0))

    # last name
    ln_updated = Entry(root2, width=30)
    ln_updated.grid(row=1, column=1, padx=20)

    # address
    address_updated = Entry(root2, width=30)
    address_updated.grid(row=2, column=1, padx=20)

    # city
    city_updated = Entry(root2, width=30)
    city_updated.grid(row=3, column=1, padx=20)

    # state
    state_updated = Entry(root2, width=30)
    state_updated.grid(row=4, column=1, padx=20)

    # zipcode
    zip_updated = Entry(root2, width=30)
    zip_updated.grid(row=5, column=1, padx=20)

    # we create labels now, so we know what are we adding
    # labels domt affect anything related to what is going inside the text boxes so theres no harm in
    # recycling these
    # first name
    fn_label = Label(root2, text="Insert First Name")
    fn_label.grid(row=0, column=0, pady=(10, 0))

    # last name
    ln_label = Label(root2, text="Insert Last Name")
    ln_label.grid(row=1, column=0)

    # address
    address_label = Label(root2, text="Insert Address")
    address_label.grid(row=2, column=0)

    # city
    city_label = Label(root2, text="Insert City of Residence")
    city_label.grid(row=3, column=0)

    # state
    state_label = Label(root2, text="Insert State of Residence")
    state_label.grid(row=4, column=0)

    # zipcode
    zip_label = Label(root2, text="Insert Zipcode")
    zip_label.grid(row=5, column=0)

    users = dbCursor.fetchall()
    for user in users:
        fn_updated.insert(0, user[0])
        ln_updated.insert(0, user[1])
        address_updated.insert(0, user[2])
        city_updated.insert(0, user[3])
        state_updated.insert(0, user[4])
        zip_updated.insert(0, user[5])

    # we need a save button
    save_button = Button(root2, text="Save Changes", command=save)
    save_button.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=15)

    myDB.commit()
    myDB.close()


# Create our submit function that will allows us to insert users information in our address book

def submit():
    # Create database or connect to an existing one
    myDB = sqlite3.connect('address_book.db')
    # Create a cursor
    dbCursor = myDB.cursor()

    dbCursor.execute("INSERT INTO addresses VALUES (:fn, :ln, :address, :city, :state, :zip)",
      # same as our text boxes "names"
                        {
                            'fn': fn.get(),
                            'ln': ln.get(),
                            'address': address.get(),
                            'city': city.get(),
                            'state': state.get(),
                            'zip': zip.get()
                        })

    myDB.commit()
    myDB.close()
    # we need to know if we succeeded when we add new information to our address book
    messagebox.showinfo("Notification", "Submission Successful!")

    # Clear the textboxes each time we click submit
    fn.delete(0, END)
    ln.delete(0, END)
    address.delete(0, END)
    city.delete(0, END)
    state.delete(0, END)
    zip.delete(0, END)


def query():
    # Create database or connect to an existing one
    myDB = sqlite3.connect('address_book.db')

    # Create a cursor
    dbCursor = myDB.cursor()

    dbCursor.execute("SELECT *,oid FROM addresses")
    users = dbCursor.fetchall()

    showUsers = ''
    for user in users:
        showUsers += str(user[0]) + " " + str(user[1]) + "\t" + str(user[-1]) + "\n"

    query_label = Label(root,  text = showUsers)
    query_label.grid(row = 12, column = 0, columnspan = 2)

    myDB.commit()
    myDB.close()


# eventualy we need to delete users from our database and thats what the following function will do

def delete():
    # Create database or connect to an existing one
    myDB = sqlite3.connect('address_book.db')

    # Create a cursor
    dbCursor = myDB.cursor()

    dbCursor.execute("DELETE FROM addresses WHERE oid= " + select_id.get())
    messagebox.showinfo("Notification", "User successfully removed!")


    myDB.commit()
    myDB.close()
    return




# Create our form text boxes
# first name
fn = Entry(root, width = 30)
fn.grid(row = 0, column = 1, padx = 20, pady=(10,0))

# last name
ln = Entry(root, width = 30)
ln.grid(row = 1, column = 1, padx = 20)

# address
address = Entry(root, width = 30)
address.grid(row = 2, column = 1, padx = 20)

# city
city = Entry(root, width = 30)
city.grid(row = 3, column = 1, padx = 20 )

# state
state = Entry(root, width = 30)
state.grid(row = 4, column = 1, padx = 20)

# zipcode
zip = Entry(root, width = 30)
zip.grid(row = 5, column = 1, padx = 20)

# select Id box
select_id = Entry(root, width = 30)
select_id.grid(row = 9, column=1, padx = 20)

# we create labels now, so we know what are we adding

# first name
fn_label = Label(root, text = "Insert First Name")
fn_label.grid(row = 0, column =0, pady=(10,0))

# last name
ln_label = Label(root, text = "Insert Last Name")
ln_label.grid(row = 1, column =0)

# address
address_label = Label(root, text = "Insert Address")
address_label.grid(row = 2, column =0)

# city
city_label = Label(root, text = "Insert City of Residence")
city_label.grid(row = 3, column =0)

# state
state_label = Label(root, text = "Insert State of Residence")
state_label.grid(row = 4, column =0)

# zipcode
zip_label = Label(root, text = "Insert Zipcode")
zip_label.grid(row = 5, column =0)

# Insert ID
select_id_label = Label(root, text = "Insert User ID")
select_id_label.grid(row = 9, column = 0)


# we need buttons
# this button adds entries to the database
submit_button = Button(root, text = "Add a user to the database", command = submit)
submit_button.grid(row = 6, column = 0, columnspan = 2, pady = 10, padx = 10, ipadx = 10)

# query button will shows whats in the database

query_button = Button(root, text = "Show users", command = query)
query_button.grid(row = 7, column = 0, columnspan = 2, pady = 10, padx = 10, ipadx = 50)

# delete button
delete_button = Button(root, text = "Delete the selected user", command = delete)
delete_button.grid(row = 10, column = 0, columnspan = 2, pady = 10, padx = 10, ipadx = 20)

# update button
update_button = Button(root, text = "Update users information", command = update)
update_button.grid(row = 11, column = 0, columnspan = 2, pady = 10, padx = 10, ipadx = 15)





root.mainloop()
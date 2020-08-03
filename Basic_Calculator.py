from tkinter import *

root = Tk()
root.title("Basic Calculator")

e = Entry(root, width = 35, borderwidth = 5)
e.grid(row = 0, column = 0, columnspan = 4, padx = 10, pady = 10)

def clickNumber(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))

def clickClear():
    e.delete(0, END)

def clickPlus():
    f_number = e.get()
    e.delete(0, END)
    global first_number
    first_number = int(f_number)
    global operator
    operator = "Addition"

def clickMinus():
    f_number = e.get()
    e.delete(0, END)
    global first_number
    first_number = int(f_number)
    global operator
    operator = "Subtraction"


def clickMultiply():
    f_number = e.get()
    e.delete(0, END)
    global first_number
    first_number = int(f_number)
    global operator
    operator = "Multiplication"


def clickDivide():
    f_number = e.get()
    e.delete(0, END)
    global first_number
    first_number = int(f_number)
    global operator
    operator = "Division"


def clickEqual():
    s_number = e.get()
    e.delete(0, END)
    if operator == "Addition":
        e.insert(0, first_number + int(s_number))
    elif operator == "Subtraction":
        e.insert(0, first_number - int(s_number))
    elif operator == "Multiplication":
        e.insert(0, first_number * int(s_number))
    else:
        if int(s_number) == 0:
            e.insert(0, "ERROR!! I CAN'T DIVIDE BY ZERO")

        e.insert(0, first_number / int(s_number))



def clickPoint():
    number = e.get()
    e.delete(0, END)
    e.insert(0, number + ".")


def clickPercent():
     number = e.get()
     e.delete(0,END)
     e.insert(0, int(number)/100)

# define buttons
button_1 = Button(root, text = 1, padx = 30, pady =20, command = lambda: clickNumber(1))
button_2 = Button(root, text = 2, padx = 30, pady =20, command = lambda: clickNumber(2))
button_3 = Button(root, text = 3, padx = 30, pady =20, command = lambda: clickNumber(3))
button_4 = Button(root, text = 4, padx = 30, pady =20, command = lambda: clickNumber(4))
button_5 = Button(root, text = 5, padx = 30, pady =20, command = lambda: clickNumber(5))
button_6 = Button(root, text = 6, padx = 30, pady =20, command = lambda: clickNumber(6))
button_7 = Button(root, text = 7, padx = 30, pady =20, command = lambda: clickNumber(7))
button_8 = Button(root, text = 8, padx = 30, pady =20, command = lambda: clickNumber(8))
button_9 = Button(root, text = 9, padx = 30, pady =20, command = lambda: clickNumber(9))
button_0 = Button(root, text = 0, padx = 30, pady =20, command = lambda: clickNumber(0))

button_equal = Button(root, text = "=", padx = 70, pady =20, command = lambda: clickEqual())

button_clear = Button(root, text = "Clear", padx = 70, pady =20, command = clickClear)

button_plus = Button(root, text = "+", padx = 30, pady =20, command = clickPlus)
button_minus = Button(root, text = "-", padx = 30, pady =20, command = clickMinus)
button_mult = Button(root, text = "x", padx = 30, pady =20, command = clickMultiply)
button_divide = Button(root, text = "/", padx = 30, pady =20, command = clickDivide)

button_point = Button(root, text = ".", padx = 30, pady =20, command = clickPoint)
button_percent = Button(root, text = "%", padx = 30, pady =20, command = clickPercent)

# pack buttons

button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)
button_point.grid(row=4, column=1)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)
button_percent.grid(row=4, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_0.grid(row=4, column=0)

button_equal.grid(row=5, column=2, columnspan = 2)
button_clear.grid(row=5, column=0, columnspan = 2)

button_plus.grid(row=1, column=3)
button_minus.grid(row=2, column=3)
button_mult.grid(row=3, column=3)
button_divide.grid(row=4, column=3)

#button_point(row=5, column = 2)

root.mainloop()


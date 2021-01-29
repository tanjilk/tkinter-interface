from tkinter import *

# Shows in the console the input and places on the text widget to the miles
def km_to_miles():
    # Shows the input
    print(e1_value.get())
    # Convert input to miles
    miles = float(e1_value.get()) * 1.6
    # Places the miles into text widget
    t1.insert(END, miles)


# Create a window
window = Tk()

# Create a button
b1 = Button(window, text="Execute", command=km_to_miles)

# Places the button
b1.grid(row=0, column=0)


# Create an string var objetct
e1_value = StringVar()

# Create input
e1 = Entry(window, textvariable=e1_value)

# Places input
e1.grid(row=0, column=1)

# Creates an text widget
t1 = Text(window, height=1, width=20)
t1.grid(row=0, column=2)

# Mantains the window
window.mainloop()

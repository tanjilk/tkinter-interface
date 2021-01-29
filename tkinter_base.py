from tkinter import *

# Create a window
window = Tk()

# Create a button
b1 = Button(window, text="Execute")

# Places the button
b1.grid(row=0, column=0)

# Create an input
e1 = Entry(window)
e1.grid(row=0, column=1)

# Creates an text widget
t1 = Text(window, height=1, width=20)
t1.grid(row=0, column=2)

# Mantains the window
window.mainloop()

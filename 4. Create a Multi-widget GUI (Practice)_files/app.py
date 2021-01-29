from tkinter import * 

window = Tk()

def convert():
    grams = float(kg.get()) * 1000
    text_gr.insert(END,grams)

    pounds = float(kg.get()) * 2.20462
    text_pounds.insert(END,pounds)

    ounces = float(kg.get()) * 35.274
    text_ounces.insert(END,ounces) 

label = Label(window, text="Kg")
label.grid(row=0, column=0)

kg = StringVar()
kg_entry = Entry(window, textvariable=kg)
kg_entry.grid(row=0, column=1)

convert = Button(window, text="Convert", command=convert)
convert.grid(row=0, column=2)

text_gr = Text(window, height=1, width=20)
text_gr.grid(row=1, column=0)

label_gr = Label(window, text="Grams")
label_gr.grid(row=2, column=0)

text_pounds = Text(window, height=1, width=20)
text_pounds.grid(row=1, column=1)

label_pounds = Label(window, text="Pounds")
label_pounds.grid(row=2, column=1)

text_ounces = Text(window, height=1, width=20)
text_ounces.grid(row=1, column=2)

label_ounces = Label(window, text="Ounces")
label_ounces.grid(row=2, column=2)



window.mainloop()
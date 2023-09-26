from tkinter import messagebox
from tkinter import *

window = Tk()
window.config(padx=100,pady=100)

def show_message():
    print(messagebox.askokcancel(title="123", message="456"))

b = Button(text="Button", command=show_message)
b.pack()

window.mainloop()


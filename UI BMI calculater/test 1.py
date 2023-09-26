# scores = (20,30,40,50)
# print(scores[0])

from tkinter import *
import tkinter.font as tkFont

window = Tk()
window.title("First project")
window.geometry("400x400")
window.maxsize(width="400",height="400")
window.resizable(True,False)

#label
my_label = Label(text="How you doing")
my_label.pack(side="top", pady=20)
my_label.grid(row=0,column=0)
my_label["text"] = "Hola"

def click():
    print(my_entry.get())
    my_label["text"] = my_entry.get()

#button
my_button= Button(text="Button", command=click)
my_button.pack(side="top",pady=10)
my_button.place(anchor="center", x=200,y=200)

#entry
my_entry = Entry(width=10)
my_entry.pack(side="top",pady=15)
my_entry.place(anchor="center", x=150,y=150)
my_entry.get()
# print(tkFont.families())

window.mainloop()
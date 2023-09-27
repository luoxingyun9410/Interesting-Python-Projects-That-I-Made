from tkinter import *
from tkinter import messagebox
import tkinter.font as tkFont

window = Tk()
window.title("BMI Calculator")
window.geometry("300x300")
window.config(padx=50,pady=50)

height_label = Label(text="Height")
height_label .grid(row=0,column=0)

height_input=Entry()
height_input.grid(row=0,column=1)

cm_label = Label(text="cm")
cm_label.grid(row=0,column=2)

weight_label = Label(text="Weight")
weight_label.grid(row=1,column=0)

weight_input=Entry()
weight_input.grid(row=1,column=1)

kg_label = Label(text="kg")
kg_label.grid(row=1,column=2)

bmi_label = Label(text="Your BMI is ")
bmi_label.grid(row=2, column=1)

def cal_bmi():
        try:
            height = float(height_input.get())/100
            weight = float(weight_input.get())
            if height < 0 or weight < 0:
                 raise ValueError("Height or weight cannot be negative")
        except:
            messagebox.showerror(title="Error", message="Wrong type of input")
        else:
            bmi = weight / height**2
            bmi = round(bmi, 1)
            bmi_label["text"] = f"Your BMI is {bmi}"

button = Button(text="Calculate",command=cal_bmi)
button.grid(row=3, column=1)

window.mainloop()
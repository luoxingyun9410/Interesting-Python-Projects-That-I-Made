from tkinter import *
from PIL import Image, ImageTk
import json
from tkinter import messagebox

window = Tk()
window.title("LastPass")
window.config(padx=50,pady=50)

img = ImageTk.PhotoImage(file="C:/Users/steven.luo/Documents/Python project/Interesting-Python-Projects-That-I-Made/UI LastPass/lock.png")
window.iconphoto(True, img)
canvas = Canvas(width=224,height=225)
canvas.create_image(112,112,image = img)
canvas.grid(row=0, column=0, columnspan=2)

name_label = Label(text="Name")
name_label.grid(row=1,column=0)

name_input=Entry()
name_input.grid(row=1,column=1)

acc_label = Label(text="Account")
acc_label.grid(pady=5, row=2,column=0)

acc_input=Entry()
acc_input.grid(row=2,column=1)

pass_label = Label(text="Password")
pass_label.grid(row=3,column=0)

pass_input=Entry()
pass_input.grid(row=3,column=1)


def get_password_dic():
    with open("password.json","r") as f:
        password_str = f.read()
        if password_str == "":
            return {}
        else:
            return json.loads(password_str)
        
def add_password():
    password_dic = get_password_dic()
    name = name_input.get()
    account = acc_input.get()
    password = pass_input.get()

    if name =="" or account =="" or password == "":
        print(messagebox.showerror(title="Failed", message="Entry cannot be empty"))
    elif name in password_dic.keys():
        print(messagebox.showerror(title="Failed", message="Account already exists"))
    else:
        password_dic[name] = {
            "account":account,
            "password":password
        }

        with open("password.json","w") as f:
            f.write(json.dumps(password_dic))

        name_input.delete(0,'end')
        acc_input.delete(0,'end')
        pass_input.delete(0,'end')

        messagebox.showinfo(title="Successed", message="New account has been added")

def search_acc():
    password_dic = get_password_dic()
    if name_input in password_dic.keys():
        name = name_input.get()
        account = password_dic[name]["account"]
        password = password_dic[name]["password"]
        messagebox.showinfo(title=name, message=f"Account: {account}\nPassword: {password}")
    else:
        return True
    
button1 = Button(text="Search", width=35, bg="#8E8E8E", fg="white", command=search_acc)
button1.grid(pady=10, row=4, column=0, columnspan=2)

button = Button(text="Add", width=35, bg="#0066CC", fg="white", command=add_password)
button.grid(row=5, column=0, columnspan=2)

window.mainloop()
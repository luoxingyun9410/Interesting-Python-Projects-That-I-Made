import json

def get_password_dic():
    with open("password.json", "r") as f:
        return json.loads(f.read())

def add_password(name, account, password):
    password_dic = get_password_dic()
    password_dic[name] = {
        "account": account,
        "password": password
    }
    with open ("password.json", "w") as f:
        f.write(json.dumps(password_dic))



print("Welcome!")

while True:
    option = input("What would you like to do today? (r Search a Add q Exit)")
    if option == "q":
        break
    elif option == "a":
        name = input("Please enter account name: ")
        account = input("Please enter account: ")
        password = input("Please enter password: ")
        add_password(name, account, password)

    
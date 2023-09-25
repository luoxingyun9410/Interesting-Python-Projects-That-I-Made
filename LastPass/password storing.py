import json

def get_password_dic():
        with open("password.json", "r") as f:
            password_str = f.read()
            if password_str == "":
                return {}
            else:
                return json.loads(f.read())

def ckeck_name(name):
    password_dic = get_password_dic()
    if name in password_dic.keys():
        return False
    else:
        return True

def add_password(name, account, password):
    if ckeck_name(name):
        password_dic = get_password_dic()
        password_dic[name] = {
            "account": account,
            "password": password
        }
        with open ("password.json", "w") as f:
            f.write(json.dumps(password_dic))
        return True
    else:
        return False


print("Welcome!")

while True:
    option = input("What would you like to do today? (r Search a Add q Exit)")
    if option == "q":
        break
    elif option == "a":
        name = input("Please enter account name: ")
        account = input("Please enter account: ")
        password = input("Please enter password: ")
        if add_password(name, account, password):
            print("Successful!")
        else:
            print("It already exists")
    elif option == "r":
        name = input("Please enter account name: ")
        if ckeck_name(name):
            print("It does not exists")
        else:
            password_dic = get_password_dic()
            account = password_dic["name"]["account"]
            password = password_dic["name"]["password"]
            print(f"Account: {account}, Password: {password}")
    
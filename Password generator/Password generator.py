import random

letters_upper = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J",
                 "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T",
                 "U", "V", "W", "X", "Y", "Z"]

letters_lower = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j",
                 "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
                 "u", "v", "w", "x", "y", "z"]

numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

symbols = ["!", "@", "#", "$", "%", "^", "&", "*", "-", "+"]

print("Welcome!")
cap_input = int (input("How many captial letter you want? "))
low_input = int (input("How many lower case letter you want? "))
num_input = int (input("How many numbers you want? "))
sym_input = int (input("How many symbols you want? "))

password = ""
for i in range (0,cap_input):
    password += letters_upper[random.randint(0,25)]

for i in range (0,low_input):
    password += letters_lower[random.randint(0,25)]

for i in range (0,num_input):
    password += numbers[random.randint(0,9)]

for i in range (0,sym_input):
    password += symbols[random.randint(0,9)]

new_password = list(password)
random.shuffle(new_password)

def listToString(s):
    str1 = ""
    return (str1.join(s))

print(listToString(new_password))


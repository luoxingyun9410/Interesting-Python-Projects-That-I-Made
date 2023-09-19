# Different Types of variables
# string "Hello"
# int 88
# float 188.5
# boolean True False

# name = "Steve"[2] #string only
# print(name)

# num1 = int(input("Please enter the first number:"))
# num2 = int(input("Please enter the second number:"))
# print(num1 + num2)

# num_input = input("Please enter a two digit number:")
# print(float(num_input[0]) + float(num_input[1]))

# # next line \n
# print("I am Steven\nI love data")

# #f string
# age = 22
# height = 180.5
# is_male = True

# print(f"I am {age} years old, my height is {height}, is or not male: {is_male}")

height = float(input("Please enter your height (cm):\n"))
weight = float(input("Please enter your weight (kg):\n"))

height /= 100
bmi = weight / height**2
bmi = round(bmi, 1)
print(f"Your BMI is {bmi}")
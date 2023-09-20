# i = 1

# while i < 6:
#     print(87)
#     i +=1
# print("End")

# name = input("Guess my name ")

# while name != "Steve":
#     print("Wrong!")
#     name = input("Guess my name again ")
# print("Righttttt!")

use = True

while use:
    height = float(input("Please enter your height (cm):\n"))
    weight = float(input("Please enter your weight (kg):\n"))

    height /= 100
    bmi = weight / height**2
    bmi = round(bmi, 1)
    print(f"Your BMI is {bmi}")

    choice = input("Wanna calculate again? (Enter y or n)")

    if choice == "n":
        use = False
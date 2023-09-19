print("Welcome!")
print("(1) Calculate your BMI")
print("(2) Calculate your BMR")
print("(3) Calculate your TDEE")
option = int(input("Please choose your option (Enter 1 or 2 or 3):"))

def get_bmi(height,weight):
    return weight / height**2

def get_bmr(sex, height,weight,age):
    if sex == "M":
        return 88.362 + 13.397 * weight + 4.799 *height - 5.677 * age
    else:
        return 447.593 + 9.247 * weight + 3.098 * height - 4.330 * age
    
def get_tdee(sex, height,weight,age,choice):
    if choice == 1 :
        return get_bmr(sex, height,weight,age)*1.2
    if choice == 2 :
        return get_bmr(sex, height,weight,age)*1.375
    if choice == 3 :
        return get_bmr(sex, height,weight,age)*1.55
    if choice == 4 :
        return get_bmr(sex, height,weight,age)*1.725
    if choice == 5 :
        return get_bmr(sex, height,weight,age)*1.9


if option == 1:
    height = float(input("Please enter your height (cm):"))
    weight = float(input("Please enter your weight (kg):"))

    height /= 100
    bmi = get_bmi(height,weight)
    bmi = round(bmi, 1)
    print(f"Your BMI is {bmi}")

if option == 2:
    sex = input("Please enter your gender (Enter M or F):").upper()
    height = float(input("Please enter your height (cm):"))
    weight = float(input("Please enter your weight (kg):"))
    age = int(input("Please enter your age:"))

    bmr = get_bmr(sex, height,weight,age)
    bmr = round(bmr,2)
    print(f"Your BMR is {bmr}")

if option == 3:
    sex = input("Please enter your gender (Enter M or F):").upper()
    height = float(input("Please enter your height (cm):"))
    weight = float(input("Please enter your weight (kg):"))
    age = int(input("Please enter your age:"))
    print("Here are some index for your exercise level:\n")
    print("(1) No exercise")
    print("(2) Low intensity exercise")
    print("(3) Moderate intensity exercise")
    print("(4) High intensity exercise")
    print("(5) Crazy intensity exercise")
    choice = int(input("Please choose your daily exercise level (Enter 1~5):"))

    tdee = int(get_tdee(sex, height,weight,age,choice))
    print(f"Your TDEE is {tdee}")
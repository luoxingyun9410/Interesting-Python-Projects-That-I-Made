height = float(input("Please enter your height (cm):\n"))
weight = float(input("Please enter your weight (kg):\n"))

height /= 100
bmi = weight / height**2
bmi = round(bmi, 1)
if bmi < 18.5:
    print(f"Your BMI is {bmi} (underweight)")
elif 18.5 <= bmi < 24:
    print(f"Your BMI is {bmi} (healthy)")
elif 24 <= bmi < 27:
    print(f"Your BMI is {bmi} (overweight)")
elif 27 <= bmi < 30:
    print(f"Your BMI is {bmi} (light obesity)")
elif 30 <= bmi < 35:
    print(f"Your BMI is {bmi} (mid obesity)")
else:
    print(f"Your BMI is {bmi} (serious obesity)")
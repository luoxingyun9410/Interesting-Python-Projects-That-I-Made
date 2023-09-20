import random

print("Welcome!")
print("The answer is a number between 1~100 (You have 5 guesses)")

answer = random.randint(1,101)

i = 0

while True:
    i += 1
    if i > 5:
        print(f"The correct answer is {answer}")
        break
    print(f"This is No.{i} guess")
    user_input = input("Please enter your guess ")
    if user_input.isdigit():
        user_input = int(user_input)
    else:
        print("Numbers only!")
        continue
    if user_input > answer:
        print("Smaller")
    elif user_input < answer:
        print("Bigger")
    else:
        print("Correct!")
        break

# first_guess = int(input("Enter your first guess "))
# if first_guess == answer:
#     print("Correct!")
# elif first_guess < answer:
#     print("Bigger")
# else:
#     print("Smaller")
# second_guess = int(input("Enter your second guess "))
# if second_guess == answer:
#     print("Correct!")
# elif second_guess < answer:
#     print("Bigger")
# else:
#     print("Smaller")
# third_guess = int(input("Enter your third guess "))
# if third_guess == answer:
#     print("Correct!")
# elif third_guess < answer:
#     print("Bigger")
# else:
#     print("Smaller")
# fourth_guess = int(input("Enter your fourth guess "))
# if fourth_guess == answer:
#     print("Correct!")
# elif fourth_guess < answer:
#     print("Bigger")
# else:
#     print("Smaller")
# final_guess = int(input("Enter your final guess "))
# if final_guess == answer:
#     print("Correct!")
# else:
#     print(f"The correct answer is {answer}")
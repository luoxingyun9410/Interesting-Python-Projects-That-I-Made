import random

scissor = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''
option = input("Please enter rock (r), paper(p), scissors(s):")

if option == "r":
    print(rock)
if option == "s":
    print(scissor)
if option == "p":
    print(paper)

print("Machine's choice:")

all_options = ["r","p","s"]
machine_choice = random.choice(all_options)
if machine_choice == "r":
    print(rock)
if machine_choice == "s":
    print(scissor)
if machine_choice == "p":
    print(paper)

if (option == "r" and machine_choice == "p") or (option == "p" and machine_choice == "s") or (option == "s" and machine_choice == "r"):
    print("Machine won!")

elif (option == "r" and machine_choice == "r") or (option == "p" and machine_choice == "p") or (option == "s" and machine_choice == "s"):
    print("Even!")

else:
    print("We won!")
#     if machine_choice == "p":
#         print("Machine won!")
#     elif machine_choice == "s":
#         print("We won!")
#     else:
#         print("Even!")

# if option == "p" :
#     if machine_choice == "s":
#         print("Machine won!")
#     elif machine_choice == "r":
#         print("We won!")
#     else:
#         print("Even!")

# if option == "s" :
#     if machine_choice == "r":
#         print("Machine won!")
#     elif machine_choice == "p":
#         print("We won!")
#     else:
#         print("Even!")
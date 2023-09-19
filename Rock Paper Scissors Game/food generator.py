# scores = [80,40,60,80,80]

# print(scores[2])

# scores.append(88)
# print(scores)

# num = scores.count(80)
# print(num)

import random

# food = ["Rice","Noodles","Dumplings","Pasta", "BBQ"]

# option = random.choice(food)
# print(option)

print("Welcome to food generator!")

pick = input("Please enter what you want for tonight:\n")
food = pick.split(",")
option = random.choice(food)
print(option)
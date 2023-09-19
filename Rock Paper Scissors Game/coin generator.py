import random

num = random.randint(1, 100)
print(num)

coin = random.randint(0,1)
if coin == 0:
    print("UP")
else:
    print("DOWN")
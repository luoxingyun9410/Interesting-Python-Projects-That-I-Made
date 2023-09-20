# for item in ["I am Steve","I am Jess","I am Juan"]:
#     print(item)

# print("End")

# scores = [50,60,70,80,90,100]

# sum = 0
# for score in scores:
#     sum += score
# print(sum)

scores = input("Please enter all marks (use , to separate)\n")

scores = scores.split(",")

maximun = 0
for i in scores:
    if int(i) > maximun:
        maximun = int(i)
print(f"Highest mark is {maximun}")

sum = 0
for i in range(1,51,1):
    sum += i
print(sum)

sum = 0
for i in range(2,101,2):
    sum += i
print(sum)
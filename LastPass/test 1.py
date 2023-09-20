sum = 0

with open("123.txt","r") as file:
    for i in file:
        sum += int(i)

print(sum)
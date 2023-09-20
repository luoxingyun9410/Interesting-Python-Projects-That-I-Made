a = 1
def abc():
    # global a
    a = 2
    print(f"Internal number is {a}")

abc()
print(f"External number is {a}")

def fun1(a,b):
    c = a + b

for i in range(1,6):
    print(i)
    if i ==3:
        break
    i += 1
print("BREAK")

highest = 0
for score in [20,30,40,50,80,10]:
    if score==100:
        highest = 100
        break
    else:
        if score > highest:
            highest = score
print(highest)
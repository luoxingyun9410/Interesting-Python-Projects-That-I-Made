def print_info(name, age, height):
    print(f"I am {name}, I am {age},I am {height}")
    print(name + " learning data")

# print_info("AK", 26, 188)

def find_max(A,B,C):
    if type(A) != int or type(B) != int or type(C) != int:
        return "Wrong type"
    if A > B > C or A > C > B:
        return A 
    if B > A > C or B > C > A:
        return B 
    if C > A > B or C > B > A:
        return C 

max = find_max(30,40,50.5)
print(max)
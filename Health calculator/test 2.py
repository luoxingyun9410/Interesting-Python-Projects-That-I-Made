def find_max(A,B,C):
    if type(A) != int or type(B) != int or type(C) != int:
        return "Wrong type"
    if A > B > C or A > C > B:
        return A 
    elif B > A > C or B > C > A:
        return B 
    else:
        return C

max = find_max(30,40,50)
print(max)

def find_min(A,B,C):
    if type(A) != int or type(B) != int or type(C) != int:
        return "Wrong type"
    if A < B < C or A < C < B:
        return A 
    elif B < A < C or B < C < A:
        return B 
    else:
        return C 


def max_min(A,B,C):
    if type(A) != int or type(B) != int or type(C) != int:
        return "Wrong type"
    else:
        return find_max(A,B,C) - find_min(A,B,C)
    
find_gap = max_min(-80,40,50)
print(find_gap)
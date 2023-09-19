print("Welcome!")
print("(1) A Ramen $220")
print("(2) B Ramen $240")
print("(3) C Ramen $280")
flavour = input("Please choose your flavour (Enter A or B or C):").upper()
size = input("Large or normal, C ramen +$50 other flavours +$30 (Enter Y or N)").upper()
is_egg = input("Egg +$30 (Enter Y or N)").upper()
is_meat = input("Meat +$60 (Enter Y or N)").upper()
if flavour == "A":
    if size =="Y":
        if is_egg =="Y":
            if is_meat == "Y":
                print("After your discount, Your ramen is $320")
            else:
                print("Your ramen is $280")
        else:
            if is_meat == "Y":
                print("Your ramen is $310")
            else:
                print("Your ramen is $250")
    else:
        if is_egg =="Y":
            if is_meat == "Y":
                print("Your ramen is $310")
            else:
                print("Your ramen is $250")
        else:
            if is_meat == "Y":
                print("Your ramen is $280")
            else:
                print("Your ramen is $220")            
if flavour == "B":
    if size =="Y":
        if is_egg =="Y":
            if is_meat == "Y":
                print("After your discount, Your ramen is $340")
            else:
                print("Your ramen is $300")
        else:
            if is_meat == "Y":
                print("Your ramen is $330")
            else:
                print("Your ramen is $270")
    else:
        if is_egg =="Y":
            if is_meat == "Y":
                print("Your ramen is $330")
            else:
                print("Your ramen is $270")
        else:
            if is_meat == "Y":
                print("Your ramen is $300")
            else:
                print("Your ramen is $240") 
if flavour == "C":
    if size =="Y":
        if is_egg =="Y":
            if is_meat == "Y":
                print("After your discount, Your ramen is $400")
            else:
                print("Your ramen is $360")
        else:
            if is_meat == "Y":
                print("Your ramen is $390")
            else:
                print("Your ramen is $330")
    else:
        if is_egg =="Y":
            if is_meat == "Y":
                print("Your ramen is $370")
            else:
                print("Your ramen is $310")
        else:
            if is_meat == "Y":
                print("Your ramen is $340")
            else:
                print("Your ramen is $280") 

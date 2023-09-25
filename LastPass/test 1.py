# sum = 0

# with open("C:/Users/steven.luo/Documents/Python project/Interesting-Python-Projects-That-I-Made/LastPass/123.txt","r") as file:
#     for i in file:
#         sum += int(i)

# print(sum)

import json
password = [1,2,3,4,5]

with open("password.json","w") as f:
    f.write(json.dumps(password))
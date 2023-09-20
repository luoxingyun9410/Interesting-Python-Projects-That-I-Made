import random

eng_dic = {
    "蘋果": "apple",
    "香蕉": "banana",
    "貓": "cat",
    "狗": "dog",
    "蛋": "egg",
    "食物": "food",
    "遊戲": "game",
    "手": "hand",
    "冰": "ice",
    "果醬": "jam",
    "國王": "king",
    "標籤": "label",
    "郵件": "mail",
    "脖子": "neck",
    "油": "oil",
    "豬": "pig",
    "皇后": "queen"
}

num_input = int(input("How many questions fot today?"))

score = 0
for i in range(1, num_input+1):

    questions = random.choice(list(eng_dic.keys()))
    print(f"No.{i} question")
    ans = input(f"What's the answer for {questions}")
    if ans == eng_dic[questions]:
        print("Correct!")
        score +=1
    else:
        print(f"Wrong~ the right answer is {eng_dic[questions]}")

print(f"You've answered {score} question correct!")
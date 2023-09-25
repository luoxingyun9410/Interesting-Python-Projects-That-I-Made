# class Phone:
#     def __init__(self, number, price, waterproof, power) -> None:
#         self.number = number
#         self.price= price
#         self.waterproof= waterproof
#         self.power = power

#     def play(self, num):
#         self.power -= num
#         if self.power < 0 :
#             self.power = 0

# phone1 = Phone("123",8000,True,60) #phone1 is an object under Phone class
# print(phone1.number)
# print(phone1.price)
# print(phone1.waterproof)
# print(phone1.power)
# phone1.play(10)
# print(phone1.power)
# phone2 = Phone("123456",8600,True,80)
# print(phone2.number)
# print(phone2.price)
# print(phone2.waterproof)
# phone3 = Phone("12345678",6000,False,150)
# print(phone3.number)
# print(phone3.price)
# print(phone3.waterproof)

class Question:
    def __init__(self,description,answer) -> None:
        self.description = description
        self.answer = answer

    def ask(self):
        ans = input(self.description)
        if ans == self.answer:
            return True
        else:
            return False

# question1 = Question("What is 1+1=?\n(a)2\n(b)3\n(c)4\n", "a")
# if question1.ask():
#     print("CORRECT")
# else:
#     print("Wrong")


import random
import json

class QuestionGame:
    def __init__(self,questions) -> None:
        self.questions = questions
        self.scores = 0

    def random_pick(self,num):
        random_questions = random.sample(self.questions, num)
        return random_questions

    def play(self):
        random_quesions = self.random_pick(5)
        for question in random_quesions:
            if question.ask():
                self.scores += 1
                print("Correct")
            else:
                print(f"Wrong, the correct answer is {question.answer}")
        print(f"Your score is {self.scores}")
    
with open("C:/Users/steven.luo/Documents/Python project/Interesting-Python-Projects-That-I-Made/Answer questions game/questions.json","r",encoding="utf-8") as f:
    questions_list = json.loads(f.read())
print(questions_list)

questions = []

for question in questions_list:
    des = question["description"]
    ans = question["answer"]
    q = Question(des,ans)
    questions.append(q)

question_game = QuestionGame(questions)
question_game.play()

# question1 = Question("What is 1+1=?\n(a)2\n(b)3\n(c)4\n", "a")
# question2 = Question("What is 2+2=?\n(a)2\n(b)3\n(c)4\n", "c")
# question3 = Question("What is 4+4=?\n(a)7\n(b)8\n(c)9\n", "b")
# questions = [question1,question2,question3]
# question_game = QuestionGame(questions)
# question_game.play()
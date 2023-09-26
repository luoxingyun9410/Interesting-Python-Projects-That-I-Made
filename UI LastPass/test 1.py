# def fun(a, b, c):
#     print(a,b,c)

# fun(a=1,b=2,c=3)

# def add(*nums):
#     total = 0
#     for num in nums:
#         total += num
#     return total

# print(add(1,2,3,4))

# def add(**nums):
#     total = 0
#     for num in nums:
#         # print(num)
#         # print(nums[num])
#         total += nums[num]
#     return total

# print(add(num1=1,num2=2))

from tkinter import Canvas, Tk
from PIL import Image, ImageTk

window = Tk()

img = ImageTk.PhotoImage(file="C:/Users/steven.luo/Documents/Python project/Interesting-Python-Projects-That-I-Made/UI LastPass/p10543523_i_h10_ag.jpg")
window.iconphoto(True, img)
canvas = Canvas(width=1080,height=720)
canvas.create_image(540,360,image = img)
canvas.pack()

window.mainloop()
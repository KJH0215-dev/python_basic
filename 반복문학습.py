"""반복문 학습용 파일"""


"""a= int(input("숫자를 입력하세요:"))
b=0
for i in range(1, a+1):
    b=b+i
    print(b)"""
import turtle
t = turtle.Turtle()
t.shape("turtle")
t.color("red")
for i  in range(360):
    t.left(30)
    t.forward(10)
    t.right(30)
    t.forward(10)
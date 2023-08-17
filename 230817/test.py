# print("Hello Python!")
# # ctrl + F5
# a=1
# print(type(a))
# b=str(a)
# print(type(b))
# # 출력 형식 f 포맷 스트링
# print(f"test a 출력: {a}")
# # 코틀린에있는 이것과 비슷. Log.d("lys","출력하기 a : ${a}")
# print("출력형식 %d" %(a))

#ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ

#input() : 터미널에서, 문자열을 입력하는 형식
# email = input("이메일을 입력해주세용 : ")
# print(f"입력된 이메일은 : {email}")

#ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ

#터틀 구글에 검색하면 라이브러리관련 내용 볼수있음
# import turtle
# turtle.shape('turtle')
# turtle.forward(200)
# turtle.right(90)
# turtle.forward(200)
# turtle.right(90)
# turtle.forward(200)
# turtle.right(90)
# turtle.forward(200)
# turtle.done()

#ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ

# import turtle
# myT = None
# myT = turtle.Turtle()
# myT.shape('turtle') #"turtle", "arrow", "circle", "square" 등
# for i in range(0, 4) :
#     myT.forward(200)
#     myT.right(90)
# turtle.done()


#ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
import turtle
import random


def screenLeftClick(x, y):
    global r, g, b
    r = random.random()
    g = random.random()
    b = random.random()

    turtle.color(r, g, b)
    turtle.pencolor((r, g, b))
    turtle.pendown()

    tSize = random.randrange(1, 10)

    turtle.shapesize(tSize)
    turtle.stamp()
    turtle.goto(x, y)
    turtle.left(random.randrange(1, 360))


def screenRightClick(x, y):
    turtle.penup()
    turtle.goto(x, y)


def screenMidClick(x, y):
    global r, g, b
    tSize = random.randrange(1, 10)
    turtle.shapesize(tSize)
    r = random.random()
    g = random.random()
    b = random.random()
    print(f"랜덤한 색상의 값 조회: 0~255 , r : {r}, g : {g}, b : {b}")


pSize = 10
r, g, b = 0.0, 0.0, 0.0


turtle.title('거북이로 그림 그리기')
turtle.shape('turtle')
turtle.pensize(pSize)

turtle.onscreenclick(screenLeftClick, 1)
turtle.onscreenclick(screenMidClick, 2)
turtle.onscreenclick(screenRightClick, 3)

turtle.done()
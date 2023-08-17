# 실습)
# 1. 터틀 함수 이용해서, 자기 이름도 그려보고,
# 2. 추가- 별 그려보기. 등. 친해지기. 재미 붙이기.


import turtle



def  screenLeftClick(x, y):    
      turtle.forward(10)
def  screenMidClick(x, y):   
      turtle.forward(10)
def  screenRightClick(x, y):   
      turtle.forward(10)

def name():
      turtle.penup()
      turtle.goto(-150,150)
      turtle.pendown()
      turtle.circle(50)
      turtle.penup()
      turtle.goto(-50,300)
      turtle.pendown()
      turtle.right(90)
      turtle.forward(250)

      turtle.penup()
      turtle.goto(0,150)
      turtle.pendown()
      turtle.circle(25)    

      



  

turtle.onscreenclick(screenLeftClick, 1)
turtle.onscreenclick(screenMidClick, 2)
turtle.onscreenclick(screenRightClick, 3)


name()


turtle.done()

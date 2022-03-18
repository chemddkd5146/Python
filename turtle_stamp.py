import random
import turtle

tSize = 0
r,g,b = 0.0, 0.0, 0.0


def screenLeftClick(x,y):
     tSize = random.randrange(2,10)
     turtle.shapesize(tSize)
     r = random.random()
     g = random.random()
     b = random.random()
     turtle.color((r, g, b))
     tAngle = random.randrange(0, 360)

     turtle.penup()
     turtle.goto(x,y)
     turtle.left(tAngle)
     turtle.stamp()

turtle.shape('turtle')
turtle.onscreenclick(screenLeftClick,1)
turtle.done()
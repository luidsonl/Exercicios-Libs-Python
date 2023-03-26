import turtle
import math


brush = turtle.Turtle()


def drawPetal(t, radius, angle):# O angle indica o ângulo da pétala
    
    for i in range(2):
        t.circle(radius, angle)
        t.lt(180-angle)

def drawFlower(t, numberPetals, radious, angle):
    for i in range(numberPetals):
        drawPetal(t, radious, angle)
        t.lt(360.0/numberPetals)

def drawTriangle(t, length):
    
    for i in range(3):
        t.fd(length)
        t.lt(120)

def drawTriangleFlower(t, numberTriangles, length):
    for i in range(numberTriangles):
        drawTriangle(t,length)
        t.lt(360.0/numberTriangles)


def flower1():
    turtle.bgcolor('black')#deixa o fundo preto
    brush.color('red')
    drawFlower(brush, 10, 200, 90)
    brush.color('green')
    drawFlower(brush, 20, 100, 50)
    brush.color('yellow')
    drawTriangleFlower(brush,10,20)

flower1()

turtle.done()
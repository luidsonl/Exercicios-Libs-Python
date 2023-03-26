import turtle

writer = turtle.Turtle()
writer.hideturtle()
writer.speed(10)

posX = -300
posY = 0
writer.penup()
writer.setposition(posX, posY)
writer.pendown()

def updatePosition():
    global posX
    writer.penup()
    posX = posX + 40
    writer.setposition(posX, 0)
    writer.setheading(0)
    writer.pendown()

def drawA():
    writer.lt(75)
    writer.fd(50)
    writer.lt(-150)
    writer.fd(50)
    writer.lt(180)
    writer.fd(25)
    writer.lt(75)
    writer.fd(14)
    updatePosition()

def drawB():
    writer.lt(90)
    writer.fd(48)
    writer.lt(90)
    writer.circle(12,-180)
    writer.lt(180)
    writer.circle(12,-180)
    updatePosition()

def drawC():
    writer.penup()
    writer.setposition(posX + 18, 0)
    writer.pendown()
    writer.circle(24,-180)
    updatePosition()

def drawD():
    
    writer.lt(90)
    writer.fd(50)
    writer.lt(-90)
    writer.circle(-25, 180)
    updatePosition()

def drawI():
    writer.penup()
    writer.setposition(posX + 18, 0)
    writer.pendown()
    writer.lt(90)
    writer.fd(50)
    updatePosition()

def drawL():
    writer.penup()
    writer.setposition(posX + 25, 0)
    writer.pendown()
    writer.lt(180)
    writer.fd(30)
    writer.lt(-90)
    writer.fd(50)
    updatePosition()

def drawN():
    writer.lt(90)
    writer.fd(50)
    writer.lt(-160)
    writer.fd(55)
    writer.lt(160)
    writer.fd(50)
    updatePosition()


def drawU():
    writer.penup()
    writer.setposition(posX, 50)
    writer.pendown()
    writer.lt(-90)
    writer.fd(37)
    writer.circle(12, 180)
    writer.fd(37)
    updatePosition()

def drawO():
    writer.penup()
    writer.setposition(posX+ 10, 0)
    writer.pendown()
    writer.circle(15,90)
    writer.fd(17)
    writer.circle(15,90)
    writer.circle(15,90)
    writer.fd(17)
    writer.circle(15,90)
    updatePosition()

def drawS():
    writer.penup()
    writer.setposition(posX- 5, 0)
    writer.pendown()
    writer.fd(15)
    writer.circle(12,180)
    writer.circle(-12,180)
    writer.fd(15)
    updatePosition()



drawL()
drawU()
drawI()
drawD()
drawS()
drawO()
drawN()





turtle.done()
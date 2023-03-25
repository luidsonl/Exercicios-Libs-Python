import turtle
import math


# Criando quadrado
def printSquare(length):
    square = turtle.Turtle()
    #Desenhando quadrado
    for i in range(4):
        square.fd(length)
        square.lt(90)

    turtle.done()

# Criando retângulo
def printRetangle(lengthX, lengthY):
    retangle = turtle.Turtle()
    # Desenhando retangulo
    for i in range(4):
        if i%2 == 0:
            retangle.fd(lengthX)
        else:
            retangle.fd(lengthY)

        retangle.lt(90)

    turtle.done()

# Criando polígono regular
def printPolygon(sides, length):
    polygon = turtle.Turtle()

    angle = 360/sides # A soma dos angulos externos do polígono regular é 360
    
    for i in range(sides):
        
        polygon.fd(length)
        polygon.lt(angle)

    turtle.done()

# Desenhando circuncerencias usando polígonos
def arc(r, angle):
    polygon = turtle.Turtle()
    arc_length = 2 * math.pi * r * angle / 360 #Calcula o tamanho do arco a partir do raio e do ângulo
    n = int(arc_length / 3) + 1 #Calcula o número de segmentos que serão gerados
    step_length = arc_length / n # Calcula o tamanho de cada segmento
    step_angle = angle / n  #Calcula o ângulo de inclinação dos segmentos
    for i in range(n):
        polygon.fd(step_length)
        polygon.lt(step_angle)
        turtle.done()

# Criando círculo
def printCircle(radius):
    circle = turtle.Turtle()
    circle.circle(radius)
    turtle.done()

# Criando arco
def printArch(radius, angle):
    arch = turtle.Turtle()
    arch.circle(radius, angle)
    turtle.done()

# Criando um menu

print('Informe a figura que deseja desenhar:\n')
print('0 - sair')
print('1 - quadrado')
print('2 - retângulo')
print('3 - polígono regular')
print('4 - círculo')
print('5 - arco')
opcao = int(input())


if opcao == 1:
    print('Informe o comprimento dos lados do quadrado')
    length = int(input())
    printSquare(length)

elif opcao ==2:
    print('Informe o tamano dos lados do retangulo')
    print('Informe o X')
    lengthX = int(input())
    print('Informe o Y')
    lengthY = int(input())
    printRetangle(lengthX,lengthY)

elif opcao ==3:
    print('Informe o número de arestas do polígono')
    sides = int(input())
    print('Informe o comprimento das arestas do polígono')
    length = int(input())
    printPolygon(sides,length)

elif opcao ==4:
    print('Informe o raio do círculo')
    radius = int(input())
    printCircle(radius)

elif opcao == 5:
    print('Informe o raio')
    radius = int(input())
    print ('Informe a fração do círculo - 360 para um círculo completo')
    angle = int(input())
    printArch(radius, angle)
    #arc(radius, angle)

    
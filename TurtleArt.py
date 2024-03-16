#Importing Turtle
import turtle

#Naming our turtle
don = turtle.Turtle()
don.pencolor("black")
don.pensize(1)
don.speed(1000)

for x in range(5):
    for x in range(5):
        don.forward(50)
        don.right(30)
        for y in range(10):
            don.forward(10)
            don.right(20)
            for y in range(10):
                don.forward(10)
                don.right(30)


turtle.done()

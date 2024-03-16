#Importing Turtle
import turtle

#Naming our turtle
don = turtle.Turtle()

#Set up turtle
don.pencolor("black")
don.pensize(3)

#Shell
don.fillcolor("#ff00aa")
don.begin_fill()
don.setx(-100)
don.left(60)
don.forward(60)
don.right(30)
don.forward(50)
don.right(30)
don.forward(60)
don.right(30)
don.forward(50)
don.right(30)
don.forward(60)
don.right(120)
don.forward(110)
don.penup()
don.end_fill()

#Head
don.fillcolor("#d6a7c6")
don.setx(-100)
don.begin_fill()
don.pendown()
don.right(30)
don.forward(30)
don.right(30)
don.forward(30)
don.right(60)
don.forward(20)
don.right(60)
don.forward(30)
don.right(60)
don.forward(35)
don.right(60)
don.forward(30)
don.penup()
don.end_fill()

#Legs
#Left
don.setx(-60)
don.sety(0)
don.fillcolor("#f5d7eb")
don.pendown()
don.begin_fill()
don.left(30)
don.forward(30)
don.left(90)
don.forward(20)
don.left(90)
don.forward(30)
don.left(90)
don.forward(20)
don.penup()
don.end_fill()

#Right
don.setx(60)
don.sety(0)
don.fillcolor("#f5d7eb")
don.pendown()
don.begin_fill()
don.left(90)
don.forward(30)
don.left(90)
don.forward(20)
don.left(90)
don.forward(30)
don.left(90)
don.forward(20)
don.penup()
don.end_fill()

#Eye
don.setx(-120)
don.sety(40)
don.dot(5, "blacK")

don.hideturtle()

turtle.done()
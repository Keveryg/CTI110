#CTI-110
#P4LAB1b - Extra Credit
#Raul Gonzales
#11-8-23
#

#Importing turtle module
import turtle

#Declaring variable and attributes
t1 = turtle.Turtle()
t1.color("green")
t1.pensize(2)

#Moving pen to left of screen
t1.penup()
t1.goto(-50, 0)
t1.pendown()

#Creating first initial "R"
t1.left(90)
t1.forward(100)
t1.right(90)
t1.forward(50)
t1.right(90)
t1.forward(50)
t1.right(90)
t1.forward(50)
t1.left(135)
t1.forward(70)

#Moving pen location
t1.penup()
t1.goto(150, 90)
t1.pendown()

#Creating second initial "G"
t1.setheading(140)
t1.circle(50, 220)
t1.forward(35)
t1.left(90)
t1.forward(50)
t1.left(90)
t1.forward(40)

#Will keep turtle module window open until user closes window manually
turtle.exitonclick()

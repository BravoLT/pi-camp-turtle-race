
import turtle
from random import randint

turtle.speed(100)
turtle.penup()
turtle.goto(-140, 100)

for step in range(15):
  turtle.write(step, align='center')
  turtle.right(90)
  turtle.forward(10)
  turtle.pendown()

  for dash in range(15):
    turtle.forward(7)
    turtle.penup()
    turtle.forward(3)
    turtle.pendown()

  turtle.penup()
  turtle.backward(160)
  turtle.left(90)
  turtle.forward(20)

red = turtle.Turtle()
red.color('red')
red.shape('turtle')
red.penup()
red.goto(-160, 100)
red.pendown()

blue = turtle.Turtle()
blue.color('blue')
blue.shape('turtle')
blue.penup()
blue.goto(-160, 80)
blue.pendown()

green = turtle.Turtle()
green.color('green')
green.shape('turtle')
green.penup()
green.goto(-160, 60)
green.pendown()

yellow = turtle.Turtle()
yellow.color('yellow')
yellow.shape('turtle')
yellow.penup()
yellow.goto(-160, 40)
yellow.pendown()

for turn in range(100):
  red.forward(randint(1, 5))
  blue.forward(randint(1, 5))
  green.forward(randint(1, 5))
  yellow.forward(randint(1, 5))



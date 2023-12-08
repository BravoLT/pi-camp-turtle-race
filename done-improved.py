
import turtle
from random import randint


players=[]


def create_turtle(color, start):
  instance = turtle.Turtle()
  instance.color(color)
  instance.shape('turtle')
  instance.penup()
  instance.goto(-240, start)
  instance.pendown()
  instance.right(360)

  players.append(instance)


turtle.speed(10)
turtle.penup()
turtle.goto(-200, 200)

for step in range(20):
  turtle.write(step, align='center')
  turtle.right(90)
  turtle.forward(10)
  turtle.pendown()

  for dash in range(30):
    turtle.forward(10)
    turtle.penup()
    turtle.forward(5)
    turtle.pendown()

  turtle.penup()
  turtle.forward(20)

  turtle.pendown()
  turtle.write(step, align='center')
  turtle.penup()

  turtle.backward(480)
  turtle.left(90)
  turtle.forward(20)

create_turtle('red', 180)
create_turtle('blue', 140)
create_turtle('green', 100)
create_turtle('yellow', 60)
create_turtle('orange', 20)
create_turtle('maroon', -20)
create_turtle('purple', -60)
create_turtle('pink', -100)

for turn in range(100):
  for p in players:
    p.forward(randint(1, 10))

input('press enter to quit')


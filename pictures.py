import turtle
from random import *

sven = turtle.Turtle()
sven.speed(0)

screen = turtle.Screen()
screen.colormode(255)

screen.bgcolor(155,0,0)  #(R,G,B) tuple  (All RGB must be between 0 - 255)
sven.color(0,255,0)

for i in range(200):
      sven.forward(200)
      sven.right(92)
      sven.backward(100)
      sven.left(273)
      sven.color(randint(0,255), randint(0,255), randint(0,255))
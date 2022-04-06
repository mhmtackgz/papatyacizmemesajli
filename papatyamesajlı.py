import turtle
from turtle import *
from colorsys import *
def yazdır():
 turtle.color('RED')
 style=('Verdana',20,'bold')
 turtle.write('Doğum Günün Kutlu Olsun <3',font=style,align='center')
 turtle.hideturtle()
 turtle.done()
A=0.8
bgcolor("black")
speed(0)

for i in range(60):
    speed(0)
    renkler=hsv_to_rgb(A,1,1)
    A+=0.005
    color(renkler,renkler)
    begin_fill()
    circle(270 -i,90)
    lt(90)
    circle(270-i,90)
    lt(10)
    speed(0)
    end_fill()
yazdır()

done()
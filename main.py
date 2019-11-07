import math
from turtle import *
class Square:
    def __init__(self, x, y, l, ang, color):
        self.x=x
        self.y =y
        self.color = color
        self.ang = ang
        self.l = l
    def draw(self):
        t = Turtle()
        t.color(self.color)
        t.penup()
        t.goto(self.x, self.y)
        t.pendown()
        t.begin_fill()
        t.left(self.ang)
        for i in range(3):
            t.forward(self.l)
            t.right(90)
        t.end_fill()
class Rhombus:
    def __init__(self, x, y, l, ang, color):
        self.l = l
        self.x = x
        self.y = y
        self.ang = ang
        self.color = color
    def draw(self):
        t = Turtle()
        t.color(self.color)
        t.penup()
        t.goto(self.x, self.y)
        t.pendown()
        t.begin_fill()
        t.left(self.ang + 60)
        for k in range(2):
            t.forward(self.l)
            t.right(60)
            t.forward(self.l)
            t.right(120)
        t.end_fill()
        #t.screen.mainloop()
class Triangle:
    def __init__(self, x, y, l,ang, color):
        self.l = l
        self.x = x
        self.y = y
        self.ang = ang
        self.color = color
    def draw(self):
        t = Turtle()
        t.color(self.color)
        t.penup()
        t.goto(self.x, self.y)
        t.pendown()
        t.begin_fill()
        t.left(self.ang + 45)
        t.forward(self.l)
        t.right(90)
        t.forward(self.l)
        t.right(135)
        t.forward(self.l * math.sqrt(2))
        t.end_fill()
def flower( x, y, l, c1, c2, c3):
    ang = 0
    c = [c1, c2, c3, c1, c2, c3]
    for i in range(6):
        yield Rhombus(x, y, l, ang, c[i])
        ang += 60

def house( x, y, l1, l2, c1, c2, c3):
    l =  (l1 - 2 * l2) / 4
    ll = (l1-l2)/2
    yield Square(x, y, l1, 0, c1)
    yield Square(x+l, y-ll, l2, 0, c2)
    yield Square(x + 3*l + l2, y-ll, l2, 0, c2)
    yield Triangle(x, y, l1/math.sqrt(2), 0, c3)

def fish( x, y, l1, l2, l3, c1, c2, c3):
    l = l1*math.cos(math.radians(30))
    ll = l2*math.cos(math.radians(30))
    yield Rhombus(x, y, l1, -30, c1)
    yield Triangle(x + l - l2/2, y + l1/2 + ll , l2, -105, c2)
    yield Triangle(x + l - ll, y - l1/2 +l2/2, l2, -75,c2)
    yield Triangle(x- l2, y + l2, l2, -45, c2)
    yield Triangle(x , y , l2, -135, c2)
    yield Square(x + l*1.5, y, l3,  45, c3)
#flower
#house
#fish
for f in fish(-200, 100, 100, 50, 10, "gray", "red", "yellow"):
    f.draw()
for h in house(100, 100, 100, 30, "orange", "blue", "red"):
    h.draw()
for f in flower(-150, -150, 60, "green", "yellow", "blue"):
    f.draw()

t = Turtle()
t.screen.mainloop()

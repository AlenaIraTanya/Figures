# Case 1
#
import turtle
class Square:
    def __init__(self, x, y, size, color, angle):
        self.x=x
        self.y =y
        self.color = color
        self.angle = angle
    def picsgab(self):
        turtle.penup()
        turtle.goto(x, y)
        turtle.pendown()
        turtle.left(angle)
        for i in range(3):
            turtle.forward(size)
            turtle.tight(90)
            turtle.root.mainloop()
square(100, 100, 100, 12, 13)

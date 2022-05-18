from turtle import Turtle

class Paddle(Turtle):

    def __init__(self,x_c,y_c):
        super().__init__()

        self.penup()
        self.shape("square")
        self.shapesize(5, 1)
        self.color('dodger blue')
        self.goto(x_c, y_c)

    def up(self):
        if self.ycor()<=240:
            self.goto(self.xcor(), self.ycor() + 20)

    def down(self):
        if self.ycor()>=-220:
            self.goto(self.xcor(), self.ycor() - 20)
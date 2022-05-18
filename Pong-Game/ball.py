from turtle import Turtle

class Ball(Turtle):

    def __init__(self):
        super().__init__()

        self.move = 2

        self.shape('circle')
        self.penup()
        self.setheading(45)
        self.color('white')

    def wall_bounce(self):
        head= self.heading()
        self.setheading(-head)

    def padd_bounce(self):
        head=self.heading()-360
        self.setheading(180+(-head))
        self.move+=0.1

    def reset(self,heading):
        self.goto(0,0)
        self.setheading(heading)
        self.move = 2


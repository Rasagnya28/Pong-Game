from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()

        self.l_score = 0
        self.r_score = 0

        self.scoreupdate()

    def scoreupdate(self):
        self.penup()
        self.hideturtle()
        self.color('white')
        self.goto(0, 280)
        self.pendown()
        self.pensize(3)
        self.goto(0, -270)

        self.penup()
        self.goto(-200, 200)
        self.write(self.l_score, align="center", font=("Courier", 70, "normal"))
        self.goto(200,200)
        self.write(self.r_score, align="center", font=("Courier", 70, "normal"))

    def miss(self,player):
        if player=="left":
            self.l_score+=1
        if player=="right":
            self.r_score+=1
        self.clear()
        self.scoreupdate()

    def stop_game(self):
        on=False




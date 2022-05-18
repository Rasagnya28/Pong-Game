from turtle import Turtle,Screen
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard

scr=Screen()
scr.bgcolor('black')
scr.setup(800,600)
scr.title("Pong")
scr.tracer(0)

l_padd=Paddle(-380,0)
r_padd=Paddle(370,0)

scr.listen()
scr.onkey(r_padd.up,"Up")
scr.onkey(r_padd.down,"Down")
scr.onkey(l_padd.up,"w")
scr.onkey(l_padd.down,"s")

ball=Ball()

sb=ScoreBoard()
on=True
while on:
    scr.update()
    ball.forward(ball.move)
    if ball.ycor()>=290 or ball.ycor()<=-280:
        ball.wall_bounce()

    if ball.distance(r_padd)<=51  and 360>ball.xcor()>=350 and r_padd.ycor()-50<=ball.ycor()<=r_padd.ycor()+50:
        ball.padd_bounce()

    if ball.distance(l_padd)<=51 and -365> ball.xcor()<=-360 and l_padd.ycor()-51<=ball.ycor()<=l_padd.ycor()+51:
        ball.padd_bounce()

    if ball.xcor()>=400:
        ball.reset(135)
        sb.miss('left')
    if ball.xcor()<=-400:
        ball.reset(45)
        sb.miss('right')


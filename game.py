import turtle

wn = turtle.Screen()
wn.title("Pong")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

#paddleA
paddle_a=turtle.Turtle()
paddle_a.color("white")
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.shapesize(stretch_wid=5,stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350,0)

#paddleB
paddle_b=turtle.Turtle()
paddle_b.color("white")
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.shapesize(stretch_wid=5,stretch_len=1)
paddle_b.penup()
paddle_b.goto(350,0)

#ball
ball=turtle.Turtle()
ball.color("white")
ball.speed(0)
ball.shape("circle")
ball.penup()
ball.goto(0,0)
ball.dx=0.2
ball.dy=-0.2

#pen
pen=turtle.Turtle()
pen.color("white")
pen.speed(0)
pen.hideturtle()
pen.penup()
pen.goto(0,260)
pen.write("Player 1:0",align="center",font=("Courier",14,"normal"))

#score
score_a=0
score_b=0


#moving the paddles

def paddle_a_up():
    y=paddle_a.ycor()
    y+=20
    paddle_a.sety(y)

def paddle_a_down():
    y=paddle_a.ycor()
    y-=20
    paddle_a.sety(y)

def paddle_b_up():
    y=paddle_b.ycor()
    y+=20
    paddle_b.sety(y)

def paddle_b_down():
    y=paddle_b.ycor()
    y-=20
    paddle_b.sety(y)

while True:
    wn.update()
    ball.setx(ball.xcor()+ball.dx)
    ball.sety(ball.ycor()+ball.dy)

    wn.listen()
    wn.onkeypress(paddle_a_up,"w")
    wn.onkeypress(paddle_a_down,"s")
    wn.onkeypress(paddle_b_up,"Up")
    wn.onkeypress(paddle_b_down,"Down")

    if ball.ycor()>290:
        ball.sety(290)
        ball.dy*=-1

    if ball.ycor()<-290:
        ball.sety(-290)
        ball.dy*=-1

    if ball.xcor()>390:
        ball.goto(0,0)
        ball.dx*=-1
        score_a+=1
        pen.clear()
        pen.write("Player 1:{} Player 2:{}".format(score_a,score_b),align="center",font=("Courier",14,"normal"))

    if ball.xcor()<-390:
        ball.goto(0,0)
        ball.dx*=-1
        score_b+=1
        pen.clear()
        pen.write("Player 1:{} Player 2:{}".format(score_a,score_b),align="center",font=("Courier",14,"normal"))

    if ball.xcor()>340 and ball.xcor()<350 and ball.ycor()<paddle_b.ycor()+40 and ball.ycor()>paddle_b.ycor()-40:
        ball.setx(340)
        ball.dx*=-1

    if ball.xcor()<-340 and ball.xcor()>-350 and ball.ycor()<paddle_a.ycor()+40 and ball.ycor()>paddle_a.ycor()-40:
        ball.setx(-340)
        ball.dx*=-1






# Simple pong game

import turtle

wn = turtle.Screen()
wn.title("Pong by Parv")
wn.bgcolor("black")
wn.setup(width=1000, height=500)
wn.tracer(0)

# Score
score_a = 0 
score_b = 0 

# Paddle A 
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(strech_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-400, 0)

# Paddle B 
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(strech_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(400, 0)

# Ball 
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("yellow")
ball.penup()
ball.goto(0, 0)
ball.dx = 2
ball.dy = 2

# Pen 
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 210)
pen.write("Player A: 0 Player B: 0", align="center", font=("Courier", 24, "normal"))



# Function 
def paddle_a_up():
    y = paddle_a.ycor()
    y +=20
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y -=20
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    y +=20
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y -=20
    paddle_b.sety(y)

# Keyboard binding 
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")

# Main game loop 
while True:
    wn.update()

    # Move the ball 
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)


    # Border Checking 
    if ball.ycor() > 240:
        ball.sety(240)
        ball.dy *= -1 

    if ball.ycor() < -240:
        ball.sety(-240)
        ball.dy *= -1 

    if ball.xcor() > 490:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1 
        pen.clear()
        pen.write("Player A: {} Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

    if ball.xcor() < -490:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
         pen.write("Player A: {} Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

    # Paddle and ball collisions 
    if (ball.xcor() > 440 and ball.xcor() < 450) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() -40)
        ball.setx(440)
        ball.dx *= -1 


    if (ball.xcor() > -440 and ball.xcor() < -450) and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() -40)
        ball.setx(-440)
        ball.dx *= -1


import turtle
import os
import random

# import winsound

speed = .4
paddle_a_score = 0
paddle_b_score = 0
width = 800
height = 600


win = turtle.Screen()
win.title("Pong")
win.bgcolor("black")
win.setup(width=width, height=height)
win.tracer(0)

# Defines pen to draw borders

top_border = turtle.Turtle()
top_border.color('white')
top_border.shape('square')
top_border.shapesize(stretch_wid=.25, stretch_len=width/5)
top_border.penup()
top_border.goto(0, height/2)

bottom_border = turtle.Turtle()
bottom_border.color('white')
bottom_border.shape('square')
bottom_border.shapesize(stretch_wid=.25, stretch_len=width/5)
bottom_border.penup()
bottom_border.goto(0, -height/2)

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.color("white")
paddle_a.shape("square")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.speed(0)
paddle_a.penup()
paddle_a.goto(-350, 0)

# Paddle B

paddle_b = turtle.Turtle()
paddle_b.color("white")
paddle_b.shape("square")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.speed(0)
paddle_b.penup()
paddle_b.goto(350, 0)

# Ball

ball = turtle.Turtle()
ball.color("white")
ball.shape("circle")
ball.speed(0)
ball.penup()
ball.goto(0, 0)
ball.dx = speed
ball.dy = speed

# Pen to draw score

pen = turtle.Turtle()
pen.color("white")
pen.penup()
pen.speed(0)
pen.hideturtle()
pen.goto(0, 250)
pen.write("Player A: " + str(paddle_a_score) + " Player B: " + str(paddle_b_score), align="center",
          font=("Courier", 24, "normal"), )


# move the paddles
def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)


def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)


def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)


def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)


# Key bindings
win.listen()
"""
win.onkeypress(paddle_a_up, "w")
win.onkeypress(paddle_a_down, "s")
"""
win.onkeypress(paddle_b_up, "Up")
win.onkeypress(paddle_b_down, "Down")

# Draw borders


# Main game loop
while True:
    win.update()

    # move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # AI for the paddle A
    ai_speed = random.random() + 1.5
    ai_start = random.random() * -10
    if ball.ycor() > paddle_a.ycor() and paddle_a.ycor() < 350 and ball.dx < 0 and ball.xcor() < ai_start:
        paddle_a.sety(paddle_a.ycor() + speed/ai_speed)
    if ball.ycor() < paddle_a.ycor() and paddle_a.ycor() > -350 and ball.dx < 0 and ball.xcor() < ai_start:
        paddle_a.sety(paddle_a.ycor() - speed/ai_speed)

    # enforce borders
    # Left

    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        os.system("aplay bounce.wav&")
        os.system("afplay bounce.wav&")
        # winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    # right

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        os.system("aplay bounce.wav&")
        os.system("afplay bounce.wav&")
        # winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    # top

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        paddle_a_score += 1
        # redraws the score when it changes
        pen.clear()
        pen.write("Player A: " + str(paddle_a_score) + " Player B: " + str(paddle_b_score), align="center",
                  font=("Courier", 24, "normal"), )

    # bottom

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        paddle_b_score += 1
        # redraws the score when it changes
        pen.clear()
        pen.write("Player A: " + str(paddle_a_score) + " Player B: " + str(paddle_b_score), align="center",
                  font=("Courier", 24, "normal"), )

    # sets boundries on the paddles
    # sets top for a

    if paddle_a.ycor() + 50 > 300:
        paddle_a.sety(250)

    # sets bottom for a

    if paddle_a.ycor() - 50 < -300:
        paddle_a.sety(-250)

    # sets top for b

    if paddle_b.ycor() + 50 > 300:
        paddle_b.sety(250)

    # sets bottom for b

    if paddle_b.ycor() - 50 < -300:
        paddle_b.sety(-250)

    # Paddle Collisions

    if 335 < ball.xcor() < 390 and 50 + paddle_b.ycor() > ball.ycor() > paddle_b.ycor() - 50:
        ball.setx(335)
        ball.dx *= -1
        os.system("aplay bounce.wav&")
        os.system("afplay bounce.wav&")
        # winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    if ball.xcor() < -335 and 50 + paddle_a.ycor() > ball.ycor() > paddle_a.ycor() - 50:
        ball.setx(-335)
        ball.dx *= -1
        os.system("aplay bounce.wav&")
        os.system("afplay bounce.wav&")
        # winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
    if paddle_a_score >= 10 or paddle_b_score >= 10:
        break
while True:
    if paddle_a_score == 10:
        pen.clear()
        pen.goto(0, 0)
        pen.write("Player A Wins!", align="center",
                  font=("Courier", 24, "normal"), )
    if paddle_b_score == 10:
        pen.clear()
        pen.goto(0, 0)
        pen.write("Player B Wins!", align="center",
                  font=("Courier", 24, "normal"), )

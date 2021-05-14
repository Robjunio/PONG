import turtle
# import os
from winsound import PlaySound, SND_ASYNC
from time import sleep


# Sound exit.
def sound(on_tap):
    if on_tap == 1:
        # os.system("afplay bounce.wav&")  # On MAC
        # os.system("aplay bounce.wav&")  # On Linux
        PlaySound("bounce.wav", SND_ASYNC)  # On Windows

    else:
        # os.system("afplay 258020_kodack_arcade-bleep-sound.wav&")
        # os.system("aplay 258020_kodack_arcade-bleep-sound.wav&")
        PlaySound("258020__kodack__arcade-bleep-sound.wav", SND_ASYNC)


# Draw paddle.
def draw_paddle(paddle, x, y):
    paddle.speed()
    paddle.shape("square")
    paddle.color("white")
    paddle.shapesize(stretch_wid=5, stretch_len=1)
    paddle.penup()
    paddle.goto(x, y)


# Hitbox of the paddle, and defining different reactions depending
# where the ball hits.
def hitbox(paddle):
    if ball.dy == 0:
        ball.dy = 10

    ball.dx *= -1

    if (paddle.ycor() + 35 < ball.ycor() <= paddle.ycor() + 50) or\
            (paddle.ycor() - 35 > ball.ycor() >= paddle.ycor() - 50):
        ball.dy *= -1

    elif paddle.ycor() + 5 >= ball.ycor() >= paddle.ycor() - 5:
        ball.dy = 0


# Draw screen.
screen = turtle.Screen()
screen.title("My Pong")
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.tracer(0)


# Defining the paddle 1.
paddle_1 = turtle.Turtle()
draw_paddle(paddle_1, -350, 0)

# Defining the paddle 2.
paddle_2 = turtle.Turtle()
draw_paddle(paddle_2, 350, 0)


# Draw the ball.
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 10
ball.dy = 10


# Points.
score_1 = 0
score_2 = 0


# head-up display score.
hud = turtle.Turtle()
hud.speed(0)
hud.shape("square")
hud.color("white")
hud.penup()
hud.hideturtle()
hud.goto(0, 260)
hud.write("0 : 0", align="center", font=("Press Start 2P", 24,
                                         "normal"))

# Move up.
def paddle_up(paddle):
    y = paddle.ycor()
    if y < 250:
        y += 30
    else:
        y = 250
    paddle.sety(y)


# Move down.
def paddle_down(paddle):
    y = paddle.ycor()
    if y > -250:
        y += -30
    else:
        y = -250
    paddle.sety(y)


# Movements paddle 1.
def paddle_1_up():
    paddle_up(paddle_1)


def paddle_1_down():
    paddle_down(paddle_1)


# Movements paddle 2.
def paddle_2_up():
    paddle_up(paddle_2)


def paddle_2_down():
    paddle_down(paddle_2)


# Mapping the keyboard.
screen.listen()
screen.onkeypress(paddle_1_up, "w")
screen.onkeypress(paddle_1_down, "s")
screen.onkeypress(paddle_2_up, "Up")
screen.onkeypress(paddle_2_down, "Down")

# Game menu
first_screen = turtle.Turtle()
first_screen.color("white")
first_screen.write("PONG", align="center", font=("Press Start 2P", 50,
                                                 "normal"))
sleep(2)
first_screen.clear()

# Time for start
for i in range(3, 0, -1):
    first_screen.write(i, align="center", font=("Press Start 2P", 42,
                                                "normal"))
    sleep(1)
    first_screen.clear()

first_screen.hideturtle()

delay = 0.05

while True:
    screen.update()
    sleep(delay)

    # Ball movements
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Collision with the upper wall.
    if ball.ycor() > 290:
        sound(1)
        ball.sety(290)
        ball.dy *= -1

    # Collision with the downer wall.
    if ball.ycor() < -280:
        sound(1)
        ball.sety(-280)
        ball.dy *= -1

    # Collision with the sides walls.
    if ball.xcor() > 390 or ball.xcor() < -390:
        if ball.xcor() > 390:
            score_1 += 1
        elif ball.xcor() < -390:
            score_2 += 1
        hud.clear()
        hud.write("{} : {}".format(score_1, score_2), align="center",
                  font=("Press Start 2P", 24, "normal"))
        sound(0)
        if ball.dy == 0:
            ball.dy = 10
        ball.goto(0, 0)
        delay = 0.04
        ball.dx *= -1

    # Collision with the paddle 1.
    if -370 < ball.xcor() < -330 and paddle_1.ycor() + 50 > ball.ycor() >\
            paddle_1.ycor() - 50:
        hitbox(paddle_1)
        ball.setx(-325)
        if delay > 0.001:
            delay /= 1.20

        sound(1)

    # Collision with the paddle 2.
    if 370 > ball.xcor() > 330 and paddle_2.ycor() + 50 > ball.ycor() >\
            paddle_2.ycor() - 50:
        hitbox(paddle_2)
        ball.setx(325)
        if delay > 0.001:
            delay /= 1.20

        sound(1)

    # Victory condition.
    if score_1 == 11 or score_2 == 11:
        letter_win = ''
        if score_1 == 11:
            letter_win = '< You Win!'
        elif score_2 == 11:
            letter_win = 'You Win! >'
        winner_letter = turtle.Turtle()
        winner_letter.speed(0)
        winner_letter.shape("square")
        winner_letter.color("white")
        winner_letter.penup()
        winner_letter.hideturtle()
        winner_letter.goto(0, 0)
        winner_letter.write(letter_win, align="center", font=("Press Start 2P", 24, "normal"))
        PlaySound("391539__mativve__electro-win-sound.wav", SND_ASYNC)
        sleep(3)
        break

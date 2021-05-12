# Jucimar Jr 2019
# pong em turtle python https://docs.python.org/3.3/library/turtle.html
# baseado em http://christianthompson.com/node/51
# fonte Press Start 2P https://www.fontspace.com/codeman38/press-start-2p
# som pontuação https://freesound.org/people/Kodack/sounds/258020/

import turtle
import os
from winsound import PlaySound, SND_ASYC

# desenhar raquete
def draw_paddle(paddle, x, y):
    return (paddle.speed(),
            paddle.shape("square"),
            paddle.color("white"),
            paddle.shapesize(stretch_wid=5, stretch_len=1),
            paddle.penup(),
            paddle.goto(x, y))


# desenhar tela
screen = turtle.Screen()
screen.title("My Pong")
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.tracer(0)

# variaveis para raquete 1
paddle_1 = turtle.Turtle()
paddle_1_function = draw_paddle(paddle_1, -350, 0)

# variaveis para raquete 2
paddle_2 = turtle.Turtle()
paddle_2_function = draw_paddle(paddle_2, 350, 0)

# desenhar bola
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 2
ball.dy = 2

# pontuação
score_1 = 0
score_2 = 0

# head-up display da pontuação
hud = turtle.Turtle()
hud.speed(0)
hud.shape("square")
hud.color("white")
hud.penup()
hud.hideturtle()
hud.goto(0, 260)
hud.write("0 : 0", align="center", font=("Press Start 2P", 24, "normal"))


# mover raquete 1
def paddle_1_down():
    y = paddle_1.ycor()
    if y > -250:
        y += -20
    else:
        y = -250
    paddle_1.sety(y)


def paddle_1_up():
    y = paddle_1.ycor()
    if y < 250:
        y += 20
    else:
        y = 250
    paddle_1.sety(y)


# mover raquete 2
def paddle_2_up():
    y = paddle_2.ycor()
    if y < 250:
        y += 20
    else:
        y = 250
    paddle_2.sety(y)


def paddle_2_down():
    y = paddle_2.ycor()
    if y > -250:
        y += -20
    else:
        y = -250
    paddle_2.sety(y)


# mapeando as teclas
screen.listen()
screen.onkeypress(paddle_1_up, "w")
screen.onkeypress(paddle_1_down, "s")
screen.onkeypress(paddle_2_up, "Up")
screen.onkeypress(paddle_2_down, "Down")

while True:
    screen.update()

    # movimentação da bola
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # colisão com parede superior
    if ball.ycor() > 290:
        os.system("afplay bounce.wav&")
        ball.sety(290)
        ball.dy *= -1

    # colisão com parede inferior
    if ball.ycor() < -280:
        os.system("afplay bounce.wav&")
        ball.sety(-280)
        ball.dy *= -1

    # colisão com paredes laterais
    if ball.xcor() > 390 or ball.xcor() < -390:
        if ball.xcor() > 390:
            score_1 += 1
        elif ball.xcor() < -390:
            score_2 += 1
        hud.clear()
        hud.write("{} : {}".format(score_1, score_2), align="center", font=("Press Start 2P", 24, "normal"))
        # Sound Exit
        os.system("afplay 258020__kodack__arcade-bleep-sound.wav&")  # On MAC
        os.system("aplay 258020__kodack__arcade-bleep-sound.wav&")  # On Linux
        PlaySound("258020__kodack__arcade-bleep-sound.wav", SND_ASYC)  # On Windows
        ball.goto(0, 0)
        ball.dx *= -1

    # colisão com raquete 1

    if -370 < ball.xcor() < -330 and paddle_1.ycor() + 50 > ball.ycor() > paddle_1.ycor() - 50:
        ball.dx *= -1
        ball.setx(-325)
        if ball.ycor() <= paddle_1.ycor() + 50 or ball.ycor() >= paddle_1.ycor() - 50:  # alterei aqui
            ball.dy *= -1  # alterei aqui
        # Sound Exit
        os.system("afplay afplay bounce.wav&")  # On MAC
        os.system("aplay afplay bounce.wav&")  # On Linux
        PlaySound("afplay bounce.wav", SND_ASYC)  # On Windows

    # colisão com raquete 2
    if 370 > ball.xcor() > 330 and paddle_2.ycor() + 50 > ball.ycor() > paddle_2.ycor() - 50:
        ball.dx *= -1
        ball.setx(325)
        if ball.ycor() <= paddle_2.ycor() + 50 or ball.ycor() >= paddle_2.ycor() - 50:  # alterei aqui
            ball.dy *= -1 
        # Sound Exit
        os.system("afplay afplay bounce.wav&")  # On MAC
        os.system("aplay afplay bounce.wav&")  # On Linux
        PlaySound("afplay bounce.wav", SND_ASYC)  # On Window

    # Anuncio de vitória
    time_for_close = 500
    if score_1 == 11 or score_2 == 11:
        while time_for_close > 0:
            letter_win = ''
            time_for_close -= 1
            if score_1 == 11:
                letter_win = '< venceu =)'
            elif score_2 == 11:
                letter_win = '=) venceu >>'
            winner_letter = turtle.Turtle()
            winner_letter.speed(0)
            winner_letter.shape("square")
            winner_letter.color("white")
            winner_letter.penup()
            winner_letter.hideturtle()
            winner_letter.goto(0, 0)
            winner_letter.write(letter_win, align="center", font=("Press Start 2P", 24, "normal"))

        if time_for_close == 0:
            break

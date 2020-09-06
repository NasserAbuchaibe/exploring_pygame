import turtle



windows = turtle.Screen()
windows.title("Nasser Pong")
windows.bgcolor("blue")
windows.setup(width=800, height=600)
windows.tracer(0)

score_a = 0
score_b = 0

""" left racket """
racket_a = turtle.Turtle()
racket_a.speed(0)
racket_a.shape("square")
racket_a.color("black")
racket_a.shapesize(stretch_wid=5, stretch_len=1)
racket_a.penup()
racket_a.goto(-350, 0)

""" right racket """
racket_b = turtle.Turtle()
racket_b.speed(0)
racket_b.shape("square")
racket_b.color("white")
racket_b.shapesize(stretch_wid=5, stretch_len=1)
racket_b.penup()
racket_b.goto(350, 0)

""" ball """
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("red")
ball.shapesize(1)
ball.penup()
ball.goto(0, 0)
ball.dx = 2
ball.dy = 2

""" score board """
board = turtle.Turtle()
board.speed(0)
board.color("white")
board.penup()
board.hideturtle()
board.goto(0, 260)
board.write("Player1: 0  Player2: 0", align="center",
            font=("courier", 24, "bold"))


""" brand """
brand = turtle.Turtle()
brand.speed(0)
brand.color("white")
brand.penup()
brand.hideturtle()
brand.goto(0, -260)
brand.write("Nasser's PONG", align="center",
            font=("courier", 50, "bold"))

""" functions to move the racket """
def racket_a_up():
    y = racket_a.ycor()
    y += 20
    racket_a.sety(y)

def racket_a_down():
    y = racket_a.ycor()
    y -= 20
    racket_a.sety(y)

def racket_b_up():
    y = racket_b.ycor()
    y += 20
    racket_b.sety(y)

def racket_b_down():
    y = racket_b.ycor()
    y -= 20
    racket_b.sety(y)


windows.listen()
windows.onkeypress(racket_a_up, "w")
windows.onkeypress(racket_a_down, "s")
windows.onkeypress(racket_b_up, "Up")
windows.onkeypress(racket_b_down, "Down")

while True:
    windows.update()

    """ move ball """
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    """ border """
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        

        
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
    
    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        board.clear()
        board.write("Player1: {}  Player2: {}".format(score_a, score_b),
                    align="center", font=("courier", 24, "bold"))

    
    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        board.clear()
        board.write("Player1: {}  Player2: {}".format(score_a, score_b),
                    align="center", font=("courier", 24, "bold"))

    """ collisions """
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() <
        racket_b.ycor() + 50 and ball.ycor() > racket_b.ycor() -50):
        ball.setx(340)
        ball.dx *= -1

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() <
        racket_a.ycor() + 50 and ball.ycor() > racket_a.ycor() -50):
        ball.setx(-340)
        ball.dx *= -1
    
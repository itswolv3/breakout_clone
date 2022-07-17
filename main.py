from turtle import *
import time
from ball import Ball
from blocks import Block

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("BreakOut")
screen.tracer(0)

# Setup Player Paddle
paddle = Turtle()
paddle.shape("square")
paddle.color("white")
paddle.shapesize(stretch_wid=1, stretch_len=5)
paddle.penup()
paddle.goto(x=0, y=-250)

# Init Ball
ball = Ball()

# Init blocks and positions
positions = [(-350, 250), (-300, 250), (-250, 250), (-200, 250), (-150, 250), (-100, 250), (-50, 250), (0, 250),
            (50, 250), (100, 250), (150, 250), (200, 250), (250, 250), (300, 250), (350, 250), (-350, 210),
            (-300, 210), (-250, 210), (-200, 210), (-150, 210), (-100, 210), (-50, 210), (0, 210), (50, 210),
            (100, 210), (150, 210), (200, 210), (250, 210), (300, 210), (350, 210), (-350, 170), (-300, 170),
            (-250, 170), (-200, 170), (-150, 170), (-100, 170), (-50, 170), (0, 170), (50, 170), (100, 170),
            (150, 170), (200, 170), (250, 170), (300, 170), (350, 170), (-350, 130), (-300, 130), (-250, 130),
            (-200, 130), (-150, 130), (-100, 130), (-50, 130), (0, 130), (50, 130), (100, 130), (150, 130),
            (200, 130), (250, 130), (300, 130), (350,130), (-350, 90), (-300, 90), (-250, 90), (-200, 90),
            (-150, 90), (-100, 90), (-50, 90), (0, 90), (50,90), (100, 90), (150, 90), (200, 90), (250, 90),
            (300, 90), (350, 90)]

blocks = []
for i in positions:
    block = Block()
    blocks.append(block)
    block.goto(i[0], i[1])


# Move Functions
def go_left():
    new_x = paddle.xcor() - 30
    paddle.goto(y=paddle.ycor(), x=new_x)


def go_right():
    new_x = paddle.xcor() + 30
    paddle.goto(y=paddle.ycor(), x=new_x)


screen.listen()
screen.onkeypress(go_left, "Left")
screen.onkeypress(go_right, "Right")

# Run Game
game = True
while game:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()

    if ball.ycor() < -250:
        keep_playing = False

    if ball.xcor() > 350 or ball.xcor() < -350:
        ball.bounce_x()

    if ball.ycor() > 250:
        ball.bounce_y()

    if ball.distance(paddle) < 50 and ball.ycor() > -220:
        ball.bounce_y()

    if ball.ycor() < -300:
        ball.reset_on_screen()

    for i in blocks:
        if ball.distance(i) < 10:
            i.delete()
            ball.bounce_y()

screen.exitonclick()

import time
import turtle

# window configuration
wn = turtle.Screen();
wn.title("Pong")
wn.bgcolor("lightblue")
wn.setup(width=800, height=600)
wn.tracer(0)

player_1 = 0;
player_2 = 0;

# left paddle
left_paddle = turtle.Turtle()
left_paddle.speed(0)
left_paddle.shape("square") # default is 20px by 20px
left_paddle.color("black")
left_paddle.shapesize(stretch_wid=5, stretch_len=1)
left_paddle.penup()
left_paddle.goto(-350, 0)


# right paddle
right_paddle = turtle.Turtle()
right_paddle.speed(0)
right_paddle.shape("square") # default is 20px by 20px
right_paddle.color("black")
right_paddle.shapesize(stretch_wid=5, stretch_len=1)
right_paddle.penup()
right_paddle.goto(350, 0)

# ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square") # default is 20px by 20px
ball.color("black")
ball.penup()
ball.goto(0, 0)

# ball movement pattern

ball_dx = 0.5  # pixels traveled in the x direction
ball_dy = 0.5 # pixels traveled in the y direction

# Create a pen object to register the scores
pen = turtle.Turtle()
pen.speed(0)
pen.color("black")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Player1 0 - 0 Player2", align="center", font=("Courier", 24, "normal"))

# paddle movement
def left_paddle_up():
    y = left_paddle.ycor()
    y += 20
    left_paddle.sety(y)
    if left_paddle.ycor() > 290:
        left_paddle.sety(290)

def left_paddle_down():
    y = left_paddle.ycor()
    y -= 20
    left_paddle.sety(y)
    if left_paddle.ycor() < -290:
        left_paddle.sety(-290)

def right_paddle_up():
    y = right_paddle.ycor()
    y += 20
    right_paddle.sety(y)
    if right_paddle.ycor() > 290:
        right_paddle.sety(290)

def right_paddle_down():
    y = right_paddle.ycor()
    y -= 20
    right_paddle.sety(y)
    if right_paddle.ycor() < -290:
        right_paddle.sety(-290)

# key binding

wn.listen()
wn.onkeypress(left_paddle_up, "w") # when we press W on our window it calls the function left_paddle_up
wn.onkeypress(left_paddle_down, "s") # when we press s on our window it calls the function left_paddle_down
wn.onkeypress(right_paddle_up, "Up") # when we press s on our window it calls the function left_paddle_down
wn.onkeypress(right_paddle_down, "Down") # when we press s on our window it calls the function left_paddle_down




# main game loop
while player_1 < 10 and player_2 < 10:
    wn.update()
    # moving the ball
    ball.setx(ball.xcor() + ball_dx)
    ball.sety(ball.ycor() + ball_dy)

    # check up and down boarders
    if ball.ycor() > 290:
        ball.sety(290)
        ball_dy *= -1 # reverse direction of movement

    if ball.ycor() < -290:
        ball.sety(-290)
        ball_dy *= -1 # reverse direction of movement

    # check left and right boarders

    if ball.xcor() > 390:
        time.sleep(0.5)
        ball.goto(0, 0)
        ball_dx *= -1 # reverse direction of movement
        player_1 += 1
        pen.clear()
        pen.write("Player 1 {} - {} Player 2".format(player_1, player_2), align="center",
                  font=("Courier", 24, "normal"))

    if ball.xcor() < -390:
        time.sleep(0.5)
        ball.goto(0, 0)
        ball_dx *= -1 # reverse direction of movement
        player_2 += 1
        pen.clear()
        pen.write("Player 1 {} - {} Player 2".format(player_1, player_2), align="center",
                  font=("Courier", 24, "normal"))

    # collision
    # the right paddle is at position 350
    # the ball is 20px by 20pxp
    # we count as a colision with the right paddle whenever the ball is x cord is greater than 340
    # and the balls y coordinate is between the (y coordinate of the paddle + 40) and (y coordinate of the paddle - 50)
    if 350 > ball.xcor() > 340 and (right_paddle.ycor() + 40 > ball.ycor() > right_paddle.ycor() - 40):
        ball.setx(340)
        ball_dx *= -1 # collision ball reverses its movement

    if -350 < ball.xcor() < -340 and (left_paddle.ycor() + 40 > ball.ycor() > left_paddle.ycor() - 40):
        ball.setx(-340)
        ball_dx *= -1 # collision ball reverses its movement




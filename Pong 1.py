import turtle
import winsound

wn = turtle.Screen()
wn.title("Pong by Casey WW")
wn.bgcolor("black")
wn.setup(width=800,height=600)
wn.tracer(0)

#score
score_a =0
score_b =0

#Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0) #speed of annimation set at max
paddle_a.shape("square") #20X20 pixels
paddle_a.color("red")
paddle_a.shapesize(stretch_wid=5,stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350,0)


#Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0) #speed of annimation set at max
paddle_b.shape("square") #20X20 pixels
paddle_b.color("green")
paddle_b.shapesize(stretch_wid=5,stretch_len=1)
paddle_b.penup()
paddle_b.goto(350,0)



#Ball
ball = turtle.Turtle()
ball.speed(1) #speed of annimation set at max
ball.shape("square") #20X20 pixels
ball.color("white")
ball.penup()
ball.goto(0,0)
ball.dx = 0.25
ball.dy = 0.25

#pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Player A: 0  Player B: 0", align="center", font=("Courier",24,"normal"))


#Function
def pa_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)

def pa_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)

def pb_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)

def pb_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)

# keyboard binding
wn.listen()
wn.onkeypress(pa_up,"w")
wn.onkeypress(pa_down,"s")


wn.onkeypress(pb_up,"Up")
wn.onkeypress(pb_down,"Down")

#main game loop

while True:
    wn.update()

    #move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    #Border check
    if ball.ycor() > 290:
        ball.sety(290)
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
        ball.dy = -ball.dy

    if ball.ycor() < -290:
        ball.sety(-290)
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
        ball.dy = -ball.dy

    if ball.xcor() > 390:
        ball.goto(0,0)
        ball.dx = -ball.dx
        score_a += 1
        ball.color("white")
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
        ball.dx = 0.25
        ball.dy = 0.25
    if ball.xcor() < -390:
        ball.goto(0,0)
        ball.dx = -ball.dx
        score_b += 1
        ball.color("white")
        pen.clear()
        ball.dx = 0.25
        ball.dy = 0.25
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

    #paddle and ball collisions
    if (ball.xcor() > 340 and ball.xcor() <350) and (ball.ycor() < paddle_b.ycor()+50 and ball.ycor() > paddle_b.ycor() -50):
        ball.setx(340)
        ball.color("green")
        winsound.PlaySound('C:/Users/Casey/Downloads/bounce.wav', winsound.SND_ASYNC)
        ball.dx = -ball.dx-0.05
        ball.dy +=0.05


    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor()+50 and ball.ycor() > paddle_a.ycor() -50):
        ball.setx(-340)
        ball.color("red")
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
        ball.dy += 0.05
        ball.dx = -ball.dx + 0.05
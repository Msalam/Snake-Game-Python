import turtle
import random
import time
#creating turtle screen
screen=turtle.Screen()
screen.title('SNAKE GAME')
screen.setup(width=700,height=700)
screen.tracer(0)
turtle.bgcolor('turquoise')
#creating border
turtle.speed(5)
turtle.pensize(10)
turtle.penup()
turtle.goto(-310,250)
turtle.pendown()
turtle.color('black')
for i in range(2):
    turtle.forward(600)
    turtle.right(90)
    turtle.forward(500)
    turtle.right(90)
#score
score=0
delay=0.1
#snake
snake=turtle.Turtle()
snake.speed(0)
snake.shape('square')
snake.color('black')
snake.penup()
snake.goto(0,0)
snake.direction='stop'
#food
fruit=turtle.Turtle()
fruit.speed(0)
fruit.shape('circle')
fruit.color('red')
fruit.penup()
fruit.goto(30,30)
old_fruit=[]
#scoring
scoring=turtle.Turtle()
scoring.speed(0)
scoring.color('black')
scoring.penup()
scoring.hideturtle()
scoring.goto(0,300)
scoring.write("Score :{}".format(score), align="center", font=("Courier", 24, "bold"))
screen.update()
def s_up():
    if snake.direction !="down":
        snake.direction = "up"
def s_down():
    if snake.direction !="up":
        snake.direction = "down"
def s_left():
    if snake.direction !="right":
        snake.direction = "left"
def s_right():
    if snake.direction !="left":
        snake.direction = "right"
def s_move():
    if snake.direction=="up":
        y=snake.ycor()
        snake.sety(y+20)
    if snake.direction=="down":
        y=snake.ycor()
        snake.sety(y-20)
    if snake.direction=="left":
        x=snake.xcor()
        snake.setx(x-20)
    if snake.direction=="right":
        x=snake.xcor()
        snake.setx(x+20)
screen.listen()
screen.onkeypress(s_up, "Up")
screen.onkeypress(s_down, "Down")
screen.onkeypress(s_left, "Left")
screen.onkeypress(s_right, "Right")
#mian loop
while True:
    screen.update()
    if snake.distance(fruit)<=20:
        x=random.randint(-290,290)
        y=random.randint(-240,240)
        fruit.goto(x,y)
        scoring.clear()
        score+=1
        scoring.write("Score :{}".format(score), align="center", font=("Courier", 24, "bold"))
        delay=0.1
        # creating lenght
        new_fruit=turtle.Turtle()
        new_fruit.speed(0)
        new_fruit.shape('square')
        new_fruit.color('red')
        new_fruit.penup()
        old_fruit.append(new_fruit)
    for i in range(len(old_fruit)-1,0,-1):
        a=old_fruit[i-1].xcor()
        b=old_fruit[i-1].ycor()
        old_fruit[i].goto(a,b)
    if len(old_fruit)>0:
        old_fruit[0].goto(snake.xcor(), snake.ycor())
    s_move()
    if snake.xcor()>280 or snake.xcor()<-300 or snake.ycor()>240 or snake.ycor()<-240:
        time.sleep(1)
        screen.clear()
        screen.bgcolor('turquoise')
        scoring.goto(0,0)
        scoring.write("Game over \nScore :{}".format(score), align="center", font=("Courier", 24, "bold"))
        break

    #snake collision
    game_over = False
    for segment in old_fruit:
        if segment.distance(snake) < 20:
            game_over = True
            break

    if game_over:
        time.sleep(1)
        screen.clear()
        screen.bgcolor('turquoise')
        scoring.goto(0, 0)
        scoring.write("Game over \nScore :{}".format(score), align="center", font=("Courier", 24, "bold"))
        break
    time.sleep(delay)

screen.mainloop()
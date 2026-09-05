import turtle
import time
import random
delay=0.2

win = turtle.Screen()
win.setup(width=500,height=500)
win.bgcolor("blue")
win.tracer(0)

head1 = turtle.Turtle()
head1.shape("square")
head1.color("yellow")
head1.penup()
head1.goto(-100,100)
head1.direction = "stop"
head2 = turtle.Turtle()
head2.shape("square")
head2.color("cyan")
head2.penup()
head2.goto(100,100)
head2.direction = "stop"

body1 = []
body2 = []
score = 0
high_score = 0
player1_score = 0
player2_score = 0
pen = turtle.Turtle()
pen.penup()
pen.hideturtle()
pen.goto(0,200)
pen.clear()
pen.write("score: {}    High Score: {}".format(score,high_score),align="center", font=("Consolas",20,"normal"))    
pen2 = turtle.Turtle()
pen2.penup()
pen2.hideturtle()
pen2.goto(0,170)
pen2.clear()
pen2.write("player1_score: {}   player2_score:".format(player1_score,player2_score),align="center", font=("Consolas",15,"normal"))
def move():
    if head1.direction == "up":
        y = head1.ycor()
        head1.sety(y + 20)
    if head1.direction == "down":
        y = head1.ycor()
        head1.sety(y - 20)
    if head1.direction == "right":
        x = head1.xcor()
        head1.setx(x + 20)
    if head1.direction == "left":
        x = head1.xcor()
        head1.setx(x - 20)
def move_head2():
    if head2.direction == "up":
        y = head2.ycor()   
        head2.sety(y + 20)
    if head2.direction == "down":
        y = head2.ycor()
        head2.sety(y - 20)
    if head2.direction == "right":
        x = head2.xcor()
        head2.setx(x + 20)
    if head2.direction == "left":
        x = head2.xcor()
        head2.setx(x - 20)

def go_up():
    head1.direction = "up"
def go_down():
    head1.direction = "down"
def go_left():
    head1.direction = "left"
def go_right():
    head1.direction = "right"
def go_up2():
    head2.direction = "up"
def go_down2():
    head2.direction = "down"
def go_left2():
    head2.direction = "left"
def go_right2():
    head2.direction = "right"

win.listen()
win.onkey(go_up, "w")
win.onkey(go_down, "s")
win.onkey(go_right, "d")
win.onkey(go_left, "a")
win.onkey(go_up2, "u")
win.onkey(go_down2, "j")
win.onkey(go_right2, "k")
win.onkey(go_left2, "h")

food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0,0)
food_value = random.randint(1,9)
food_pen = turtle.Turtle()
food_pen.hideturtle()
food_pen.penup()
food_pen.color("white")
food_pen.goto(food.xcor(),food.ycor() -10)
food_pen.write(
    food_value,
    align="center",
    font=("Consolas",14,"bold"
          ))
def move_food():
    global food_value
    x = random.randint(-200,200)
    y = random.randint(-200,200)
    food.goto(x,y)
    food_value = random.randint(1,9)
    food_pen.clear()
    food_pen.goto(x, y - 10)
    food_pen.write(
        food_value,
        align="center",
        font=("Consolas",14,"bold")
    )
while True:
    win.update()
    if head1.distance(food)<15:
        player1_score=player1_score+food_value
        move_food
        new_body=turtle.Turtle()
        new_body.speed(0)
        new_body.shape("square")
        new_body.color("yellow")
        new_body.penup()
        body1.append(new_body)
    if head2.distance(food)<15:
            player2_score=player2_score+food_value
            move_food
            new_body=turtle.Turtle()
            new_body.speed(0)
            new_body.shape("square")
            new_body.color("cyan")
            new_body.penup()
            body2.append(new_body)
    if len(body1)>0:
        for index in range (len(body1)-1,0,-1):
            x = body1[index-1].xcor()
            y = body1[index-1].ycor()
            body1[index].goto(x,y)
        x = head1.xcor()
        y = head1.ycor()
        body1[0].goto(x,y)
    if len(body2)>0:
        for index in range (len(body2)-1,0,-1):
            x = body2[index-1].xcor()
            y = body2[index-1].ycor()
            body2[index].goto(x,y)
        x = head2.xcor()
        y = head2.ycor()
        body2[0].goto(x,y)
    if (head1.xcor() > 240 
    or head1.xcor() < -240 
    or head1.ycor() > 240 
    or head1.ycor() < -240):
        time.sleep(1)
        head1.goto(0,0)
        head1.direction = "stop"
        for item in body1:
            item.goto(1000,1000)
        body1 = []
        score = 0
    for item in body1[2:]:
        if item.distance(head1) <15:
            time.sleep(1)
            head1.goto(0,0)
            head1.direction = "stop"
            for item in body1:
                item.goto(1000,1000)
            body1 = []
            score = 0
    def reset_player1():
        global body1,player1_score
        head1.goto(-100,100)
        head1.direction="stop"
        for item in body1:
            item.goto(1000,1000)
        body1=[]
        player1_score=0
    def reset_player2():
            global body2,player2_score
            head2.goto(-100,100)
            head2.direction="stop"
            for item in body2:
                item.goto(1000,1000)
            body2=[]
            player2_score=0
    pen.clear()
    pen.write("score: {}    High Score: {}".format(score,high_score),align="center", font=("Consolas",20,"normal"))    
    
    move()
    move_head2()
    time.sleep(delay)
import turtle, time,random
screen = turtle.Screen()
screen.setup(400,300)
screen.tracer(0,0)
t = turtle.Turtle()
t.shape("turtle")
t.pu()

f = turtle.Turtle()
f.pu()
f.shape("circle")
f.color("red")
f.goto(0,150)
f.seth(-90)
speed = 0
lives = 3
tlife = turtle.Turtle()
tlife.shape("circle")
tlife.color("red")
tlife.pu()
tlife.ht()
tlife.goto(-150,130)
for i in range(3):
    tlife.stamp()
    tlife.fd(25)
scoreturt = turtle.Turtle()
score = 0
scoreturt.ht()
scoreturt.pu()
scoreturt.goto(0,120)
scoreturt.clear()
scoreturt.write("Score: 0", align="center", font=('arial',11,'normal'))  
def go_left():
    t.seth(180)
    global speed
    speed = 3

def go_right():
    t.seth(0)
    global speed
    speed = 3
def stop():
    global speed
    speed = 0  
screen.onkeypress(go_left,"Left")
screen.onkeypress(go_right,"Right")
screen.onkeyrelease(stop,"Left")
screen.onkeyrelease(stop,"Right")
screen.listen()  

while True:
    f.forward(1.8)
    if f.distance(t) < 20:
        f.setx(random.randint(-180,180))
        f.sety(150)
        score += 1
        scoreturt.clear()
        scoreturt.write("Score:" + str(score), align="center", font=('Arial',11,"normal"))
    if t.xcor() < -200:
        speed = 0
        t.setx(-200)

    elif t.xcor() > 200:
        speed = 0
        t.setx(200)
    else:
        t.fd(speed)
    if f.ycor() < -150:
        lives -= 1
        tlife.clearstamps()
        tlife.goto(-180,130)
        for i in range(lives):
            tlife.stamp()
            tlife.fd(25)
        if lives > 0:
            f.goto(random.randint(-180,180),150)
        else:
            f.ht()
    screen.update()
    time.sleep(0.0166)




    




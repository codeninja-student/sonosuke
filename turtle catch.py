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

    if t.xcor() < -200:
        speed = 0
        t.setx(-200)

    elif t.xcor() > 200:
        speed = 0
        t.setx(200)
    else:
        t.fd(speed)
    
    screen.update()
    time.sleep(0.0166)




    




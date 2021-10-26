#a121_catch_a_turtle.py
#-----import statements-----

import turtle as trtl
import random as rand



#-----game configuration----
xmin = 0
xmax = 112
ymin = 0
ymax = 324
color = "magenta"
shape = "turtle"
size = 2
score = 0
fontSetup = ("Arial",20,"normal")
timer = 30
timerUp = False
counterInterval = 1000
colors = ["yellow", "gray", "blue", "red", "purple", "pink"]
differentsizes = [0.5, 1.0, 1.5, 2.0, 2.5]


#-----initialize turtle-----
T = trtl.Turtle()
T.shape(shape)
T.turtlesize(size)
T.fillcolor(color)



scoreWriter = trtl.Turtle()
scoreWriter.penup()
scoreWriter.goto(300,-300)

counter = trtl.Turtle()
counter.penup()
counter.goto(-300,-300)
#-----game functions--------
wn = trtl.Screen()
wn.bgcolor("light green")

def spot_clicked(x, y):
    print("It worked! XD")
    rand.randint(0,400)

def spot_clicked(x, y):
    T.penup()
    T.goto(rand.randint(xmin,xmax), rand.randint(ymin,ymax))
    scoreChange()
    colorChange()
    sizeChange()

def scoreChange():
    global score
    score += 1
    print(score)
    scoreWriter.clear()
    scoreWriter.write(score, font=fontSetup)

def countdown():
    global timer, timerUp
    counter.clear()
    if timer <=0:
        counter.write("Time's Up", font=fontSetup)
        timerUp = True
    else:
        counter.write("Timer " + str(timer), font=fontSetup)
        timer-=1
        counter.getscreen().ontimer(countdown,counterInterval)

def colorChange():
    T.color(rand.choice(colors))
    T.stamp()
    T.color("magenta")

def sizeChange():
    T.shapesize(rand.choice(differentsizes))

def startgame():
    if spot_clicked():









#-----events----------------
T.onclick(spot_clicked)
wn.ontimer(countdown, counterInterval)
wn.mainloop()

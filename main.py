'''
1. Random appearance of the shape on different parts of the screen
2. The event of a shape being clicked
3. The score updating
4. The timer updating. 
'''
#a121_catch_a_turtle.py
#-----import statements-----
import turtle as trtl
import random as rand

#-----game configuration----
xmin = 0
xmax = 112
ymin = 0
ymax = 324
size = 2
score = 0
fontsetup = ("Arial",20,"normal")
timerUp = False
counterInterval = 1000
timer = 30
color = "magenta"
shape = "turtle"

#-----initialize turtle-----
T = trtl.Turtle()
T.shape(shape)
T.fillcolor(color)
T.penup()
T.hideturtle()


StartGame = trtl.Turtle()
StartGame.penup()
StartGame.goto(50,0)
StartGame.write("Click to start game.",font=fontsetup)

scoreWriter = trtl.Turtle()
scoreWriter.penup()
scoreWriter.goto(300,-300)
scoreWriter.hideturtle()

counter = trtl.Turtle()
counter.penup()
counter.goto(-300,-300)
counter.hideturtle()
#-----game functions--------


def spot_clicked(x, y):
  T.goto(rand.randint(xmin,xmax), rand.randint(ymin,ymax))
  scoreChange()
  colorChange()
  sizeChange()

def scoreChange():
    global score
    score += 1
    print(score)
    scoreWriter.clear()
    scoreWriter.write(score, font=fontsetup)

def countdown():
  global timer, timerUp
  counter.clear()
  if timer <=0:
    timer -= 2
    counter.write("Time's Up", font=fontsetup)
    timerUp = True
  else:
    counter.write("Timer " + str(timer), font=fontsetup)
    timer-=1
    counter.getscreen().ontimer(countdown,counterInterval)

def colorChange():
  colors = ["yellow", "gray", "blue", "red", "purple", "pink"]
  T.fillcolor(rand.choice(colors))
  T.stamp()
  T.fillcolor(color)

def sizeChange():
  differentsizes = [0.5, 1.0, 1.5, 2.0, 2.5]
  T.turtlesize(rand.choice(differentsizes))

def Start_Game(x, y):
  T.showturtle()
  countdown()
  StartGame.clear()

#-----events----------------
StartGame.onclick(Start_Game)
T.onclick(spot_clicked)
wn = trtl.Screen()
wn.ontimer(countdown, counterInterval)
wn.bgcolor("light green")
wn.mainloop()
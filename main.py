import turtle
from random import randint

turtleScreen = turtle.Screen()
turtleScreen.setup(800, 600)
turtleScreen.bgcolor("lightblue")
turtleScreen.title("Python Turtle Graphics")

points = turtle.Turtle()
points.hideturtle()
points.color("blue")
points.penup()
points.goto(-50, 250)
score = 0

timer = turtle.Turtle()
timer.hideturtle()
timer.color("black")
timer.penup()
timer.goto(-50, 220)
remainingTime = 30

turtleInstance = turtle.Turtle()
turtleInstance.shape("turtle")
turtleInstance.color("green")
turtleInstance.penup()
turtleInstance.speed(0)
def randomTurtle():
    turtleInstance.clear()
    x = randint(-200, 201)
    y = randint(-150, 151)
    turtleInstance.goto(x, y)
def countdown():
    global remainingTime
    if remainingTime > 0:
        randomTurtle()
        timer.clear()
        timer.write(f"Time: {remainingTime}", font=("Arial", 15, "normal"))
        remainingTime -= 1
        turtleScreen.ontimer(countdown, 1000)
    else:
        timer.clear()
        timer.write(f"Game Over!", font=("Arial", 15, "normal"))
countdown()
def scoreUpdate():
    points.clear()
    points.write(f"Score: {score}", font=("Arial", 15, "normal"))
def scoreIncrease(x, y):
    global score
    score += 1
    scoreUpdate()
turtleInstance.onclick(scoreIncrease)
scoreUpdate()

turtleScreen.mainloop()




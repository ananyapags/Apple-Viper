#Ananya's Rendition of the Classic Snake Arcade game
import turtle
import time
import random

# initializing and setting the screen color
screen = turtle.Screen()
screen.bgcolor("alice blue")
screen.tracer(0)

# draw boundary to keep our snake in! Building a square
boundary = turtle.Turtle()
boundary.color("midnight blue")
boundary.penup()
boundary.goto(-310, 310)
boundary.pendown()
for i in range(4):
    boundary.forward(620)
    boundary.right(90)
boundary.ht()

# draw snake head and intialize location, color, shape
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("green")
head.penup()
head.goto(0, 100)
headDirection = "stop"


# define event listener functions - note that you can't switch to the direct opposite direction in Snake, hence the conditional statements -> we will use the arrow kets on the keyboard to to control the snake's direction
def go_up():
    global headDirection
    if headDirection != "down":
        headDirection = "up"


def go_down():
    global headDirection
    if headDirection != "up":
        headDirection = "down"


def go_right():
    global headDirection
    if headDirection != "left":
        headDirection = "right"


def go_left():
    global headDirection
    if headDirection != "right":
        headDirection = "left"


# bind event listeners, to the fucntions listed above

screen.onkey(go_up, "Up")
screen.onkey(go_down, "Down")
screen.onkey(go_right, "Right")
screen.onkey(go_left, "Left")
screen.listen()

# create the "food" object for the snake, maybe its an apple? Maing it red and a circle
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0, 0)

# set up the score trutle to be positione don the top of the screen and update with each user play
score = 0
high_score = 0

pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("midnight blue")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Score: 0 High Score: {}".format(high_score),
          align="center",
          font=("Courier", 24, "normal"))


# move() updates the position of the head, depending on the direction the head is facing, its imortant to reorient the snake otherwise it will not stay static as it moves in different directions
def move():
    if headDirection == "up":
        y = head.ycor()
        head.sety(y + 20)

    if headDirection == "down":
        y = head.ycor()
        head.sety(y - 20)

    if headDirection == "right":
        x = head.xcor()
        head.setx(x + 20)

    if headDirection == "left":
        x = head.xcor()
        head.setx(x - 20)


# segments is a list that holds each of the snake's body segments, adding to the snakes body at it eats the apple
segments = []

# main game loop
while True:
    screen.update()
    time.sleep(0.1)  # modify this for faster/slower speed

    # check for a collision between the head and the apple
    if head.distance(food) < 15:
        # placing the apple in a random postion everytime the snake eats it
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x, y)

        # add a segment to the snake
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("yellow green")
        new_segment.penup()
        segments.append(new_segment)

        # update the score turtle
        score += 10
        if score > high_score:
            high_score = score

    # update the positioning of all of the body segments- we are moving each body segment to the location of the one before it in the list, and the first segment move to the position of the head
    for index in range(len(segments) - 1, 0, -1):
        x = segments[index - 1].xcor()
        y = segments[index - 1].ycor()
        segments[index].goto(x, y)
    # update the first segment to the position of the head, want to keep the snake head attached to it's body
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)
    # move the head to the next spot
    move()

    # check if head collided with any of the body segments, automatic loose
    headHitBody = False
    for segment in segments:
        if segment.distance(head) < 20:
            headHitBody = True
            break

    # check for a wall collision or a head collision -> edn game if true, and start next iteration
    if head.xcor() > 300 or head.xcor() < -300 or head.ycor(
    ) > 300 or head.ycor() < -300 or headHitBody:
        time.sleep(0.5)
        head.goto(0, 0)
        headDirection = "stop"

        # hide the segments
        for segment in segments:
            segment.goto(1000, 1000)

        # clear segment list in new game
        segments = []

        # reset score, but keep high score to make it seem kike a continual game
        score = 0

    # update the score turtle
    pen.clear()
    pen.write("score: {} High Score: {}".format(score, high_score),
              align="center",
              font=("Courier", 24, "normal"))

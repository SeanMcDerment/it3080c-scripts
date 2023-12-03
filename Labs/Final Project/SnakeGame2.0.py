import turtle
import time
import random

# Game Speed
easy = 0.1
med = 0.08
hard = 0.05
min = 0.01  
# Starting Speed
delay = easy

score = 0    
high_score = 0

# Starting Dif
difficulty = "easy"

# Screen Setup
Window = turtle.Screen()
Window.title("Snake Game by Sean McDerment")
Window.bgcolor("green")
Window.setup(width=600, height=600)
Window.tracer(0)

#Grid Lines for snake tiles
grid_pen = turtle.Turtle()
grid_pen.speed(0)
grid_pen.color("dark green")
grid_pen.penup()

for x in range(-310, 301, 20):
    grid_pen.goto(x, 300)
    grid_pen.pendown()
    grid_pen.goto(x, -300)
    grid_pen.penup()

for y in range(-310, 301, 20):
    grid_pen.goto(300, y)
    grid_pen.pendown()
    grid_pen.goto(-300, y)
    grid_pen.penup()

# Snake Head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("black")
head.penup()
head.goto(0, 0)
head.direction = "stop"

# Snake Food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0, 100)

segments = []

# Scoreboard
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("White")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Score: 0    High Score: 0    Difficulty: Easy", align="center", font=("Courier", 10, "normal"))



# Functions
def go_up():
    if head.direction != "down":
        head.direction = "up"

def go_down():
    if head.direction != "up":
        head.direction = "down"

def go_left():
    if head.direction != "right":
        head.direction = "left"

def go_right():
    if head.direction != "left":
        head.direction = "right"

def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)

    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)

    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)


# Difficulty  
def set_difficulty(diff):
    global difficulty, delay
    difficulty = diff
    if difficulty == "easy":
        delay = easy
    elif difficulty == "medium":
        delay = med
    elif difficulty == "hard":
        delay = hard
    pen.clear()
    pen.write("Score: {}    High Score: {}    Difficulty: {}".format(score, high_score, difficulty.capitalize()),
              align="center", font=("Courier", 10, "normal"))

# Keyboard Bindings
Window.listen()
Window.onkeypress(go_up, "w")
Window.onkeypress(go_down, "s")
Window.onkeypress(go_left, "a")
Window.onkeypress(go_right, "d")
Window.onkeypress(lambda: set_difficulty("easy"), "1")
Window.onkeypress(lambda: set_difficulty("medium"), "2")
Window.onkeypress(lambda: set_difficulty("hard"), "3")

# Main game Loop
while True:
    Window.update()

    # Check for a collision with the border
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "stop"

        # Hide the segments
        for segment in segments:
            segment.goto(1000, 1000)

        # Clear the segments list
        segments.clear()

        # Reset the Score
        score = 0
        #resets the game speed
        delay = easy if difficulty == "easy" else (med if difficulty == "medium" else hard)

        pen.clear()
        pen.write("Score: {}    High Score: {}    Difficulty: {}".format(score, high_score, difficulty.capitalize()),
                  align="center", font=("Courier", 10, "normal"))

    # Check for food collision
    if head.distance(food) < 20:
        # Move food to a random spot
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x, y)

        # Add a segment
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("grey")
        new_segment.penup()
        segments.append(new_segment)

        # Shorten the Delay
        delay -= 0.001

        # Set a minimum delay
        delay = max(delay, min)

        # Increase the score
        score += 10

        if score > high_score:
            high_score = score

        pen.clear()
        pen.write("Score: {}    High Score: {}    Difficulty: {}".format(score, high_score, difficulty.capitalize()),
                  align="center", font=("Courier", 10, "normal"))

    # Move the end segments first in reverse
    for index in range(len(segments) - 1, 0, -1):
        x = segments[index - 1].xcor()
        y = segments[index - 1].ycor()
        segments[index].goto(x, y)

    # Move Segment 0 to where the head is
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)

    move()

    # Check for head Collision with the body
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"

            # Hide the segments
            for segment in segments:
                segment.goto(1000, 1000)

            # Clear the segments list
            segments.clear()

            # Reset the Score
            score = 0

            # Update the Score
            pen.clear()
            pen.write("Score: {}    High Score: {}    Difficulty: {}".format(score, high_score, difficulty.capitalize()),
                      align="center", font=("Courier", 10, "normal"))

    time.sleep(delay)

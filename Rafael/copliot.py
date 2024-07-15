

import turtle
from turtle import Turtle
from freegames import square, vector

# Initialize the players' positions and directions
p1_pos = vector(-100, 0)
p1_dir = vector(4, 0)
p1_trace = set()

p2_pos = vector(100, 0)
p2_dir = vector(-4, 0)
p2_trace = set()

def inside(head):
    # Check if the head position is inside the screen boundary
    return -200 < head.x < 200 and -200 < head.y < 200

def draw():
    # Move players and draw the game
    p1_pos.move(p1_dir)
    p1_head = p1_pos.copy()
    p2_pos.move(p2_dir)
    p2_head = p2_pos.copy()

    if not inside(p1_head) or p1_head in p2_trace:
        print('Player blue wins!')
        return
    if not inside(p2_head) or p2_head in p1_trace:
        print('Player red wins!')
        return

    p1_trace.add(p1_head)
    p2_trace.add(p2_head)

    square(p1_pos.x, p1_pos.y, 3, 'red')
    square(p2_pos.x, p2_pos.y, 3, 'blue')
    turtle.update()
    turtle.ontimer(draw, 50)

# Set up the game window
turtle.setup(420, 420, 370, 0)
turtle.hideturtle()
turtle.tracer(False)
turtle.listen()

# Define controls for player 1
turtle.onkey(lambda: p1_dir.rotate(90), 'a')
turtle.onkey(lambda: p1_dir.rotate(-90), 'd')

# Define controls for player 2
turtle.onkey(lambda: p2_dir.rotate(90), 'j')
turtle.onkey(lambda: p2_dir.rotate(-90), 'l')

draw()
turtle.done()
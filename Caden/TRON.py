from turtle import *
from freegames import square, vector

redxy = vector(-100, 0)
redaim = vector(4, 0)
redbody = set()

bluexy = vector(100, 0)
blueaim = vector(-4, 0)
bluebody = set()

def inside(head):
    return -200 < head.x < 200 and -200 < head.y < 200

def draw():
    redxy.move(redaim)
    redhead = redxy.copy()

    bluexy.move(blueaim)
    bluehead = bluexy.copy()

def start_game():
    clear()
    onkey(lamba: redaim.rotate(90), 'a')
    onkey(lamba: redaim.rotate(-90), 'd')
    onkey(lamba: blueaim.rotate(90), 'j')
    onkey(lamba: blueaim.rotate(-90), 'l')
    draw()

setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()

onkey(start_game, 'space')
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

    if not inside(redhead) or redhead in bluebody or redhead in redbody:
        print("Blue wins! Red get good")
        penup()
        goto(0,0)
        color('black')
        write("press the [enter] key.", align="center", font=("Arial", 16, "bold"))
        return

    if not inside(redhead) or redhead in bluebody or redhead in redbody:
        print("Blue wins! Red get good")
        penup()
        goto(0,0)
        color('black')
        write("press the [enter] key.", align="center", font=("Arial", 16, "bold")) 
        return

    redbody.add(redhead)
    bluebody.add(bluehead)

    # draw players at their new positions
    square(redxy.x, redxy.y, 3, 'red')
    square(bluexy.x, bluexy.y, 3, 'blue')
    update()
    ontimer(draw, 50)

def start_game():
    clear()
    onkey(lambda: redaim.rotate(90), 'a')
    onkey(lambda: redaim.rotate(-90), 'd')
    onkey(lambda: blueaim.rotate(90), 'j')
    onkey(lambda: blueaim.rotate(-90), 'l')
    draw()

setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()

onkey(start_game, 'space')

penup()
goto(0,0)
color('black')
write("press the [enter] key.", align="center", font=("Arial", 16, "bold"))
done()
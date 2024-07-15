from turtle import *
from freegames import square, vector

redxy = (-100, 0)
redaim = vector(4, 0)
redbody = set()

bluexy = vector(100, 0)
blueaim = vector(-4, 0)
bluebody = set()

def inside(head):
    -200 < head.x < 200 and -200 < head.y < 200

def draw():
    redxy.move(redaim)
    redhead = redxy.copy()

    bluexy.move(blueaim)
    bluehead = bluexy.copy()

    if not inside(redhead) or redhead in bluebody or redhead in redbody:
        print("womp womp")
        penup()
        goto(0, 0)
        color('blue')
        write("wom womp", align="center", font=("arail", 16, "bold"))
        return
    
    if not inside(bluehead) or bluehead in redbody or bluehead in bluebody:
        print("womp womp")
        penup()
        goto(0, 0)
        color('red')
        write("wom womp", align="center", font=("arail", 16, "bold"))
        return

    redbody.add(redhead)
    bluebody.add(bluehead)



# draw players at their ner positions
square(redxy.x, redxy)
square


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
goto(0, 0)
color('black')
write("press the [enter] key. ", align="center", font=("arail", 16, "bold"))
done()
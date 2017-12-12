# ---------Shooting game about a treasure lost in space----------
# https://www.youtube.com/user/shiffman


def setup():
    size(800, 800)


def draw():

    # ---background---
    background(255)
    beginning = color(1, 5, 32)  # e.g.(5, 5, 99)
    ending = color(45, 135, 255)  # e.g.(5, 201, 187)

    for i in range(801):
        stroke(lerpColor(beginning, ending, i/600.0))
        line(0, i, width, i)
    # stars-points
    stroke(227, 231, 38)
    point(400, 400)

    stroke(227, 231, 38)
    point(300, 700)

    stroke(227, 231, 38)
    point(567, 96)

    # stars-shooting
    stroke(146, 249, 238)
    line(230, 40, 280, 70)

    stroke(146, 249, 238)
    line(230, 40, 280, 70)

    stroke(146, 249, 238)
    line(490, 400, 523, 480)

    # Title "Pew Pew! Space Bunny Edition!
    textSize(25)
    textAlign(LEFT)
    fill(255)
    text("Pew pew!", 20, 30)

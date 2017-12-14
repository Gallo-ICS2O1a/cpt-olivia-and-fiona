# shooting game about a treasure lost in space
# https://www.youtube.com/user/shiffman
# link used for treasure chest is too long (Pep 8)
# however it is required so please ignore it. Thank you!!

# variables
score = 0
ballSize = 40
playerPos = PVector(180, 0)
missile = PVector(230, 200)
missileSpeed = PVector(7, 0)
playerHP = 10
chestHP = 3
url = "http://clipartix.com/wp-content/uploads/2016/07/Treasure-chest-clipart-clipart.gif"
webImg = loadImage(url, "gif")


def setup():
    size(1000, 600)


def draw():
    # globals
    global score
    global ballSize
    global playerPos
    global missile
    global missileSpeed
    global playerHP
    global chestHP
    global url
    global webImg

    # background
    background(255)
    beginning = color(1, 5, 32)
    ending = color(45, 135, 255)

    for i in range(801):
        stroke(lerpColor(beginning, ending, i/600.0))
        line(0, i, width, i)

    # title & score
    textSize(25)
    fill(255)
    text("Pew Pew!!!", 465, 50)
    text("score:", 845, 50)
    text(score, 930, 50)

    # health points
    text("Player's HP:     / 10", 760, 90)
    text("Chest's HP:    / 3", 760, 130)
    text(playerHP, 903, 90)
    text(chestHP, 903, 130)

    # stars
    strokeWeight(2)
    stroke(255)
    point(500, 400)
    point(300, 200)
    point(100, 300)
    point(600, 100)
    point(700, 250)
    point(430, 230)
    point(150, 60)
    point(360, 470)
    point(50, 140)
    point(230, 350)
    point(750, 430)
    point(150, 450)
    point(365, 320)
    point(600, 300)
    point(650, 550)

    # treasure chest
    image(webImg, 20, 300)
    webImg.resize(100, 50)

    # player
    playerPos.y = mouseY
    stroke(255, 112, 91)
    strokeWeight(5)
    noFill()
    ellipse(playerPos.x, playerPos.y, ballSize, ballSize)

    # missiles
    stroke(255, 81, 54)
    ellipse(missile.x, missile.y, ballSize, ballSize)
    missile.add(missileSpeed)
    if missile.x > width:
        missile.x = 230
        missile.y = mouseY

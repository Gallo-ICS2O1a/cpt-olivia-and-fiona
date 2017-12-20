# shooting game about a treasure lost in space
# link used for treasure chest is too long (according to Pep 8)
# however it is required so please ignore it. Thank you!!

# variables
score = 0
playerSize = 40
playerPos = PVector(180, 0)

missilePos = PVector(200, 100)
missileSpeed = PVector(10, 0)

mobPos = PVector(950, 200)
mobSize = 50
mobSpeed = PVector(-5, 0)

playerHP = 10
chestHP = 3

url = "http://clipartix.com/wp-content/uploads/2016/07/Treasure-chest-clipart-clipart.gif"
webImg = loadImage(url, "gif")
url2 = "https://i.imgur.com/tcSd9mZ.png"
webImg2 = loadImage(url2, "png")


def setup():
    size(1000, 600)


def draw():
    # globals
    global score
    global playerSize
    global playerPos
    global missilePos
    global missileSpeed
    global mobPos
    global mobSize
    global mobSpeed
    global playerHP
    global chestHP
    global url
    global webImg
    global url2
    global webImg2

    # background
    background(255)
    beginning = color(1, 5, 32)
    ending = color(45, 135, 255)

    for i in range(801):
        stroke(lerpColor(beginning, ending, i/600.0))
        line(0, i, width, i)

    # title, score & tip
    textSize(25)
    fill(255)
    text("Pew Pew!!!", 465, 50)
    text("score:", 845, 50)
    text(score, 930, 50)
    textSize(20)
    text("tip! press down your mouse to activate [game help]", 200, 75)

    # health points
    text("Player's HP:     / 10", 760, 90)
    text("Chest's HP:    / 3", 760, 130)
    text(playerHP, 874, 90)
    text(chestHP, 877, 130)

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

    # treasure chests
    for y in range(20, 700, 100):
        image(webImg, 20, y)
        webImg.resize(100, 50)

    # player
    playerPos.y = mouseY
    stroke(255, 112, 91)
    strokeWeight(5)
    noFill()
    ellipse(playerPos.x, playerPos.y, playerSize, playerSize)

    # missiles
    stroke(255, 81, 54)
    rect(missilePos.x, missilePos.y, 50, 20)
    missilePos.add(missileSpeed)
    if missilePos.x > width:
        missilePos.x = 200
        missilePos.y = mouseY - 10

    # mobs
    stroke(146, 255, 48)
    ellipse(mobPos.x, mobPos.y, mobSize, mobSize)
    mobPos.add(mobSpeed)
    if mobPos.x == 0:
        mobPos.x = 950
        mobPos.y = random(100, 500)

    # missle detection for mobs if hit
    distance = PVector.sub(missilePos, mobPos)
    if distance.mag() <= mobSize:
        mobPos.x = 950
        mobPos.y = random(100, 500)
        missilePos.x = 200
        score += 1
    if score >= 10:
        textSize(30)
        text("DANGER, DANGER! MINI BOSS IS APPEARING!", 200, 300)
        score = 10
        chestHP = 3
        playerHP = 10

    # mob detection for player if hit
    distanceMobPlayer = PVector.sub(mobPos, playerPos)
    if distanceMobPlayer.mag() <= playerSize:
        mobPos.x = 950
        mobPos.y = random(100, 500)
        playerHP -= 1

    if playerHP <= 0:
        score = 0
        playerHP = 0
        chestHP = 3
        textSize(40)
        text("GAME OVER~ :C", 350, 300)

    # mob detection for treasure chest if hit
    if mobPos.x == 100:
        chestHP -= 1
    if chestHP <= 0:
        textSize(40)
        text("GAME OVER~ :C", 350, 300)
        chestHP = 0
        playerHP = 10
        score = 0

    # game help
    if mousePressed is True:
        webImg2.resize(320, 482)
        image(webImg2, 0, 120)
        mobSpeed = PVector(0, 0)
        missileSpeed = PVector(0, 0)
        textSize(20)
        fill(255)
        text("""Game Help:
1. You are the pink ellipse, your missiles are the red rectangles and
the enemy is the green ellipse
2. You shoot automatic missiles, move your mouse up or down to
direct the missiles
3. Defeat the enemy mobs and protect the treasure chests
4. There are 3 stages in total:
stage 1 and 2 - defeat the mob waves and a mini boss to continue
stage 3 - defeat the mob waves and the final boss to continue
5. If you or the treasure chest gets hit, HP will go down. If HP hits 0,
its game over!
6. After clearing 3 stages, you reached the spaceship and cleared the
game~""", 300, 200)
    else:
        mobSpeed = PVector(-5, 0)
        missileSpeed = PVector(10, 0)

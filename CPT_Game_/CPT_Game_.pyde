# shooting game about treasure lost in space
# [mission start]

# variables
score = 0

playerSize = 40
playerPos = PVector(180, 0)
missilePos = PVector(200, 100)
missileSpeed = PVector(10, 0)

mobPos = PVector(950, 200)
mobSize = 50
mobSpeed = PVector(-5, 0)

miniBossPosA = PVector(800, 350)
miniBossSpeedA = PVector(0, 0)
miniBossSizeA = 100
planetPos = PVector(200, 400)
planetSpeed = PVector(10, 0)
planetSize = 80

miniBossPosB = PVector(800, 350)
miniBossSpeedB = PVector(3, 3)
miniBossSizeB = 120
asteroidPos = PVector(700, 100)
asteroidSpeed = PVector(-10, 0)

playerHP = 10
chestHP = 3
miniBossHP1 = 10
miniBossHP2 = 15

urlChest = "https://i.imgur.com/lHwIfhP.gif"
imgChest = loadImage(urlChest, "gif")
# urlGirl = "https://i.imgur.com/SxPXFBX.png"
# imgGirl = loadImage(urlGirl, "png")
urlAsteroid = "https://i.imgur.com/lgju8SY.png"
imgAsteroid = loadImage(urlAsteroid, "png")


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
    global miniBossPosA
    global miniBossSpeedA
    global miniBossSizeA
    global planetPos
    global planetSpeed
    global planetSize
    global miniBossPosB
    global miniBossSizeB
    global miniBossSpeedB
    global asteroidPos
    global asteroidSpeed
    global playerHP
    global chestHP
    global miniBossHP1
    global miniBossHP2
    global urlChest
    global imgChest
    global urlGirl
    global imgGirl
    global urlAsteroid
    global imgAsteroid

    # background
    background(255)
    beginning = color(1, 5, 32)
    ending = color(45, 135, 255)

    for i in range(801):
        stroke(lerpColor(beginning, ending, i / 600.0))
        line(0, i, width, i)

    # title, score & tip
    textSize(25)
    fill(255)
    text("Pew Pew!!!", 465, 50)
    text("score:", 845, 50)
    text(score, 930, 50)
    textSize(20)
    text("tip! hold down your mouse to activate [game help]", 200, 75)

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
        imgChest.resize(100, 50)
        image(imgChest, 20, y)

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
    if distance.mag() <= mobSize/2:
        mobPos.x = 950
        mobPos.y = random(100, 500)
        missilePos.x = 200
        score += 1

    # Stage One
    if score >= 1:
        textSize(20)
        text("""DANGER, DANGER! MINI BOSS NO. 1 HAS APPEARED!
        The mini boss will follow you so be careful!
        If the mini boss touches you, you lose HP
        Crash the mini boss into the planet to defeat it
        (Chests are invincible!)""", 200, 100)

        # player adjustments
        playerPos = PVector(mouseX, mouseY)

        # disable player's missiles and mobs
        missilePos = PVector(1100, 800)
        missileSpeed = PVector(0, 0)
        mobPos = PVector(1100, 400)
        mobSpeed = PVector(0, 0)

        # mini boss no. 1
        text("Mini Boss's HP:     / 10", 620, 550)
        text(miniBossHP1, 770, 550)
        stroke(222, 0, 62)
        ellipse(miniBossPosA.x, miniBossPosA.y, miniBossSizeA, miniBossSizeA)

        # mini boss follows player
        distanceFollow = PVector.sub(miniBossPosA, playerPos)
        distanceFollow.mult(-1)
        miniBossSpeedA = distanceFollow.normalize()
        miniBossPosA.add(miniBossSpeedA * 3)

        # planet
        fill(128, 128, 128)
        noStroke()
        ellipse(planetPos.x, planetPos.y, planetSize, planetSize)

        # collision detection for planet and mini boss
        distancePlanetMB = PVector.sub(planetPos, miniBossPosA)
        if distancePlanetMB.mag() <= miniBossSizeA/2:
            miniBossHP1 -= 1
            planetPos.x = random(0, 1000)
            planetPos.y = random(0, 600)

        # mini boss detection if player attacks successfully
        distancePlayerMB1 = PVector.sub(playerPos, miniBossPosA)
        if distancePlayerMB1.mag() <= playerSize/2:
            playerHP -= 1

        # mini boss is defeat
        if miniBossHP1 <= 0:
            miniBossHP1 = 0
            textSize(30)
            fill(255)
            text("MINI BOSS no. 1 IS CLEARED!", 450, 300)

        elif playerHP <= 0:
            textSize(30)
            text("GAME OVER...", 600, 300)

    # Stage Two
    if score >= 25:
        textSize(30)
        text("DANGER, DANGER! MINI BOSS NO. 2 HAS APPEARED!", 200, 170)

        # mini boss no. 2
        stroke(222, 0, 62)
        ellipse(miniBossPosB.x, miniBossPosB.y, miniBossSizeB, miniBossSizeB)
        text("Mini Boss's HP:     / 15", 620, 550)
        text(miniBossHP2, 845, 550)
        textSize(20)
        text("dodge asteroids & bump into mini boss to deplete hp", 150, 210)
        text("(chests are invincible)", 675, 210)

        # player adjustments
        playerPos.x = mouseX

        # asteroids
        imgAsteroid.resize(60, 60)
        image(imgAsteroid, asteroidPos.x, asteroidPos.y)
        asteroidPos.add(asteroidSpeed)
        if asteroidPos.x < 0:
            asteroidPos.x = 1000
            asteroidPos.y = random(30, 570)

        # disable player's missiles and mobs
        missilePos.x = PVector(1100, 800)
        missileSpeed = PVector(0, 0)
        mobPos = PVector(1100, 400)
        mobSpeed = PVector(0, 0)

        # asteroid detection for player if hit
        distancePlayerAsteroid = PVector.sub(asteroidPos, playerPos)
        if distancePlayerAsteroid.mag() <= playerSize:
            asteroidPos.x = 1000
            asteroidPos.y = random(30, 570)
            playerHP -= 1

        if playerHP <= 0:
            score = 0
            playerHP = 0
            chestHP = 0
            textSize(40)
            text("GAME OVER~ :C", 350, 300)

        # mini boss detection if player attacks successfully
        distancePlayerMB2 = PVector.sub(miniBossPosB, playerPos)
        if distancePlayerMB2.mag() <= miniBossSizeB/2:
            miniBossHP2 -= 1
            miniBossPosB.x = random(0, 1000)
            miniBossPosB.y = random(0, 600)

        elif miniBossHP2 <= 0:
            miniBossHP2 = 0

        # range detection and repel
        radius = miniBossSizeB/2
        distanceRepel = PVector.sub(miniBossPosB, playerPos)
        if distanceRepel.mag() <= radius * 2:
            direction = distanceRepel.heading()
            repel = miniBossPosB.fromAngle(direction)
            miniBossSpeedB.add(repel)

        # mini boss bouncing off walls
        miniBossPosB.add(miniBossSpeedB)
        if miniBossPosB.x > width:
            miniBossPosB.x = width
            miniBossSpeedB.x = -miniBossSpeedB.x
        elif miniBossPosB.x < 170:
            miniBossPosB.x = 170
            miniBossSpeedB.x = -miniBossSpeedB.x

        if miniBossPosB.y > height:
            miniBossPosB.y = height
            miniBossSpeedB.y = -miniBossSpeedB.y
        elif miniBossPosB.y < 0:
            miniBossPosB.y = 0
            miniBossSpeedB.y = -miniBossSpeedB.y

    # mob detection for player if hit
    distanceMobPlayer = PVector.sub(mobPos, playerPos)
    if distanceMobPlayer.mag() <= playerSize/2:
        mobPos.x = 950
        mobPos.y = random(100, 500)
        playerHP -= 1

    if playerHP <= 0:
        score = 0
        playerHP = 0
        chestHP = 0
        textSize(40)
        text("GAME OVER~ :C", 350, 300)

    # mob detection for treasure chest if hit
    if mobPos.x == 100:
        chestHP -= 1
    if chestHP <= 0:
        textSize(40)
        text("GAME OVER~ :C", 350, 300)
        chestHP = 0
        playerHP = 0
        score = 0

    # game help
    if mousePressed is True:
        beginning = color(1, 5, 32)
        ending = color(45, 135, 255)
        for i in range(801):
            stroke(lerpColor(beginning, ending, i / 600.0))
            line(0, i, width, i)
        imgGirl.resize(320, 482)
        image(imgGirl, 0, 120)
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
stage 1 and 2 - defeat the mob waves and the mini bosses to continue
With each mini boss, there will be a special mission for the player
stage 3 - defeat the mob waves and the final boss to continue
5. If you or the treasure chest gets hit, HP will go down. If HP hits 0,
its game over!
6. After clearing 3 stages, you reached the spaceship and cleared the
game~""", 300, 180)
    else:
        mobSpeed = PVector(-5, 0)
        missileSpeed = PVector(10, 0)


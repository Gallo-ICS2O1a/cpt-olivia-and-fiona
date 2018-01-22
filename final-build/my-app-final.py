# shooting game about treasure lost in space
# [mission start]
# game help, spaceship & ending images digitally drawn by Fiona
# please enjoy our game!!

# variables
playerSize = 40
playerPos = PVector(180, 0)
missilePos = PVector(200, 100)
missileSpeed = PVector(10, 0)

mobPos = PVector(950, 200)
mobSize = 50
mobSpeed = PVector(-5, 0)
miniBossPos = PVector(1000, 600)
miniBossSpeed = PVector(0, 0)
miniBossSize = 100

planetPos = PVector(200, 400)
planetSize = 80
planetSpeed = PVector(10, 0)

bossPos = PVector(800, 350)
bossSpeed = PVector(3, 3)
bossSize = 120
asteroidPos = PVector(700, 100)
asteroidSpeed = PVector(-10, 0)

score = 0
playerHP = 10
chestHP = 3
miniBossHP = 10
bossHP = 20

screen = "start menu"

urlChest = "https://i.imgur.com/lHwIfhP.gif"
imgChest = loadImage(urlChest, "gif")
urlGirl = "https://i.imgur.com/SxPXFBX.png"
imgGirl = loadImage(urlGirl, "png")
urlGirlBlue = "https://i.imgur.com/kEvWRTm.png"
imgGirlBlue = loadImage(urlGirlBlue, "png")
urlAsteroid = "https://i.imgur.com/lgju8SY.png"
imgAsteroid = loadImage(urlAsteroid, "png")
urlPlanet = "https://i.imgur.com/PwoqdLl.png"
imgPlanet = loadImage(urlPlanet, "png")
urlRocket = "https://i.imgur.com/IKJ9fyN.png"
imgRocket = loadImage(urlRocket, "png")


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
    global miniBossPos
    global miniBossSpeed
    global miniBossSize
    global planetPos
    global planetSpeed
    global planetSize
    global bossPos
    global bossSize
    global bossSpeed
    global asteroidPos
    global asteroidSpeed
    global playerHP
    global chestHP
    global miniBossHP
    global bossHP
    global imgChest
    global imgGirl
    global imgGirlBlue
    global imgAsteroid
    global imgPlanet
    global imgRocket
    global screen

    # start menu
    if screen == "start menu":
        if keyPressed:
            if key == "s":
                screen = "stage zero"
        background(255)
        beginning = color(1, 5, 32)
        ending = color(45, 135, 255)
        for i in range(801):
            stroke(lerpColor(beginning, ending, i / 600.0))
            line(0, i, width, i)
        fill(255)
        textSize(30)
        text("""
            Pew Pew!!
            Press [s] to start the game~!""", 100, 200)

    # Stage 0 (Normal Stage)
    elif screen == "stage zero":
        background(255)
        beginning = color(1, 5, 32)
        ending = color(45, 135, 255)
        for i in range(801):
            stroke(lerpColor(beginning, ending, i / 600.0))
            line(0, i, width, i)

        # title, score & tip
        textSize(25)
        fill(255)
        text("Pew Pew!!", 465, 50)
        text("score:", 845, 50)
        text(score, 930, 50)
        textSize(20)
        text("tip! hold down your mouse to activate [game help]", 200, 90)

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

        # mob detection for player if hit
        distanceMobPlayer = PVector.sub(mobPos, playerPos)
        if distanceMobPlayer.mag() <= playerSize/2:
            mobPos.x = 950
            mobPos.y = random(100, 500)
            playerHP -= 1
        if playerHP <= 0:
            background(196, 7, 0)
            textSize(30)
            text("GAME OVER...", 350, 300)

        # mob detection for treasure chest if hit
        if mobPos.x == 100:
            chestHP -= 1
        if chestHP <= 0:
            background(196, 7, 0)
            textSize(30)
            text("GAME OVER...", 350, 300)

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
            textSize(18)
            fill(255)
            text("""Game Help:
    1. You are the pink ellipse, your missiles are the red rectangles and
    the enemy is the green ellipse
    2. You shoot automatic missiles, move your mouse up or down to
    direct the missiles
    3. Defeat the enemy mobs and protect the treasure chests
    4. The mini boss will arrive once you hit a score of 10
    The boss will arive once you hit a score of 25
    5. If you or the treasure chest gets hit, HP will go down. If HP hits 0,
    its game over!
    6. After clearing 3 stages, you reached the spaceship and cleared the
    game~""", 340, 180)
        else:
            mobSpeed = PVector(-5, 0)
            missileSpeed = PVector(10, 0)

        # scores
        if score == 10:
            screen = "stage one"
        elif score == 25:
            screen = "stage two"

    # Stage One
    elif screen == "stage one":
        # background
        background(255)
        beginning = color(1, 5, 32)
        ending = color(45, 135, 255)
        for i in range(801):
            stroke(lerpColor(beginning, ending, i / 600.0))
            line(0, i, width, i)

        # game help
        if keyPressed:
            if key == "1":
                textSize(20)
                fill(255)
                text("""
            The mini boss will follow you so be careful!
            If the mini boss touches you, your HP will deplete
            Crash the mini boss into the planet to defeat it
            (Chests are invincible!)
            """, 200, 160)
            miniBossPos = PVector(1000, 600)

        # title, score & tip
        textSize(25)
        fill(255)
        text("Pew Pew!!", 465, 50)
        text("score:", 845, 50)
        text(score, 930, 50)
        textSize(20)
        text("tip! hold down [1] to activate [game help]", 200, 90)

        # health points
        text("Player's HP:     / 10", 760, 90)
        text("Chest's HP:    / 3", 760, 130)
        text(playerHP, 874, 90)
        text(chestHP, 877, 130)

        # treasure chests
        for y in range(20, 700, 100):
            imgChest.resize(100, 50)
            image(imgChest, 20, y)

        # player adjustments
        playerPos = PVector(mouseX, mouseY)
        stroke(255, 112, 91)
        strokeWeight(5)
        noFill()
        ellipse(playerPos.x, playerPos.y, playerSize, playerSize)

        # disable player's missiles and mobs
        missilePos = PVector(1100, 800)
        missileSpeed = PVector(0, 0)
        mobPos = PVector(1100, 400)
        mobSpeed = PVector(0, 0)

        # mini boss
        textSize(30)
        text("Mini Boss's HP:     / 10", 600, 560)
        text(miniBossHP, 825, 560)
        stroke(222, 0, 62)
        ellipse(miniBossPos.x, miniBossPos.y, miniBossSize, miniBossSize)

        # mini boss follows player
        distanceFollow = PVector.sub(miniBossPos, playerPos)
        distanceFollow.mult(-1)
        miniBossSpeed = distanceFollow.normalize()
        miniBossPos.add(miniBossSpeed * 3)

        # planet
        fill(182, 223, 255)
        stroke(73, 141, 158)
        strokeWeight(3)
        ellipse(planetPos.x, planetPos.y, planetSize, planetSize)

        # collision detection for planet and mini boss
        distancePlanetMB = PVector.sub(planetPos, miniBossPos)
        if distancePlanetMB.mag() <= miniBossSize/2:
            miniBossHP -= 1
            planetPos.x = random(0, 1000)
            planetPos.y = random(0, 600)

        # mini boss detection if player attacks successfully
        distancePlayerMB = PVector.sub(playerPos, miniBossPos)
        if distancePlayerMB.mag() <= playerSize/2:
            playerHP -= 1

        if miniBossHP <= 0:
            miniBossHP = 0
            screen = "stage zero"
            score += 1
            playerPos.x = 180
        elif playerHP <= 0:
            background(196, 7, 0)
            textSize(30)
            text("GAME OVER...", 350, 300)

    # Stage Two
    elif screen == "stage two":
        # background
        background(255)
        beginning = color(1, 5, 32)
        ending = color(45, 135, 255)
        for i in range(801):
            stroke(lerpColor(beginning, ending, i / 600.0))
            line(0, i, width, i)

        # game help
        if keyPressed:
            if key == "2":
                textSize(20)
                fill(255)
                text("""
            Your mission is to attack the boss by colliding into it.
            But be wary of the asteroids that fly out of nowhere.
            Dodge the asteroids and defeat the boss!
            (Chests are invincible!)
            """, 200, 160)
            bossPos = PVector(1000, 600)
            asteroidPos = PVector(0, 600)

        # title, score & tip
        textSize(25)
        fill(255)
        text("Pew Pew!!", 465, 50)
        text("score:", 845, 50)
        text(score, 930, 50)
        textSize(20)
        text("tip! hold down [2] to activate [game help]", 200, 90)
        # health points
        text("Player's HP:     / 10", 760, 90)
        text("Chest's HP:    / 3", 760, 130)
        text(playerHP, 874, 90)
        text(chestHP, 877, 130)

        # treasure chests
        for y in range(20, 700, 100):
            imgChest.resize(100, 50)
            image(imgChest, 20, y)

        # player adjustments
        playerPos = PVector(mouseX, mouseY)
        stroke(255, 112, 91)
        strokeWeight(5)
        noFill()
        ellipse(playerPos.x, playerPos.y, playerSize, playerSize)

        # disable player's missiles and mobs
        missilePos = PVector(1100, 800)
        missileSpeed = PVector(0, 0)
        mobPos = PVector(1100, 400)
        mobSpeed = PVector(0, 0)

        # boss
        textSize(30)
        text("Boss's HP:     / 20", 600, 560)
        text(bossHP, 750, 560)
        stroke(222, 0, 62)
        ellipse(bossPos.x, bossPos.y, bossSize, bossSize)

        # asteroids
        imgAsteroid.resize(60, 60)
        image(imgAsteroid, asteroidPos.x, asteroidPos.y)
        asteroidPos.add(asteroidSpeed)
        if asteroidPos.x < 0:
            asteroidPos.x = 1000
            asteroidPos.y = random(30, 570)

        # asteroid detection for player if hit
        distancePlayerAsteroid = PVector.sub(asteroidPos, playerPos)
        if distancePlayerAsteroid.mag() <= playerSize:
            asteroidPos.x = 1000
            asteroidPos.y = random(30, 570)
            playerHP -= 1
        if playerHP <= 0:
            background(196, 7, 0)
            textSize(30)
            text("GAME OVER...", 350, 300)

        # range detection and repel
        radius = bossSize/2
        distanceRepel = PVector.sub(bossPos, playerPos)
        if distanceRepel.mag() <= radius * 2:
            direction = distanceRepel.heading()
            repel = bossPos.fromAngle(direction)
            bossSpeed.add(repel)

        # boss bouncing off walls
        bossPos.add(bossSpeed)
        if bossPos.x > width:
            bossPos.x = width
            bossSpeed.x = -bossSpeed.x
        elif bossPos.x < 170:
            bossPos.x = 170
            bossSpeed.x = -bossSpeed.x
        if bossPos.y > height:
            bossPos.y = height
            bossSpeed.y = -bossSpeed.y
        elif bossPos.y < 0:
            bossPos.y = 0
            bossSpeed.y = -bossSpeed.y

        # boss detection if player attacks successfully
        distancePlayerBoss = PVector.sub(bossPos, playerPos)
        if distancePlayerBoss.mag() <= bossSize/2:
            bossHP -= 1
            bossPos.x = random(0, 1000)
            bossPos.y = random(0, 600)
        elif bossHP <= 0:
            bossHP = 0
            screen = "end"

    # The End
    elif screen == "end":
        # background
        background(255)
        beginning = color(1, 5, 32)
        ending = color(45, 135, 255)
        for i in range(801):
            stroke(lerpColor(beginning, ending, i / 600.0))
            line(0, i, width, i)

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

        # images
        imgGirlBlue.resize(500, 700)
        image(imgGirlBlue, 640, -315)
        imgRocket.resize(230, 330)
        image(imgRocket, 17, 285)
        imgPlanet.resize(320, 440)
        image(imgPlanet, 690, 290)
        imgChest.resize(210, 110)
        image(imgChest, 45, 120)

        # text
        fill(183, 245, 217)
        noStroke()
        rect(370, 40, 400, 150)
        triangle(770, 95, 770, 135, 800, 115)

        textSize(25)
        fill(0)
        text("Thank you for playing", 390, 95)
        textSize(30)
        fill(4, 23, 76)
        text("Pew Pew!! (> W <)", 390, 140)
        textSize(25)
        fill(0)
        text("""Congrats! You have reached your spaceship
and cleared the game~
We hope you had fun playing!
* ^*)9""", 310, 350)

import pygame, time, random

pygame.init()

W, H = 800, 600
win = pygame.display.set_mode((W, H))
pygame.display.set_caption('Platformer')
pygame.event.clear()

gravity = 1
score = 0
score_list = []
Platforms = []
clock = pygame.time.Clock()
fps = 60

ground = {
    "x": 0,
    "y": 560,
    "width": W,
    "height": 40,
    "color": (0, 0, 0)
}

player = {
    "x": 380,
    "y": 520,
    "width": 40,
    "height": 40,
    "color": (255, 0, 0),
    "Xspeed": 10,
    "Yspeed": 20,
    "touchingPlatform": False
}

player_rect = pygame.Rect(player["x"], player["y"], player["width"], player["height"])


class Platform:
    def __init__(
            self, x, y, width, height, scrollSpeed, r, b, g):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.scrollSpeed = scrollSpeed
        self.red = r
        self.blue = b
        self.green = g
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        Platforms.append(self)


platform1 = Platform(800, random.randint(400, 520), 300, 20, 5, random.randint(0, 255), random.randint(0, 255),
                     random.randint(0, 255))


class Hole:
    y = ground["y"]
    height = ground["height"]
    r = 255
    g = 255
    b = 255

    def __init__(self, x, width, scrollSpeed):
        self.x = x
        self.width = width
        self.scrollSpeed = scrollSpeed


hole1 = Hole((platform1.x - 25), (platform1.width + 50), platform1.scrollSpeed)
backgroundColor = (255, 255, 255)


# checks if a number is within two other numbers and then sets it equal to the closer number, designed for stopping the
# player from getting stuck inside a platform#

def check_inside(a, b, c):
    if a < b < c:
        if a > c:
            avg = (a - c) / 2
            if b - c > avg:
                return "a"
            else:
                return "c"
        else:
            avg = (c - a) / 2
            if b - a > avg:
                return "c"
            else:
                return "a"

    # else:
    # print("Double check inputs on check_inside()!")


# Supposed to be for detecting collisions, and it checks them well enough but I don't know how to make the character
# stop moving when they hit a platform#

# okay I'm having goddamn brain diarrhea here. I have collision detection """"working"""" in the sense that it knows
# when and which side of the platforms it's hitting but I have no idea how to make it stop# #Okay this is super weird,
# it doesn't function right on this project but it functions on my backup, still not complete function tho#

def detect_collisions():
    for Platform in Platforms:
        if check_inside(Platform.y, (player["y"] + player["height"]), (Platform.y + Platform.height)) == "a":
            if platform1.x < player["x"] and player["x"] + player["width"] < platform1.x + Platform.width:
                player["touchingPlatform"] = True
        else:
            player["touchingPlatform"] = False


while True:
    win.fill(backgroundColor)
    pygame.event.get()
    keys = pygame.key.get_pressed()
    detect_collisions()

    for Platform in Platforms:
        Platform.x -= Platform.scrollSpeed
        if Platform.x <= -200:
            Platform.x = 800
            Platform.y = random.randint(300, 520)
            Platform.red, Platform.blue, Platform.green = (
            random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            Platform.rect = pygame.Rect(Platform.x, Platform.y, Platform.width, Platform.height)
    hole1.x -= hole1.scrollSpeed

    if keys[pygame.K_LEFT]:
        if not (player["x"] <= 0):
            player["x"] -= player["Xspeed"]
        else:
            player["x"] = 0

    if keys[pygame.K_RIGHT]:
        if not ((player["x"] + player["width"]) >= 800):
            player["x"] += player["Xspeed"]
        else:
            player["x"] = 800 - player["width"]

    if keys[pygame.K_UP] and (player["y"] == (ground["y"] - player["height"]) or player["touchingPlatform"] == True):
        player["Yspeed"] = 20
        player["y"] -= player["Yspeed"]
    elif player["y"] < (ground["y"] - player["height"]) and player["touchingPlatform"] == False:
        if player["y"] - player["Yspeed"] < ground["y"] - player["height"]:
            player["Yspeed"] -= gravity
            player["y"] -= player["Yspeed"]
        else:
            player["y"] = ground["y"] - player["height"]
        # if hole1.x < player["x"] < hole1.x + 40:
    print(player["touchingPlatform"])

    if keys[pygame.K_DOWN] and player["y"] >= 520:
        if not (player["height"] == 4 and player["y"] == 556 and player["width"] == 76):
            player["height"] -= 4
            player["width"] += 4
            player["y"] += 4
    elif player["height"] < 40 and player["y"] > 520 and player["width"] > 40:
        player["height"] += 4
        player["width"] -= 4
        player["y"] -= 4

    player_rect = pygame.Rect(player["x"], player["y"], player["width"], player["height"])

    pygame.draw.rect(win, ground["color"], (ground["x"], ground["y"], ground["width"], ground["height"]))
    pygame.draw.rect(win, (255, 0, 0), player_rect)
    for Platform in Platforms:
        Platform.rect = pygame.Rect(Platform.x, Platform.y, Platform.width, Platform.height)
        pygame.draw.rect(win, (Platform.red, Platform.blue, Platform.green), Platform.rect)
        detect_collisions()
    pygame.draw.rect(win, (hole1.r, hole1.g, hole1.b), (hole1.x, hole1.y, hole1.width, hole1.height))

    pygame.display.update()
    clock.tick(fps)
    time.sleep(1 / 100)

import pygame, time, random

Platforms = []

ground = {
    "x": 0,
    "y": 560,
    "width": 800,
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
    def __init__(self, x, y, width, height, scrollSpeed, r, b, g):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.scrollSpeed = scrollSpeed
        self.color = (r, g, b)
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        Platforms.append(self)

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


class game(Platform, Hole):
    def __init__(self, Platforms):
        self.gravity = 1
        self.score = 0
        self.score_list = []
        self.Platforms = Platforms
        self.clock = pygame.time.Clock()
        self.fps = 60
        gameDisplay.__init__(self)
        self.play()

    def moveRight(self):
        availableRoom = player["Xspeed"]
        if player["x"] + player["width"] + player["Xspeed"] > 800:
            availableRoom = (800 - (player["x"] + player["width"]))
        else:
            for platform in self.Platforms:
                besidePlatform = (platform.y < player["y"] < platform.y + platform.height) or (platform.y < player["y"] + player["height"] < platform.y + platform.height)
                if (player["x"] + player["width"] + player["Xspeed"] > platform.x) and besidePlatform:
                    availableRoom = (platform.x - (player["x"] + player["width"]))
        player["x"] += availableRoom

    def moveLeft(self):
        availableRoom = player["Xspeed"]
        if player["x"] - player["Xspeed"] < 0:
            availableRoom = player["x"]
        else:
            for platform in self.Platforms:
                besidePlatform = (platform.y < player["y"] < platform.y + platform.height) or (platform.y < player["y"] + player["height"] < platform.y + platform.height)
                if (player["x"] - player["Xspeed"] < platform.x + platform.width) and besidePlatform:
                    availableRoom = player["x"] - (platform.x + platform.width)
        player["x"] -= availableRoom

    def play(self):
        running = True
        while running:
            keys = pygame.key.get_pressed()

            if keys[pygame.K_LEFT]:
                self.moveLeft()
            if keys[pygame.K_RIGHT]:
                self.moveRight()

            gameDisplay.drawGame(self, Platforms = self.Platforms)
            self.clock.tick(self.fps)
            time.sleep(1/100)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False


class gameDisplay():
    def __init__(self):
        pygame.init()
        self.W, self.H = 800, 600
        self.win = pygame.display.set_mode((self.W, self.H))
        pygame.display.set_caption('Platformer')
        pygame.event.clear()
        self.bg = (255, 255, 255)
        pygame.display.update()

    def drawGame(self, Platforms = []):
        self.win.fill(self.bg)
        player_rect = pygame.Rect(player["x"], player["y"], player["width"], player["height"])
        pygame.draw.rect(self.win, ground["color"], (ground["x"], ground["y"], ground["width"], ground["height"]))
        pygame.draw.rect(self.win, (255, 0, 0), player_rect)
        if len(Platforms) > 0:
            for Platform in Platforms:
                Platform.rect = pygame.Rect(Platform.x, Platform.y, Platform.width, Platform.height)
                pygame.draw.rect(self.win, Platform.color, Platform.rect)
        pygame.display.update()

fun = game(Platforms)
# running = True
# while running:

#     pygame.event.get()
#     

#     for Platform in Platforms:
#         Platform.x -= Platform.scrollSpeed
#         if Platform.x <= -200:
#             Platform.x = 800
#             Platform.y = random.randint(300, 520)
#             Platform.red, Platform.blue, Platform.green = (
#             random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
#             Platform.rect = pygame.Rect(Platform.x, Platform.y, Platform.width, Platform.height)
#     hole1.x -= hole1.scrollSpeed

#     if keys[pygame.K_LEFT]:
#         if not (player["x"] <= 0):
#             player["x"] -= player["Xspeed"]
#         else:
#             player["x"] = 0

#     if keys[pygame.K_UP] and (player["y"] == (ground["y"] - player["height"]) or player["touchingPlatform"] == True):
#         player["Yspeed"] = 20
#         player["y"] -= player["Yspeed"]
#     elif player["y"] < (ground["y"] - player["height"]) and player["touchingPlatform"] == False:
#         if player["y"] - player["Yspeed"] < ground["y"] - player["height"]:
#             player["Yspeed"] -= gravity
#             player["y"] -= player["Yspeed"]
#         else:
#             player["y"] = ground["y"] - player["height"]
#         # if hole1.x < player["x"] < hole1.x + 40:
#     print(player["touchingPlatform"])

#     if keys[pygame.K_DOWN] and player["y"] >= 520:
#         if not (player["height"] == 4 and player["y"] == 556 and player["width"] == 76):
#             player["height"] -= 4
#             player["width"] += 4
#             player["y"] += 4
#     elif player["height"] < 40 and player["y"] > 520 and player["width"] > 40:
#         player["height"] += 4
#         player["width"] -= 4
#         player["y"] -= 4


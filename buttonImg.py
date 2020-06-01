import pygame

class ButtonImg:
    def __init__(self, name, x, y, imgPaths):
        self.name = name
        self.x = x
        self.y = y
        self.surfaces = []
        for imgPath in imgPaths:
            surface = pygame.image.load(imgPath)
            self.surfaces.append(surface)
        self.width = self.surfaces[0].get_width()
        self.height = self.surfaces[0].get_height()
        print(self.width)
        print(self.height)
        self.STATE = 0
        self.STATE_NORMAL = 0
        self.STATE_HOVER = 1
        self.STATE_CLICKED = 2

    def draw(self, win):
        win.blit(self.surfaces[self.STATE], (self.x, self.y))

    def isClicked(self, pos):
        x1 = pos[0]
        y1 = pos[1]
        if self.x <= x1 <= self.x + self.width and self.y <= y1 <= self.y + self.height:
            self.STATE = self.STATE_CLICKED
            print('TRUE')
            return True
        else:
            print('FALSE')
            self.STATE = self.STATE_NORMAL
            return False

    def onClick(self):
        self.STATE = self.STATE_CLICKED
    def onHover(self):
        self.STATE = self.STATE_HOVER
    def onNormal(self):
        self.STATE = self.STATE_NORMAL


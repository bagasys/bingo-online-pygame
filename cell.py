from button import Button
import pygame

class Cell():
    def __init__(self, text, font_size, x, y, width, height, color):
        self.text = text
        self.x = x
        self.y = y
        self.color = color
        self.width = width
        self.height = height
        self.font_size = font_size
        self.coret = False

    def draw(self, win):
        if self.coret:
            self.color = (255, 0, 255)
        if self.selected:
            self.color = (0, 255, 255)
        else:
            self.color = (0, 255, 0)
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height))
        font = pygame.font.SysFont("comicsans", self.font_size)
        text = font.render(self.text, 1, (255, 255, 255))
        win.blit(text, (self.x + round(self.width / 2) - round(text.get_width() / 2),
                        self.y + round(self.height / 2) - round(text.get_height() / 2)))

    def isClicked(self, pos):
        x1 = pos[0]
        y1 = pos[1]
        if self.x <= x1 <= self.x + self.width and self.y <= y1 <= self.y + self.height:
            return True
        else:
            return False
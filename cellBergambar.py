import pygame

class CellBergambar():
    def __init__(self, id, text, x, y):
        self.id = id
        self.text = text
        self.surfaces = []
        self.surfaces.append(pygame.image.load('cell_normal.png'))
        self.surfaces.append(pygame.image.load('cell_pilih.png'))
        self.surfaces.append(pygame.image.load('cell_coret.png'))
        self.x = x
        self.y = y
        self.width = self.surfaces[0].get_width()
        self.height = self.surfaces[0].get_height()
        self.STATE = 0
        self.STATE_NORMAL = 0
        self.STATE_PILIH = 1
        self.STATE_CORET = 2
        self.font_size = 30



    def draw(self, win, tulisan, tercoret, terpilih):
        if tulisan == None:
            self.text = ''
        else:
            self.text = tulisan

        if tercoret:
            self.STATE = self.STATE_CORET
        elif terpilih:
            self.STATE = self.STATE_PILIH
        else:
            self.STATE = self.STATE_NORMAL

        win.blit(self.surfaces[self.STATE], (self.x, self.y))
        font = pygame.font.SysFont("comicsans", self.font_size)
        text = font.render(str(self.text), 1, (94, 100, 114))
        win.blit(text, (self.x + round(self.width / 2) - round(text.get_width() / 2),
                        self.y + round(self.height / 2) - round(text.get_height() / 2)))

    def isClicked(self, pos):
        x1 = pos[0]
        y1 = pos[1]
        if self.x <= x1 <= self.x + self.width and self.y <= y1 <= self.y + self.height:
            return True
        else:
            return False
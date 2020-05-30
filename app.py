import pygame
from network import Network
from button import Button

class App:
    def __init__(self):
        pygame.init()
        self.run = True
        self.screen = pygame.display.set_mode((800, 600))

    def start(self):
        while self.run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run = False
        pygame.quit()

    def handle_welcome(self):
        pass

    def handle_play(self):
        pass

    def handle_winner(self):
        pass

    def redrawWindow(self):
        self.screen.fill((128, 128, 128))
        pygame.display.update()


if __name__ == "__main__":
    app = App()
    app.start()
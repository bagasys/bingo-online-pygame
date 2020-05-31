import pygame
from network import Network
from button import Button
from text import Text

class App:
    def __init__(self):
        pygame.init()
        self.RUNNING = True
        self.width = 800
        self.height = 600
        self.CAPTION = "BINGO!"
        self.SCREEN_RESOLUTION = (self.width, self.height)

        self.screen = pygame.display.set_mode(self.SCREEN_RESOLUTION)

        self.GAME_STATE = 1
        self.STATE_WELCOME = 1
        self.STATE_PLAY = 2
        self.STATE_WINNER = 3
        self.STATE_HOWTOPLAY = 4
        self.STATE_PREPAREPLAY = 5
        self.count = 1
        self.clock = pygame.time.Clock()
        self.texts_welcome = [Text("BINGO!", 80, 350, 50, 60, 100, (0, 0, 0)),]
        self.buttons_welcome = [Button("Join Game", 30, 300, 250, 120, 60, (0, 255, 0)),
                                Button("How To Play", 30, 300, 320, 130, 60, (0, 255, 255)),
                                Button("Prepare Play", 30, 300, 390, 130, 60, (0, 255, 255))]

        self.texts_play = [Text("PLAY", 80, 350, 50, 60, 100, (0, 0, 0)), ]
        self.texts_howtoplay = [Text("HOW TO PLAY", 80, 350, 50, 60, 100, (0, 0, 0)), ]
        self.buttons_howtoplay = [Button("Home", 30, 300, 390, 120, 60, (0, 255, 0))]

        self.texts_prepareplay = [Text("Selected Number", 40, 625, 150, 60, 100, (0, 0, 0)),
                                  Text("", 40, 625, 200, 60, 100, (0, 0, 0))]
        self.texts_confirmprepareplay = [Text("Confirm", 40, 625, 250, 60, 100, (0, 0, 0))]
        self.buttons_prepareplay = []

        for row in range(5):
            for column in range(5):
                x = 100 + 80 * column + 5 * column
                y = 100 + 80 * row + 5 * row
                self.buttons_temp = Button("", 30, x, y, 80, 80, (0, 255, 0))
                self.buttons_prepareplay.append(self.buttons_temp)


        self.game = None
        self.net = None
        self.player = None

    def start(self):
        while self.RUNNING:
            self.clock.tick(10)
            if self.GAME_STATE == self.STATE_WELCOME:
                self.handle_welcome()
            elif self.GAME_STATE == self.STATE_PLAY:
                self.handle_play()
            elif self.GAME_STATE == self.STATE_WINNER:
                self.handle_winner()
            elif self.GAME_STATE == self.STATE_HOWTOPLAY:
                self.handle_howtoplay()
            elif self.GAME_STATE == self.STATE_PREPAREPLAY:
                self.handle_prepareplay()
        pygame.quit()

    def handle_welcome(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.RUNNING = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                click_pos = pygame.mouse.get_pos()
                for btn in self.buttons_welcome:
                    if btn.isClicked(click_pos):
                        if btn.text == "Join Game":
                            self.GAME_STATE = self.STATE_PLAY
                            return
                        elif btn.text == "How To Play":
                            self.GAME_STATE = self.STATE_HOWTOPLAY
                            return
                        elif btn.text == "Prepare Play":
                            self.GAME_STATE = self.STATE_PREPAREPLAY
                            return

        # Gambar-gambar
        self.screen.fill((128, 128, 128))
        for button in self.buttons_welcome:
            button.draw(self.screen)

        for text in self.texts_welcome:
            text.draw(self.screen)

        pygame.display.update()

    def handle_howtoplay(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.RUNNING = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                click_pos = pygame.mouse.get_pos()
                for btn in self.buttons_howtoplay:
                    if btn.isClicked(click_pos):
                        if btn.text == "Home":
                            self.GAME_STATE = self.STATE_WELCOME
                            return
                        

        # Gambar-gambar
        self.screen.fill((128, 128, 128))
        for button in self.buttons_howtoplay:
            button.draw(self.screen)

        for text in self.texts_howtoplay:
            text.draw(self.screen)
        pygame.display.update()

    def handle_play(self):
        # print('play')
        if not self.net:
            self.net = Network()
            try:
                self.player = int(self.net.getP())
                print(self.player)
            except:
                self.run = False
                print("app: Can't get player info")
            try:
                data = {}
                data['type'] = 'join'
                data['payload'] = None
                self.game = self.net.send(data)
            except:
                self.run = False
                print("app: Couldn't get game\n")

        # Event Handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.RUNNING = False

        if self.game.state == self.game.STATE_WAIT:
            # Gambar-gambar
            self.screen.fill((128, 128, 128))
            # TO DO: Check if Waiting.
            # count_player = 2
            count_player = self.game.countPlayer()
            waiting_text = "waiting player-({}/5)...".format(count_player)
            waiting_font = pygame.font.SysFont("comicsans", 80)
            waiting_surface = waiting_font.render(waiting_text, 0, (255, 255, 255))
            self.screen.blit(waiting_surface, (
            self.width / 2 - waiting_surface.get_width() / 2, self.height / 2 - waiting_surface.get_height() / 2))
            pygame.display.update()

        elif self.game.state == self.game.STATE_PLAY:
            pass





    def handle_winner(self):
        pass


    def redrawWindow(self):
        pygame.display.update()

    def handle_prepareplay(self):
        # Event Handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.RUNNING = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                click_pos = pygame.mouse.get_pos()
                for btn in self.buttons_prepareplay:
                    if btn.isClicked(click_pos):
                        if (self.count <= 25 and btn.text == ""):
                            btn.text = str(self.count)
                            self.count += 1
                        self.GAME_STATE = self.STATE_PREPAREPLAY
                        return

        # Gambar-gambar
        self.screen.fill((128, 128, 128))
        for button in self.buttons_prepareplay:
            button.draw(self.screen)

        if (self.count <= 25):
            self.texts_prepareplay[1].text = str(self.count)
        else:
            self.texts_prepareplay[1].text = "-"

        for text in self.texts_prepareplay:
            text.draw(self.screen)

        if (self.count > 25):
            for text in self.texts_confirmprepareplay:
                text.draw(self.screen)
        pygame.display.update()


if __name__ == "__main__":
    app = App()
    app.start()
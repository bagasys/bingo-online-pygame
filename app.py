import pygame
from network import Network
from button import Button
from text import Text

class App:
    def __init__(self):
        pygame.init()
        self.count = 1
        self.RUNNING = True
        self.width = 800
        self.height = 600
        self.CAPTION = "BINGO!"
        self.SCREEN_RESOLUTION = (self.width, self.height)
        self.frame_count = 0

        self.screen = pygame.display.set_mode(self.SCREEN_RESOLUTION)
        self.update_count = 0

        self.DISPLAY = 0
        self.DISPLAY_WELCOME = 0
        self.DISPLAY_HOWTOPLAY = 1
        self.DISPLAY_PREPARE = 2
        self.DISPLAY_PLAY = 3

        self.clock = pygame.time.Clock()

        self.game = None
        self.net = None
        self.player = None

        self.texts_welcome = [Text("BINGO!", 80, 350, 50, 60, 100, (0, 0, 0)), ]
        self.buttons_welcome = [Button("Join Game", 30, 300, 250, 120, 60, (0, 255, 0)),
                                Button("How To Play", 30, 300, 320, 130, 60, (0, 255, 255)),
                                Button("Prepare Play", 30, 300, 390, 130, 60, (0, 255, 255))]

        self.texts_play = [Text("PLAY", 80, 350, 50, 60, 100, (0, 0, 0)), ]
        self.texts_howtoplay = [Text("HOW TO PLAY", 80, 350, 50, 60, 100, (0, 0, 0)), ]
        self.buttons_howtoplay = [Button("Home", 30, 300, 390, 120, 60, (0, 255, 0))]

        self.texts_prepareplay = [Text("Selected Number", 40, 625, 150, 60, 100, (0, 0, 0)),
                                  Text("", 40, 625, 200, 60, 100, (0, 0, 0))]
        self.buttons_preparefinish = [Button("Confirm", 40, 625, 250, 60, 100, (0, 0, 0))]
        self.buttons_prepareplay = []

        for row in range(5):
            for column in range(5):
                x = 100 + 80 * column + 5 * column
                y = 100 + 80 * row + 5 * row
                self.buttons_temp = Button("", 30, x, y, 80, 80, (0, 255, 0))
                self.buttons_prepareplay.append(self.buttons_temp)

    def start(self):
        while self.RUNNING:
            self.clock.tick(10)
            if self.DISPLAY == self.DISPLAY_WELCOME:
                self.handleWelcome()
            if self.DISPLAY == self.DISPLAY_PLAY:
                self.onPlay()
            if self.DISPLAY == self.DISPLAY_HOWTOPLAY:
                self.handleHowtoplay()

    def handleWelcome(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.RUNNING = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                click_pos = pygame.mouse.get_pos()
                for btn in self.buttons_welcome:
                    if btn.isClicked(click_pos):
                        if btn.text == "Join Game":
                            self.DISPLAY = self.DISPLAY_PLAY
                            return
                        elif btn.text == "How To Play":
                            self.DISPLAY = self.DISPLAY_HOWTOPLAY
                            return
                        elif btn.text == "Prepare Play":
                            self.DISPLAY = self.DISPLAY_PREPARE
                            return

        # Gambar-gambar
        self.screen.fill((128, 128, 128))
        for button in self.buttons_welcome:
            button.draw(self.screen)

        for text in self.texts_welcome:
            text.draw(self.screen)

        pygame.display.update()

    def handleHowtoplay(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.RUNNING = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                click_pos = pygame.mouse.get_pos()
                for btn in self.buttons_howtoplay:
                    if btn.isClicked(click_pos):
                        if btn.text == "Home":
                            self.DISPLAY = self.DISPLAY_WELCOME
                            return
        # Gambar-gambar
        self.screen.fill((128, 128, 128))
        for button in self.buttons_howtoplay:
            button.draw(self.screen)

        for text in self.texts_howtoplay:
            text.draw(self.screen)
        pygame.display.update()

    def onPlay(self):
        if not self.updateGameData():
            return

        if self.game.STATE == self.game.STATE_WAIT:
            self.handleWait()

        elif self.game.STATE == self.game.STATE_FILL:
            self.handlePrepare()
        
        elif self.game.STATE == self.game.STATE_PLAY:
            self.handlePlay()

    def handlePlay(self):
        self.screen.fill((0, 0, 1))
        waiting_text = "PLAY"
        waiting_font = pygame.font.SysFont("comicsans", 80)
        waiting_surface = waiting_font.render(waiting_text, 0, (255, 255, 255))
        self.screen.blit(waiting_surface, (
            self.width / 2 - waiting_surface.get_width() / 2, self.height / 2 - waiting_surface.get_height() / 2))
        pygame.display.update()

    def handlePrepare(self):
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
                            self.player.tableCoret.append(self.count)
                            self.player.table.append(False)
                            self.count += 1
                for btn in self.buttons_preparefinish:
                    if btn.isClicked(click_pos):
                        if (self.count > 25):
                            data = {}
                            data['type'] = 'updateTable'
                            data['payload'] = self.player
                            self.game = self.net.send(data)
                            print("app: ke click woy")
                            break

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
            for btn in self.buttons_preparefinish:
                btn.draw(self.screen)
        pygame.display.update()


    def handleWait(self):
        if self.game.STATE == self.game.STATE_WAIT:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.RUNNING = False

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

    def updateGameData(self):
        if not self.net:
            self.net = Network()
            try:
                data = {}
                data['type'] = 'join'
                data['payload'] = None
                try:
                    self.game = self.net.send(data)
                except:
                    print("app: gagal dapet game pas awal")
                self.player = self.game.players[int(self.net.id)]
                return True
            except:
                self.run = False
                print("app: Couldn't get game\n")
                return False
        else:
            if self.frame_count == 29:
                data = {}
                data['type'] = 'update'
                data['payload'] = None
                print(data)
                self.game = self.net.send(data)
                self.player = self.game.players[int(self.net.id)]
            self.frame_count = ( self.frame_count + 1 ) % 30
            return True

if __name__ == "__main__":
    app = App()
    app.start()
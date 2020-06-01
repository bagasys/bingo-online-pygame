import pygame
from network import Network
from button import Button
from text import Text
from tableBergambar import TabelBergambar
from buttonImg import ButtonImg
class App:
    def __init__(self):


        self.selectedNumber = None
        self.tabel = TabelBergambar()

        pygame.init()
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
        self.indeksTabel = 0

        self.texts_welcome = [Text("BINGO!", 80, 350, 50, 60, 100, (0, 0, 0)), ]


        self.texts_play = [Text("PLAY", 80, 350, 50, 60, 100, (0, 0, 0)), ]
        self.texts_howtoplay = [Text("HOW TO PLAY", 80, 350, 50, 60, 100, (0, 0, 0)), ]
        self.buttons_howtoplay = [Button("Home", 30, 300, 390, 120, 60, (0, 255, 0))]

        self.texts_prepareplay = [Text("Selected Number", 40, 625, 150, 60, 100, (0, 0, 0)),
                                  Text("", 40, 625, 200, 60, 100, (0, 0, 0))]

        self.buttons_preparefinish = [Button("Confirm", 40, 625, 250, 60, 100, (0, 0, 0))]

        self.texts_play = [Text("Selected Number", 40, 625, 150, 60, 100, (0, 0, 0)),]

        self.texts_winplay = [Text("Winner", 40, 550, 150, 60, 100, (0, 0, 0)),
                              Text("", 40, 550, 0, 60, 100, (0, 0, 0)),
                              Text("", 40, 550, 0, 60, 100, (0, 0, 0)),
                              Text("", 40, 550, 0, 60, 100, (0, 0, 0)),
                              Text("", 40, 550, 0, 60, 100, (0, 0, 0)),
                              Text("", 40, 550, 0, 60, 100, (0, 0, 0))]
        
        self.buttons_tabelwinplay = [Button("Lihat Tabel", 30, 625, 230, 125, 30, (0, 255, 0)),
                                    Button("Lihat Tabel", 30, 625, 280, 125, 30, (0, 255, 0)),
                                    Button("Lihat Tabel", 30, 625, 330, 125, 30, (0, 255, 0)),
                                    Button("Lihat Tabel", 30, 625, 380, 125, 30, (0, 255, 0)),
                                    Button("Lihat Tabel", 30, 625, 430, 125, 30, (0, 255, 0))]

        self.texts_winnername = [Text("", 40, 300, 10, 60, 100, (0, 0, 0)),]

        self.buttons_winplay = [Button("Play Again", 30, 450, 150, 120, 60, (0, 255, 0)),
                                Button("Back to Home", 30, 450, 220, 130, 60, (0, 255, 255)),]

        self.button_send = Button("Send", 40, 625, 250, 60, 100, (0, 0, 0))

        self.background = pygame.image.load('background.png')
        self.background_mainmenu = pygame.image.load('main_menu.png')
        self.background_wait = pygame.image.load('wait_screen.png')
        btn_join = ButtonImg('join' ,0, 0, ['Join Game netral.png', 'Join Game hover.png', 'Join Game clicked.png'])
        btn_howtoplay = ButtonImg('how_to_play' ,0, 0, ['How to Play netral.png', 'How to Play hover.png', 'How To Play clicked.png'])
        btn_finish = ButtonImg('finish', 0, 0, ['Finish netral.png', 'Finish hover.png', 'Finish clicked.png'])
        btn_confirm = ButtonImg('confirm',0, 0, ['Confirm netral.png', 'Confirm hover.png', 'Confirm clicked.png'])
        btn_backtomenu = ButtonImg('back_to_menu', 0, 0, ['Back to Menu netral.png', 'Back to Menu hover.png', 'Back to Menu clicked.png'])
        self.buttons_welcome = [ButtonImg('join' ,300, 300, ['Join Game netral.png', 'Join Game hover.png', 'Join Game clicked.png']), ButtonImg('how_to_play' ,300, 350, ['How to Play netral.png', 'How to Play hover.png', 'How To Play clicked.png'])]
        self.buttons_howtoplay = [ButtonImg('back_to_menu', 300, 450, ['Back to Menu netral.png', 'Back to Menu hover.png', 'Back to Menu clicked.png'])]
        self.buttons_prepare = [ButtonImg('finish', 555, 330, ['Finish netral.png', 'Finish hover.png', 'Finish clicked.png'])]
        self.buttons_play = [ButtonImg('confirm',555, 330, ['Confirm netral.png', 'Confirm hover.png', 'Confirm clicked.png']),]

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

            click_pos = pygame.mouse.get_pos()
            if event.type == pygame.MOUSEBUTTONUP:
                for btn in self.buttons_welcome:
                    if btn.isClicked(click_pos):
                        btn.onNormal()
                        if btn.name == "join":
                            self.DISPLAY = self.DISPLAY_PLAY
                        elif btn.name == "how_to_play":
                            self.DISPLAY = self.DISPLAY_HOWTOPLAY

            elif event.type == pygame.MOUSEBUTTONDOWN:
                for btn in self.buttons_welcome:
                    if btn.isClicked(click_pos):
                        btn.onClick()
                        if btn.name == "join":
                            pass
                        elif btn.name == "how_to_play":
                            print('Click down HTP')

            else:
                for btn in self.buttons_welcome:
                    if btn.isClicked(click_pos):
                        btn.onHover()
                        if btn.name == "join":
                            print('Click up Join')
                        elif btn.name == "how_to_play":
                            print('Click up HTP')
                    else:
                        btn.onNormal()



        # Gambar-gambar
        self.screen.blit(self.background_mainmenu, (0, 0))
        for btn in self.buttons_welcome:
            btn.draw(self.screen)

        pygame.display.update()

    def handleHowtoplay(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.RUNNING = False

            click_pos = pygame.mouse.get_pos()
            if event.type == pygame.MOUSEBUTTONUP:
                for btn in self.buttons_howtoplay:
                    if btn.isClicked(click_pos):
                        btn.onNormal()
                        if btn.name == "back_to_menu":
                            self.DISPLAY = self.DISPLAY_WELCOME

            elif event.type == pygame.MOUSEBUTTONDOWN:
                for btn in self.buttons_howtoplay:
                    if btn.isClicked(click_pos):
                        btn.onClick()
            else:
                for btn in self.buttons_howtoplay:
                    if btn.isClicked(click_pos):
                        btn.onHover()
                    else:
                        btn.onNormal()

        # Gambar-gambar
        self.screen.blit(self.background, (0, 0))
        for btn in self.buttons_howtoplay:
            btn.draw(self.screen)

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

        elif self.game.STATE == self.game.STATE_WIN:
            self.handleWin()

    def handleWin(self):
        indeks = 0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.RUNNING = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                click_pos = pygame.mouse.get_pos()    
                for btn in self.buttons_tabelwinplay:       
                    if btn.isClicked(click_pos):
                        if btn.text == "Lihat Tabel":         
                            self.indeksTabel = indeks            
                            return
                    indeks += 1

        self.screen.fill((128, 128, 128))
        self.game.winners[self.indeksTabel]['tabel'].draw(self.screen)
            # self.game.winners[0]['tabel'].draw(self.screen)
        count = 0
        for btn in self.buttons_tabelwinplay:
            if(count < len(self.game.winners)):
                btn.draw(self.screen)
            count += 1

        for i in range (len(self.game.winners)):
            self.texts_winplay[i + 1].text = str(self.game.winners[i]['id'])
            self.texts_winplay[i + 1].y = 150 + (i + 1) * 50
     
        for text in self.texts_winplay:
            text.draw(self.screen)
        
        for winner in self.texts_winnername:
            winner.text = "player " + str(self.game.winners[self.indeksTabel]['id']) + " table"
            winner.draw(self.screen)

        pygame.display.update()

    def handlePlay(self):
        # Event Handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.RUNNING = False

            click_pos = pygame.mouse.get_pos()
            if event.type == pygame.MOUSEBUTTONUP:
                for btn in self.buttons_play:
                    if btn.isClicked(click_pos):
                        btn.onNormal()
                        if btn.name == "confirm" and self.tabel.angkaTerpilih != None:
                            data = {}
                            data['type'] = 'coret'
                            data['payload'] = self.tabel.angkaTerpilih
                            self.game = self.net.send(data)
                            self.player = self.game.players[self.net.id]
                            self.tabel.tabelCoret = self.player.tableCoret

            elif event.type == pygame.MOUSEBUTTONDOWN:
                idx_clicked = self.tabel.checkClick(click_pos)
                print(idx_clicked)
                if idx_clicked != -1:
                    self.tabel.pilihKotak(idx_clicked)

                for btn in self.buttons_play:
                    if btn.isClicked(click_pos):
                        btn.onClick()
            else:
                for btn in self.buttons_howtoplay:
                    if btn.isClicked(click_pos):
                        btn.onHover()
                    else:
                        btn.onNormal()


        #Gambar gambar
        self.screen.blit(self.background, (0, 0))

        self.tabel.draw(self.screen)

        for btn in self.buttons_play:
            btn.draw(self.screen)

        # for text in self.texts_prepareplay:
        #     text.draw(self.screen)

        selected_text = "Selected Number: {}".format(self.selectedNumber)
        selected_font = pygame.font.SysFont("comicsans", 25)
        selected_surface = selected_font.render(selected_text, 0, (255, 255, 255))
        self.screen.blit(selected_surface, (600, 250))

        player_text = "you are player X"
        player_font = pygame.font.SysFont("comicsans", 18)
        player_surface = player_font.render(player_text, 0, (255, 255, 255))
        self.screen.blit(player_surface, (10, 10))

        turn_text = "Player's Y Turn"
        turn_font = pygame.font.SysFont("comicsans", 20)
        turn_surface = turn_font.render(player_text, 0, (255, 255, 255))
        self.screen.blit(turn_surface, (300, 10))

        yourturn_text = "Player's Y Turn"
        yourturn_font = pygame.font.SysFont("comicsans", 20)
        yourturn_surface = yourturn_font.render(player_text, 0, (255, 255, 255))
        self.screen.blit(yourturn_surface, (300, 30))

        pygame.display.update()

    def handlePrepare(self):
        # Event Handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.RUNNING = False

            click_pos = pygame.mouse.get_pos()

            if event.type == pygame.MOUSEBUTTONUP:
                for btn in self.buttons_prepare:
                    if btn.isClicked(click_pos):
                        btn.onNormal()
                        if btn.name == 'finish':
                            if (self.tabel.count_isi > 24):
                                data = {}
                                data['type'] = 'isiTable'
                                data['payload'] = self.tabel.tabel
                                print('payload:', data['payload'])
                                self.game = self.net.send(data)
                                break

            elif event.type == pygame.MOUSEBUTTONDOWN:
                idx_clicked = self.tabel.checkClick(click_pos)
                print(idx_clicked)
                if idx_clicked != -1:
                    self.tabel.isiTabel(idx_clicked)

                for btn in self.buttons_prepare:
                    if btn.isClicked(click_pos):
                        btn.onClick()
            else:
                for btn in self.buttons_prepare:
                    if btn.isClicked(click_pos):
                        btn.onHover()
                    else:
                        btn.onNormal()

        # Gambar-gambar
        self.screen.blit(self.background, (0, 0))
        self.tabel.draw(self.screen)
        if (self.tabel.count_isi > 24):
            for btn in self.buttons_prepare:
                btn.draw(self.screen)
        pygame.display.update()

    def handleWait(self):
        if self.game.STATE == self.game.STATE_WAIT:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.RUNNING = False

            # Gambar-gambar
            self.screen.blit(self.background_wait, (0, 0))
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
                self.player = self.game.players[self.net.id]
                self.tabel.tabelCoret = self.player.tableCoret
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
                self.game = self.net.send(data)
                self.player = self.game.players[int(self.net.id)]
                self.tabel.tabelCoret = self.player.tableCoret
                print('tabel coret terbaru:')
                print(self.player.tableCoret)
            self.frame_count = ( self.frame_count + 1 ) % 30
            return True

if __name__ == "__main__":
    app = App()
    app.start()
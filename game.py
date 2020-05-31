from player import Player

class Game:
    def __init__(self, id):
        self.players = []
        self.last_number = 0
        self.current_number = 0

        self.READY = False
        self.MAX_PLAYER = 2

        self.STATE = 0
        self.STATE_WAIT = 0
        self.STATE_FILL = 1
        self.STATE_PLAY = 2

    def isReadyToFill(self):
        return len(self.players) == self.MAX_PLAYER

    def isReadyToPlay(self):
        for i in range(self.MAX_PLAYER):
            print("game: PLAYER YG DICEK", self.players[i].readyToPlay)
            if self.players[i].readyToPlay == False:
                print("game: FALSE")
                return False
        print("game: TRUEEEEE")
        return True

    def addPlayer(self, player_id, game_id):
        newPlayer = Player(player_id, game_id)
        self.players.append(newPlayer)

    def startFill(self):
        self.STATE = self.STATE_FILL

    def startPlay(self):
        self.STATE = self.STATE_PLAY

    def countPlayer(self):
        return len(self.players)
        
    def updatePlayer(self, player_id, player):
        self.players[int(player_id)] = player

    def isWinner(self, id):
        for i in range (5):
            win = 1
            for j in range (25):
                if(j % 5 == i and self.players[int(id)].tableCoret[j] == False):
                    win = 0
                    break
            if(win == 1):
                return True



class Game:
    def __init__(self, id):
        self.players = []
        self.chosen_number = False
        self.player_order = []
        self.state = 0
        self.STATE_WAIT = 0
        self.STATE_PLAY = 1
        self.PLAYER_MAX = 5
        # self.winner_isoke 

        self.p1Went = False
        self.p2Went = False
        self.ready = False
        self.id = id
        self.moves = [None, None]
        self.wins = [0,0]
        self.ties = 0


    def get_player_move(self, p):
        """
        :param p: [0,1]
        :return: Move
        """
        return self.moves[p]

    def play(self, player, move):
        self.moves[player] = move
        if player == 0:
            self.p1Went = True
        else:
            self.p2Went = True

    def connected(self):
        return self.ready

    def addPlayer(self, player):
        self.players.append(player)
        if self.countPlayer() == self.PLAYER_MAX:
            self.state = self.STATE_PLAY

    def countPlayer(self):
        return len(self.players)

    def isRoomFull(self):
        if self.countPlayer() == 5:
            return True
    
    def bothWent(self):
        return self.p1Went and self.p2Went

    def setTable(self, player, table):
        self.players[player].table = table
        print(self.players[player].table)
        if player == 0:
            self.p1Table = True
        elif player == 1:
            self.p2Table = True
        elif player == 2:
            self.p3Table = True
        elif player == 3:
            self.p4Table = True
        elif player == 4:
            self.p5Table = True

    def winner(self):

        p1 = self.moves[0].upper()[0]
        p2 = self.moves[1].upper()[0]

        winner = -1
        if p1 == "R" and p2 == "S":
            winner = 0
        elif p1 == "S" and p2 == "R":
            winner = 1
        elif p1 == "P" and p2 == "R":
            winner = 0
        elif p1 == "R" and p2 == "P":
            winner = 1
        elif p1 == "S" and p2 == "P":
            winner = 0
        elif p1 == "P" and p2 == "S":
            winner = 1

        return winner

    def resetWent(self):
        self.p1Went = False
        self.p2Went = False
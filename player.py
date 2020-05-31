class Player:
    def __init__(self, id, game_id):
        self.id = id
        self.game_id = game_id
        self.table = []
        self.tableCoret = []
        self.readyToPlay = False

        for i in range(25):
            self.table.append(0)
            self.tableCoret.append(False)

    def imReady(self):
        self.readyToPlay = True
        print("player: INI READY GAES", self.readyToPlay)
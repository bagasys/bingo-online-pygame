class Player:
    def __init__(self, id, game_id):
        self.id = id
        self.game_id = game_id
        self.table = []
        self.tableCoret = []

        for i in range(25):
            self.table.append(0)
            self.tableCoret.append(False)
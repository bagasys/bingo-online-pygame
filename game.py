from player import Player
from tableBergambar import TabelBergambar
from tabel import Tabel
class Game:
    def __init__(self, id):
        self.players = []
        self.last_number = 0
        self.current_number = 0

        self.READY = False
        self.MAX_PLAYER = 5
        self.winners = []
        self.winnertable = []

        self.STATE = 0
        self.STATE_WAIT = 0
        self.STATE_FILL = 1
        self.STATE_PLAY = 2
        self.STATE_WIN = 3

        self.GILIRAN = 0

    def isReadyToFill(self):
        return len(self.players) == self.MAX_PLAYER

    def isReadyToPlay(self):
        for i in range(self.MAX_PLAYER):
            if self.players[i].readyToPlay == False:
                return False
        return True

    def addPlayer(self, player_id, game_id):
        newPlayer = Player(player_id, game_id)
        self.players.append(newPlayer)

    def startFill(self):
        self.STATE = self.STATE_FILL

    def startPlay(self):
        self.STATE = self.STATE_PLAY
    
    def winPlay(self):
        self.STATE = self.STATE_WIN

    def countPlayer(self):
        return len(self.players)

    def isiTable(self, player_id, newTable):
        self.players[int(player_id)].table = newTable
        print(self.players[int(player_id)].table)

    def isWinner(self, player_id):
        # cek vertikal
        for i in range (5):
            win = 1
            for j in range (25):
                if(j % 5 == i and self.players[int(player_id)].tableCoret[j] == False):
                    win = 0
                    break
            if(win == 1):
                print("ada vertikal")
                return True
        # cek horizontal
        for i in range (5):
            win = 1
            for j in range (25):
                if(j // 5 == i and self.players[int(player_id)].tableCoret[j] == False):
                    win = 0
                    break
            if(win == 1):
                print("ada horizontal")
                return True
        # cek diagonal ka
        win = 1
        for j in range (1, 21):
            if(j % 4 == 0 and self.players[int(player_id)].tableCoret[j] == False):
                win = 0
                break
        if(win == 1):
            print("ada diagonal ka")
            return True

        # cek diagonal kb
        win = 1
        for j in range (25):
            if(j % 6 == 0 and self.players[int(player_id)].tableCoret[j] == False):
                win = 0
                break
        if(win == 1):
            print("ada diagonal kb")
            return True
        else:
            return False
    
    def cekWinner(self):
        kondisi = False
        for i in range(len(self.players)):
            if(self.isWinner(i)):
                winner = {}
                # newTable = Tabel()
                # newTable.tabel = self.players[i].table
                # newTable.tabelCoret = self.players[i].tableCoret
                # self.players[i].tableCoret
                winner['tabel'] = self.players[i].table
                winner['tabelCoret'] = self.players[i].tableCoret
                winner['id'] = i
                self.winners.append(winner)
                kondisi = True
        return kondisi

    def coret(self, angka, player_id):
        print('giliran: ', self.GILIRAN, 'player_id:', player_id )
        if self.GILIRAN != player_id:
            return

        print('luar coret')
        for i in range(len(self.players)):
            # print(self.players[i])
            index = self.players[i].table.index(angka)
            self.players[i].tableCoret[index] = True
            # print(self.players[i].tableCoret)

        self.GILIRAN = (self.GILIRAN + 1) % self.MAX_PLAYER
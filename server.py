import socket
from _thread import *
import pickle
from game import Game

class Server:
    def __init__(self):
        self.server = 'localhost'
        self.port = 5555
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.bind((self.server, self.port))
        self.socket.listen(2)
        self.idCount = 0
        self.connected = set()
        self.games = {}
        self.MAX_PLAYER = 2

    def threaded_client(self, conn, p, gameId):
        conn.sendall(pickle.dumps(p))
        while True:
            try:
                data = pickle.loads(conn.recv(4096))

                if gameId in self.games:
                    game = self.games[gameId]

                    if not data:
                        break
                    else:
                        if data['type'] == "join":
                            if not game.isReadyToFill():
                                try:
                                    game.addPlayer(p, gameId)
                                    if game.isReadyToFill():
                                        game.startFill()
                                        print(game.STATE)
                                except:
                                    print('server: cannot add player')
                        elif data['type'] == "reset":
                            game.resetWent()
                        elif data['type'] == "isiTable":
                            try:
                                table = data['payload']
                                game.isiTable(p, table)
                                game.players[int(p)].imReady()
                            except:
                                print("server: gagal isi table")
                            if game.isReadyToPlay():
                                game.startPlay()
                                print("server: ready to play")
                        elif data['type'] == "coret":
                            game.coret(data['payload'], p)
                            print('player:', p)
                        try:
                            conn.sendall(pickle.dumps(game))
                        except:
                            print("server: can't send game")
                else:
                    break
            except:
                break

        print("Lost connection")
        try:
            del self.games[gameId]
            print("Closing Game", gameId)
        except:
            pass
        self.idCount -= 1
        conn.close()

    def start(self):
        while True:
            conn, addr = self.socket.accept()
            print("Connected to:", addr)

            self.idCount += 1

            p = 0
            gameId = (self.idCount - 1) // self.MAX_PLAYER
            if self.idCount % self.MAX_PLAYER == 1:
                self.games[gameId] = Game(gameId)
                print("Creating a new game...")

            else:
                self.games[gameId].ready = True
                p = 1

            start_new_thread(self.threaded_client, (conn, p, gameId))




if __name__ == '__main__':
    server = Server()
    server.start()





import socket
from _thread import *
import pickle
from game import Game

def listToStr(s):  
    str1 = " " 
    return (str1.join(s)) 

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

    def threaded_client(self, conn, p, gameId):
        conn.send(str.encode(str(p)))
        while True:
            try:
                data = pickle.loads(conn.recv(4096))

                if gameId in self.games:
                    game = self.games[gameId]

                    if not data:
                        break
                    else:
                        if data['type'] == "join":
                            if not game.isRoomFull():
                                game.addPlayer(p)

                        elif data['type'] == "reset":
                            game.resetWent()
                        elif data['type'] != "get":
                            game.play(p, data)
                        elif data['type'] == "table":
                            try:
                                game.setTable(p, data[1])
                            except:
                                print("game gagal nge set table")

                        conn.sendall(pickle.dumps(game))
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
            gameId = (self.idCount - 1) // 5
            if self.idCount % 5 == 1:
                self.games[gameId] = Game(gameId)
                print("Creating a new game...")
            else:
                self.games[gameId].ready = True
                p = self.idCount % 5

            start_new_thread(self.threaded_client, (conn, p, gameId))
# print("Waiting for a connection, Server Started")

if __name__ == '__main__':
    server = Server()
    server.start()





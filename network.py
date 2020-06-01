import socket
import pickle

class Network:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = "localhost"
        # self.server = "157.245.50.224"
        self.port = 5555
        self.addr = (self.server, self.port)
        try:
            self.id = self.connect()
        except:
            print("network: can't connect to sever")

    def connect(self):
        try:
            self.client.connect(self.addr)
            return pickle.loads(self.client.recv(2048*3))
        except:
            pass

    def send(self, data):
        try:
            self.client.sendall(pickle.dumps(data))
            data = self.client.recv(2048*5)
            if len(data) == 0:
                print("network: PUTUS!!!!!!!!!!!!!!!!!!!!!!!")
                return self.disconnect()
            return pickle.loads(data)
        except socket.error as e:
            print(e)

    def disconnect(self):
        self.client.close()
        return "disconnect"
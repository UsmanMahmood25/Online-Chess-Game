import socket
import pickle
import time

BUFFER_SIZE = 4096 * 8
CONNECTION_TIMEOUT = 5

class Network:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.host = "localhost"
        self.port = 5000
        self.addr = (self.host, self.port)
        self.board = self.connect()
        self.board = pickle.loads(self.board)

    def connect(self):
        self.client.connect(self.addr)
        return self.client.recv(BUFFER_SIZE)

    def disconnect(self):
        self.client.close()

    def send(self, data, pick=False):
        """
        :param data: str
        :return: str
        """
        start_time = time.time()
        while time.time() - start_time < CONNECTION_TIMEOUT:
            try:
                if pick:
                    self.client.send(pickle.dumps(data))
                else:
                    self.client.send(str.encode(data))
                reply = self.client.recv(BUFFER_SIZE)
                try:
                    reply = pickle.loads(reply)
                    break
                except Exception as e:
                    print(e)

            except socket.error as e:
                print(e)


        return reply



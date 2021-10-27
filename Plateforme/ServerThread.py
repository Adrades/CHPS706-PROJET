import threading
import time
from Plateforme.Protocole.UDPServer import UDPServer
from Plateforme.Protocole.UDPSocket import UDPSocket


def action():
    print("Received")


class ServerThread(threading.Thread):
    def __init__(self, ip="127.0.0.1", port=25565):
        threading.Thread.__init__(self)
        self.ip = ip
        self.port = port

    def run(self):
        receiver = UDPServer(self.ip, self.port)
        sender = UDPSocket()
        sender.init_udp_send(self.ip, self.port)
        receiver.wait_message(action)

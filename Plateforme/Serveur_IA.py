import socket
import threading
from Plateforme.Protocole.UDPServer import UDPServer
from Plateforme.Protocole.UDPSocket import UDPSocket

def hello():
    msg = str.encode("Hello Gestionnaire!")


class ServerThread(threading.Thread):
    def __init__(self, ip="127.0.0.1", port=25565):
        threading.Thread.__init__(self)
        self.ip = ip
        self.port = port
        # # Créer une socket datagramme
        # s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        #
        # # Lier à l'adresse IP et le port
        # s.bind(("127.0.0.1", 5555))
        # print("Serveur UDP à l'écoute")

    # Écoutez les datagrammes entrants
    def run(self):
        addr = s.recvfrom(1024)
        message = addr[0]
        address = addr[1]
        clientMsg = "Message du client: {}".format(message)
        clientIP  = "Adresse IP du client: {}".format(address)
        print(clientMsg)
        print(clientIP)
        # Envoi d'une réponse au client
        s.sendto(msg, address)
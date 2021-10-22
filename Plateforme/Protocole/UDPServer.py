import socket


class UDPServer:
    # todo Sûr pour les variables de classe?
    ip = "127.1.0.0"
    port = 25565
    bufferSize = 2048
    this = None

    def __init__(self, ip="127.1.0.0", port=25565, bufferSize=2048):
        self.ip = ip
        self.port = port
        self.bufferSize = bufferSize
        self.this = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
        # todo C'est quoi ce this ?
        # this.bind((ipServer, portServer))
        print("Ouverture d'un serveur local")

    def wait_message(self, action):
        """

        :param action: a function called when a message is received
        :return:
        """
        while True:
            pass
            # todo Passé en commentaire, ça ne marche pas (le this n'existe pas)
            # data, addr = this.recvfrom(self.bufferSize)
            # Data = String
            # action(data, addr)

    def close(self):
        # todo self.udp_socket n'existe pas
        self.udp_socket.close()

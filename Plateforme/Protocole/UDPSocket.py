import socket


class UDPSocket:
    def __init__(self):
        self.udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        "Requires an IP, a port and a String to send"

    def init_udp_send(self, ip="127.1.0.0", port=25565, message="Empty"):
        # Todo revoir la doc, mauvais type de données
        self.udp_socket.sendto(message, (ip, port))
        print("Envoi d'un message à l'ip " + ip + ":" + str(port))

    def wait_message(self, action):
        """
        Grossièrement, créez une fonction que vous enverrez en paramètre comme une lambda mais prenant obligatoirement data et addr (d'autres paramètres sont ok si valeurs par défaut)
        :param action: a function called when a message is received
        :return:
        """
        while True:
            pass
            # todo this n'existe pas, c'est quoi ?
            # data, addr = this.recvfrom(self.bufferSize)
            # action(data, addr)

    def close(self):
        self.udp_socket.close()

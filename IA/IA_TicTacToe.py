#!/usr/bin/env python3

# faire une Ia qui joue au tictactoe

import socket
import random


class IaTictactoe():

    def __init__(self):
        self.__socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.__socket.bind(("127.0.0.1", 8081))

    def launch(self):
        while True:

            socket_jeu = self.__socket.recvfrom(2048)
            
            bytes_to_send = self.random_behavior()
            self.__socket.sendto(str.encode(bytes_to_send), socket_jeu[1])

    def random_behavior(self):
        return str(random.randint(0, 8))

    def end_IA_comm(self):
        self.__socket.close()


if __name__ == "__main__":
    current_IA = IaTictactoe()
    current_IA.launch()

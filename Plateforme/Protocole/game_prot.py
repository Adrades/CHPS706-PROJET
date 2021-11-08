# GAME PROTOCOL

import socket

Input_msg = "Game input"

bytesToSend = str.encode(Input_msg)
print(Input_msg)

serverAddressPort = ("127.0.0.1", 8081)

bufferSize = 1024

# Create a UDP socket at client side

GameSocketInit = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

# Send to server using created UDP socket

GameSocketInit.sendto(bytesToSend, serverAddressPort)

AImsg = GameSocketInit.recvfrom(bufferSize)

msg = "Message from AI : {}".format(AImsg[0].decode('utf-8'))

print(msg)

# Todo c'est un fichier de test? Faire un test unitaire ou le passer dans un main

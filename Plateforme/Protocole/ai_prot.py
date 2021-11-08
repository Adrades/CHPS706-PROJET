# AI PROTOCOL
import socket

localIP = "127.0.0.1"
localPort = 8081

bufferSize = 1024

Connectmsg = "AI has connected to the game sucessfully"

bytesToSend = str.encode(Connectmsg)
# todo remove ? gameAddress = ("127.0.0.1", 8082)

# Create a datagram socket

AISocketInit = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

# Bind to address and ip

AISocketInit.bind((localIP, localPort))

print("AI is ready and listening")

# Listen for incoming datagrams

while True:
    bytesAddressPair = AISocketInit.recvfrom(bufferSize)

    message = bytesAddressPair[0].decode('utf-8')

    address = bytesAddressPair[1]

    clientMsg = "Input of the game : {} \n".format(message)
    clientIP = "Client IP Address:{} \n\n".format(address)

    print(clientMsg)
    print(clientIP)

    # Sending a reply to client

    AISocketInit.sendto(bytesToSend, address)

# Todo c'est un fichier de test? Faire un test unitaire ou le passer dans un main

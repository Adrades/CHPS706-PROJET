#AI PROTOCOL
import socket

localIP     = "127.0.0.1"
localPort   = 8081

bufferSize  = 1024

bytesToSend = str.encode(Connectmsg)

gameAddress = ("127.0.0.1", 8082)
# Create a datagram socket

AISocketInit = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

 

# Bind to address and ip

AISocketInit.bind((localIP, localPort))

print("IA is ready and listening")

 

# Listen for incoming datagrams

while(True):

    bytesAddressPair = AISocketInit.recvfrom(bufferSize)

    message = bytesAddressPair[0].decode('utf-8')

    address = bytesAddressPair[1]

    clientMsg = "Input of the game : {} \n".format(message)
    clientIP  = "Client IP Address:{} \n\n".format(address)
    
    print(clientMsg)
    print(clientIP)

    AISocketInit.sendto("UP", gameAddress)

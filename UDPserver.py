# Jason Walker

from socket import *
serverPort = 13051

serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort))
                            
print "The server is ready to recieve"

while 1:

    message, clientAddress = serverSocket.recvfrom(2048)

    if message == "l":
        input_mes = "l"
        serverSocket.sendto(input_mes, clientAddress)
        message2, clientAddress = serverSocket.recvfrom(2048)
        modifiedMessage = message2.lower()
        serverSocket.sendto(modifiedMessage, clientAddress)

    elif message == "u":
        input_mes = "u"
        serverSocket.sendto(input_mes, clientAddress)
        message2, clientAddress = serverSocket.recvfrom(2048)
        modifiedMessage = message2.upper()
        serverSocket.sendto(modifiedMessage, clientAddress)

    elif message == "r":
        input_mes = "r"
        serverSocket.sendto(input_mes, clientAddress)
        message2, clientAddress = serverSocket.recvfrom(2048)
        modifiedMessage = message2.swapcase()
        serverSocket.sendto(modifiedMessage, clientAddress)
        
    else:
        input_mes = "e"
        serverSocket.sendto(input_mes, clientAddress)
        message2, clientAddress = serverSocket.recvfrom(2048)
        modifiedMessage = message2
        serverSocket.sendto(modifiedMessage, clientAddress)

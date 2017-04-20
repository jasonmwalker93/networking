# Jason Walker

from socket import *
serverName = 'localhost'
serverPort = 13051

clientSocket = socket(AF_INET,SOCK_DGRAM)

message = raw_input("Input 'l' for lowercase, 'u' for uppercase, and 'r' to reverse upper/lower case , or 'q' to quit: ")

while message != 'q':
    clientSocket.sendto(message,(serverName, serverPort))

    input_mes, serverAddress = clientSocket.recvfrom(2048)

    if input_mes == "l":
        message2 = raw_input("Input sentence: ")
        clientSocket.sendto(message2,(serverName, serverPort))
    elif input_mes == "u":
        message2 = raw_input("Input sentence: ")
        clientSocket.sendto(message2,(serverName, serverPort))
    elif input_mes == "r":
        message2 = raw_input("Input sentence: ")
        clientSocket.sendto(message2,(serverName, serverPort))
    else:
        message2 = "Invalid input. Please enter a valid letter indicator."
        clientSocket.sendto(message2,(serverName, serverPort))

    modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
    print modifiedMessage

    message = raw_input("Input 'l' for lowercase, 'u' for uppercase, and 'r' to reverse upper/lower case , or 'q' to quit: ")

raw_input("Press any key to close connection...")
clientSocket.close()

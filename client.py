import socket

serverAddress = "127.0.0.1"
serverPort = 5000

startString = input("write something, it will be then processed with the BWT algorithm\nwrite here: ")

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientSocket.connect((serverAddress, serverPort))

clientSocket.sendall(startString.encode("utf-8"))
clientSocket.shutdown(socket.SHUT_WR)    #tell the server that the string is complete

finalString = b""

while True:
    receivedData = clientSocket.recv(1024)

    if receivedData == b"":
        break

    finalString += receivedData

clientSocket.close()

print("final string: " + finalString.decode("utf-8"))

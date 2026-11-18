import socket

serverAddress = "127.0.0.1"
serverPort = 5000

startString = input("write something, it will be then processed with the BWT algorithm\nwrite here: ")

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as clientSocket:     #creating a socket in wich we will send the string (data)
    clientSocket.connect((serverAddress, serverPort))

    clientSocket.sendall(startString.encode("utf-8"))   #sending the string encoded in utf-8 standard
    clientSocket.shutdown(socket.SHUT_WR)   #tells the server that the string is sent (puts a end flag)

    finalString = b""   #creating a "null" variable in string bytes (the b before "")

    while True:
        receivedData = clientSocket.recv(1024)

        if receivedData == b"":      #null data reception case control
            break

        finalString += receivedData

print("final string: " + finalString.decode("utf-8"))

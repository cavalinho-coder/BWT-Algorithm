import socket

serverAddress = "127.0.0.1"
serverPort = 5000

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSocket.bind((serverAddress, serverPort))
serverSocket.listen(1)

print("waiting for the client...")
connection, clientAddress = serverSocket.accept()

receivedString = b""

while True:
    receivedData = connection.recv(1024)

    if receivedData == b"":
        break

    receivedString += receivedData

startString = receivedString.decode("utf-8")
print(f"your string: {startString}")

if "$" in startString:
    connection.sendall("error: the string cannot contain $".encode("utf-8"))
else:
    startString += "$"    #the algorithm starts adding a dollar at the end of the string

    stringSteps = []
    stringSteps.append(startString)

    while startString[0] != "$":
        firstChar = startString[0]    #save the first char of the startString
        startString = startString[1:]    #remove it from the startString
        startString += firstChar    #add the char we saved at the end of the string
        stringSteps.append(startString)

    for i in range (len(stringSteps)):
        for j in range (len(stringSteps)-1):
            if stringSteps[j] > stringSteps[j+1]:
                stringSteps[j], stringSteps[j+1] = stringSteps[j+1], stringSteps[j]

    finalString = []

    for i in range(len(stringSteps)):
        finalString.append(stringSteps[i][-1])    #taking the last char of each string

    connection.sendall("".join(finalString).encode("utf-8"))

connection.close()
serverSocket.close()

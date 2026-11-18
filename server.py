import socket

serverAddress = "127.0.0.1"
serverPort = 5000

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as serverSocket:
    serverSocket.bind((serverAddress, serverPort))
    serverSocket.listen(1)

    print("waiting for the client...")
    connection, clientAddress = serverSocket.accept()   #establsishing the connection between server and client
    with connection:

        receivedString = b""

        while True:
            receivedData = connection.recv(1024)

            if receivedData == b"":      #null data case control
                break

            receivedString += receivedData

        startString = receivedString.decode("utf-8")    #decoding with the utf-8 standard
        
        print(f"your string: {startString}")

        if "$" in startString:
            connection.sendall("error: the string cannot contain $".encode("utf-8"))    #$ in the string case control
        else:
            startString += "$"    # algorithm starts adding a dollar at the end of the string

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
            
            print(finalString)

            connection.sendall("".join(finalString).encode("utf-8"))    #sending the encoded string back to the client

import socket

hostIP = socket.gethostbyname(socket.gethostname())
print(hostIP)
port = 7420
format = "utf-8"
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

serverSocket.bind((hostIP, port))
serverSocket.listen(5)
print("The server's now listening!")

while True:
    communicationSocket, clientAddress = serverSocket.accept()
    print(f"New connection from {clientAddress}")
    message = communicationSocket.recv(1024).decode(format)
    messageSent = message.upper()
    print("message from client: ", message)

    communicationSocket.send(messageSent.encode(format))
    communicationSocket.close()
    print(f"Connection with client {clientAddress} is closed")
# print(socket.gethostbyname(socket.gethostname()))
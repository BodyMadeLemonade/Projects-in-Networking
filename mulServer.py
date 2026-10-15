import socket
import threading

def handleClient(communicationSocket):
    message = communicationSocket.recv(1024).decode(format)
    format = "utf-8"
    print("message from client: ", message)
    messageSent = message.upper()
    
    communicationSocket.send(messageSent.encode(format))
    communicationSocket.close()
    print(f"Connection with client {clientAddress} is closed")

hostIP = socket.gethostbyname(socket.gethostname())
print(hostIP)
port = 7420
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #Address family (aka Network Protocol): Network Protocol (IPv4), and Socket Kind (aka Transmission Protocol): Stream (TCP aka Transmission Control Protocol)

serverSocket.bind((hostIP, port))
serverSocket.listen(5)
print("The server's now listening!")

while True:
    communicationSocket, clientAddress = serverSocket.accept()
    print(f"New connection from {clientAddress}")
    client_thread = threading.Thread(target=handleClient, args=(communicationSocket,clientAddress))
    client_thread.start()
# print(socket.gethostbyname(socket.gethostname()))
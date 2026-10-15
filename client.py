import socket
#run server script first. Run the file path for this script in your command prompt/powershell
hostIP = "" #enter hostIP (aka your IP in this instance). Server script prints it for convenience when ran.
port = 7420
format = "utf-8"
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

clientSocket.connect((hostIP, port))
message = input("Enter your message")
clientSocket.send(message.encode(format))
messageRecieved = clientSocket.recv(1024).decode(format)
print("From server", messageRecieved)
clientSocket.close()
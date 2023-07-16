import socket
hostname = socket.gethostname()
IP_Addr = socket.gethostbyname(hostname)
print(IP_Addr)

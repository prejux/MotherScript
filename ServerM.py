import os
import socket
ServSock = socket.socket()
ServSock.bind(("localhost",33333))
ServSock.listen(True)
con,addr = ServSock.accept()
print(addr)
while True:
    data = con.recv(1024)
    os.system(data.decode())

con.close()
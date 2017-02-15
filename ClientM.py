#Реализован сырой клиент,с функцией подключения к сокету
#Следущий пункт,выполнение подключения по логину и пассворду
#В идеале связать с SQL (тащить логин и пассворд)
#Реализация мультипоточности,нужно организовать отправку логов выполнения команд
import socket
MotherSocket = socket.socket()
MotherSocket.connect(("localhost",33333))
while True:
    cmdBox = input()
    MotherSocket.send(cmdBox.encode())
con.close()

import threading
import socket

HOST = '127.0.0.1'
PORT = 8080

server = socket.socket()
server.bind((HOST,PORT))

server.listen(0)

clients = []
names = []

def broadcast(msg,author):
    for client in clients:
        client.send('[{}]:  {}'.format(author,msg).encode('utf-8'))

def receive():
    while True:
        client,addr = server.accept()
        username = client.recv(1024).decode('utf-8')
        broadcast('{} Joined'.format(username),'NEW USER')
        clients.append(client)
        names.append(username)
        thread = threading.Thread(target=handle_client,args=[client])
        thread.start()

def handle_client(client):
    while True:
        try:
            msg = client.recv(1024).decode('utf-8')
            broadcast(msg,names[clients.index(client)])
        except:
            end_connection(client)
            break

def end_connection(client):
    client.close()
    broadcast('{} Left'.format(names[clients.index(client)]),'USER LEFT')
    index = clients.index(client)
    clients.pop(index)
    names.pop(index)

receive()

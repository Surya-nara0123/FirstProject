import socket, threading, sys, datetime
s = socket.socket()		
print ("Socket successfully created")
port = 12345
s.bind(('', port))		
print ("socket binded to %s" %(port))
s.listen(5)	
print ("socket is listening")
clientList = []

def clientHandler(c, addr):
    while True:
        try:
            username = c.recv(2048).decode("utf-8")
        except Exception as m:
            username = ''
        if username != '':
            clientList.append((c, username, addr))
            #c.close()
            print("hello, ", username)
            while True:
                #print('hello')
                try:
                    msg = c.recv(2048).decode("utf-8")
                except Exception as m:
                    msg = ''
                if msg != '':
                    print(msg)
                    for socket, us, m  in clientList:
                        socket.send(f"{username}, {datetime.datetime.now()} {msg}".encode("utf-8"))
while True:
    c, addr = s.accept()
    print ('Got connection from', addr )
    c.send('Thank you for connecting'.encode())
    threading.Thread(target=clientHandler, args=(c, addr)).start()

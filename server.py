import socket, threading, sys
s = socket.socket()		
print ("Socket successfully created")
port = 12345
s.bind(('', port))		
print ("socket binded to %s" %(port))
s.listen(5)	
print ("socket is listening")
def clientHandler(c):
    while True:
        username = c.recv(2048).decode("utf-8")
        if username == 'oooo':
            c.close()
            sys.exit()
            #print(username)
while True:
    c, addr = s.accept()
    print ('Got connection from', addr )
    c.send('Thank you for connecting'.encode())
    threading.Thread(target=clientHandler, args=(c, )).start()

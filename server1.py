import socket, threading, sys, datetime
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
            #print("hello, ", username)
            while True:
                try:
                    msg = c.recv(2048).decode("utf-8")
                except Exception as m:
                    msg = ''
                if msg != '':
                    for socket, us, m  in clientList:
                        try:
                            socket.send(f"('{username}', '{datetime.datetime.now()}', '{msg}')".encode("utf-8"))
                        except BrokenPipeError:
                            pass
def function():

    while True:
        c, addr = s.accept()
        #print ('Got connection from', addr )
        #c.send('Thank you for connecting'.encode())
        threading.Thread(target=clientHandler, args=(c, addr)).start()
    
if __name__ == "__main__":
    try:
        s = socket.socket()		
        #print ("Socket successfully created")
        port = 12345
        s.bind(('', port))		
        #print ("socket binded to %s" %(port))
        s.listen(5)	
        #print ("socket is listening")
        function()
    except:
        pass
    
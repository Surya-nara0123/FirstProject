import pygame
import threading
import socket
import sys

pygame.init()
pygame.font.init()

class App:

    def __init__(self,ip='127.0.0.1',port=8080):
        self.ip = ip
        self.port = port
        self.initial_thread_count = threading.active_count()
        self.width = 750
        self.height = 750
        self.display = pygame.display.set_mode((self.width,self.height))
        self.server = socket.socket()
        self.history = []
        self.font = pygame.font.SysFont('comicsans',25)
        self.pos = 0
        self.msg = ''
        self.run = True

    def ask_name(self,win):
        run = True
        name = ''
        font = pygame.font.SysFont('comicsans',50)
        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        return name
                    elif event.key == pygame.K_BACKSPACE:
                        name = name[:len(name) - 1]
                    else:
                        if len(name) < 15:
                            name += event.unicode

            win.fill((0,0,0))
            ask_name = font.render("Enter your name: ",True,(255,255,255))
            win.blit(ask_name,(100,300))
            display_name = font.render(name,True,(255,255,255))
            win.blit(display_name,(100 + ask_name.get_width() + 20,300))
            pygame.display.update()

        pygame.quit()

    def main(self):
        self.username = self.ask_name(self.display)
        self.connect(self.username)
        thread = threading.Thread(target=self.receive_messages,args=[])
        thread.start()
        while self.run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_BACKSPACE:
                        self.msg = self.msg[:len(self.msg) - 1]
                    elif event.key == pygame.K_DELETE:
                        self.clear_history()
                    elif event.key == pygame.K_RETURN:
                        try:
                            self.server.send(self.msg.encode('utf-8'))
                            self.msg = ''
                        except:
                            print('Server crashed...')
                            self.run = False
                    else:
                        if len(self.msg) < 30:
                            self.msg += event.unicode

            self.draw(self.display)

        pygame.quit()
        self.server.close()

    def draw(self,win):
        win.fill((0,0,0))
        text = self.font.render('[You]:  {}'.format(self.msg),True,(255,255,255))
        win.blit(text,(0,self.height - text.get_height()))
        for pos,msg in self.history:
            text = self.font.render(msg,True,(255,255,255))
            win.blit(text,(0,pos))
        pygame.display.update()

    def connect(self,username):
        self.server.connect((self.ip,self.port))
        self.server.send(username.encode('utf-8'))
        self.history.append([self.pos,'You Joined the Chat Room as {}'.format(self.username)])
        self.pos += 30

    def receive_messages(self):
        while self.run:
            msg = self.server.recv(1024).decode('utf-8')
            self.history.append([self.pos + 10,msg])
            self.pos += 40

    def clear_history(self):
        self.history.clear()
        self.pos = 0
            
app = App()
app.main()

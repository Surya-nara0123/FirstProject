import threading
import pygame as pyg, sys
import socket
#s = socket.socket()
#port = 12345
#s.connect(('127.0.0.1', port))


class Application:
    def __init__(self):
        #inittialising stuff
        self.width, self.height = 400, 600
        self.window = pyg.display.set_mode((self.width, self.height))
        pyg.display.set_caption("Chatsapp")
        pyg.font.init()
        self.messages = []
        #variable assigning
        self.run = True
        self.textBoxRect = pyg.Rect(20, self.height-60, self.width-100, 50)
        self.sendBoxRect = pyg.Rect(self.textBoxRect.right+10, self.height-60, 60, 50)
        self.inputText = ''
        self.font = pyg.font.SysFont("Arial Black", 20, False, False)
        self.sendImage = pyg.image.load("SuryaAssets/send-message.png")
        self.sendImage = pyg.transform.scale(self.sendImage, (30, 25))
        self.flag = False

        #server - client connection setting 
        self.s = socket.socket()
        self.port = 12345
        self.s.connect(('127.0.0.1', self.port))
        threading.Thread(target=(self.recieve)).start()

    def recieve(self):
        while True:
            if self.flag:
                try:
                    self.messages.append(self.s.recv(2048).decode("utf-8"))
                except Exception as m:
                    pass
            
                print(self.messages)

    def main(self):

        while self.run:
            self.window.fill((255, 200, 100))
            pyg.draw.rect(self.window, (255, 255, 255), self.textBoxRect, 0, 100)
            pyg.draw.rect(self.window, (100, 255, 100), self.sendBoxRect, 0, 20)
            self.window.blit(self.sendImage, (self.sendBoxRect.x+15, self.sendBoxRect.y+14))
            for event in pyg.event.get():
                if event.type == pyg.QUIT:
                    run = False
                    #self.s.send("oooo".encode("utf-8"))
                    pyg.quit()
                    sys.exit()

                if event.type == pyg.MOUSEBUTTONDOWN:
                    if self.sendBoxRect.collidepoint(pyg.mouse.get_pos()):
                        print("send")
                        try:
                            self.s.send(self.inputText.encode("utf-8"))
                            self.flag = True
                        except BrokenPipeError:
                            pass
                if event.type == pyg.KEYDOWN:
                    if event.key == pyg.K_BACKSPACE:
                        self.inputText = self.inputText[:-1]
                    else:
                        self.inputText += event.unicode
            self.window.blit(self.font.render(self.inputText, False, (0, 0, 0)), (self.textBoxRect.x+20, self.textBoxRect.y+10))
            pyg.display.update()

if __name__ == "__main__":
    chatapp = Application()
    chatapp.main()

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
        pyg.display.set_icon(pyg.image.load("SuryaAssets/download-16.jpg"))
        pyg.font.init()
        
        #variable assigning
        self.EndThread = False
        self.run = True
        self.messages = []
        self.textBoxRect = pyg.Rect(20, self.height-60, self.width-100, 50)
        self.sendBoxRect = pyg.Rect(self.textBoxRect.right+10, self.height-60, 60, 50)
        self.inputText = ''
        self.font = pyg.font.SysFont("Arial Black", 20, False, False)
        self.sendImage = pyg.image.load("SuryaAssets/send-message.png")
        self.sendImage = pyg.transform.scale(self.sendImage, (30, 25))
        self.flag = False
        self.username = ''
        self.enterUserName = True
        self.rectList = []
        for i in range(50):
            self.rectList.append(pyg.Rect(0, self.height/15*i, self.width, 30))
#
        #self.rectList1 = []
        #for i in range(50):
        #    self.rectList.append(pyg.Rect(0, self.height/15*i, self.width, 30))

        #server - client connection setting 
        self.s = socket.socket()
        self.port = 12345
        self.s.connect(('127.0.0.1', self.port))
        threading.Thread(target=(self.recieve)).start()

    def recieve(self):
        while True:
            if self.EndThread:
                self.s.close()
                sys.exit()
            if not self.enterUserName:
                try:
                    self.messages.append(eval(self.s.recv(2048).decode("utf-8")))
                except Exception as m:
                    pass
            
                print(self.messages)

    def placesMessages(self):
        for i, data in enumerate(self.messages):
            #print(data)
            username = data[0]
            time = data[1]
            msg = data[2]
            
            
            
            if username == self.username:
                text = self.font.render(msg, False, (255,255,255))
                font2 = pyg.font.SysFont("arial black", 10, True)
                time = font2.render(time, True, (255, 255,255))
                rect = text.get_rect()
                rect2 = time.get_rect()
                rect2.topleft = (self.width - rect2.width, self.rectList[i].y+35)
                rect.topleft = (self.width - rect.width, self.rectList[i].y+10)
                pyg.draw.rect(self.window, (18,146,120), rect, 0, 5)
                self.window.blit(text, rect)
                self.window.blit(time, rect2)
            else:
                text = self.font.render(msg, False, (255,255,255))
                rect = text.get_rect()
                font2 = pyg.font.SysFont("arial black", 10, True)
                time = font2.render(time, True, (255, 255,255))
                rect.topleft = (0, self.rectList[i].y+10)
                rect2 = time.get_rect()
                rect2.topleft = (0, self.rectList[i].y+35)
                pyg.draw.rect(self.window, (50,50, 50), rect , 0, 5)
                self.window.blit(text, rect)
                self.window.blit(time, rect2)


    def main(self):
        while self.run:
            self.window.fill((255, 200, 100))
            self.placesMessages()
            pyg.draw.rect(self.window, (255, 255, 255), self.textBoxRect, 0, 100)
            pyg.draw.rect(self.window, (100, 255, 100), self.sendBoxRect, 0, 20)
            self.window.blit(self.sendImage, (self.sendBoxRect.x+15, self.sendBoxRect.y+14))
            for event in pyg.event.get():
                if event.type == pyg.QUIT:
                    self.run = False
                    self.EndThread = True
                    #self.s.send("oooo".encode("utf-8"))
                    
                if event.type == pyg.MOUSEBUTTONDOWN:
                    if self.sendBoxRect.collidepoint(pyg.mouse.get_pos()):
                        print("send")
                        try:
                            self.s.send(self.inputText.encode("utf-8"))
                            if self.enterUserName:
                                self.username = self.inputText
                                self.enterUserName = False
                            #if self.flag:
                            #    self.username = self.inputText
                            #self.flag = True
                            self.inputText = ''
                        except BrokenPipeError:
                            pass
                if event.type == pyg.KEYDOWN:
                    if event.key == pyg.K_BACKSPACE:
                        self.inputText = self.inputText[:-1]
                    elif event.key == pyg.K_RETURN:
                        print("send")
                        try:
                            self.s.send(self.inputText.encode("utf-8"))
                            if self.enterUserName:
                                self.username = self.inputText
                                self.enterUserName = False
                            #if self.flag:
                            #    self.username = self.inputText
                            #self.flag = True
                            self.inputText = ''
                        except BrokenPipeError:
                            pass
                    else:
                        self.inputText += event.unicode
            
            self.window.blit(self.font.render(self.inputText, False, (0, 0, 0)), (self.textBoxRect.x+20, self.textBoxRect.y+10))
            pyg.display.update()
def run():
    chatapp = Application()
    chatapp.main()

if __name__ == "__main__":
    run()
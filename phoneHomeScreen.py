import pygame as pyg, sys, cv2, random, os, handDetector, time, threading
import pywhatkit, pyjokes, pyttsx3 as pyt
import speech_recognition as sr, chatApp, server1

class homeScreen:
    def __init__(self):
        self.width, self.height = 400, 600
        self.window = pyg.display.set_mode((self.width, self.height))
        self.webcam = cv2.VideoCapture(0)
        self.hand = handDetector.handDetector(maxhands=1)
        self.run = True
        self.image = pyg.image.load(f"/Users/surya/Desktop/SuryaFolder/SuryaAssets/nature/Image_10.jpg")
        self.googleWidget = pyg.image.load("SuryaAssets/googleWidget.png")
        self.googleWidget = pyg.transform.smoothscale(self.googleWidget, (self.width-50, self.height*(self.width/self.googleWidget.get_width())))
        self.image = pyg.transform.smoothscale(self.image, (self.width, self.height))
        self.chatsappIcon = pyg.image.load("SuryaAssets/download-16.jpg")
        self.chatsappIcon = pyg.transform.smoothscale(self.chatsappIcon, (40, 40))
        self.pTime = 0
        self.microphoneRect = pyg.Rect(320, 52, 25, 20)
        self.x = y = 0
        self.select = False
        self.googleAssistant = False
        self.c = ''
        self.a1 = False
        self.run1 = False
        self.engine = pyt.Engine()
        self.a = False
        self.listener = sr.Recognizer()
        self.run1 = False
        self.command = ''
        self.newserver = False
        self.d = threading.Thread(target=self.mainScreen,).start()
        self.b = threading.Thread(target=self.function,).start()
        self.g =  threading.Thread(target=(server1.function(),)).start()
        

    def function(self):
        if threading.active_count() != 1:
            while self.run:
                try:
                    with sr.Microphone(len(sr.Microphone.list_microphone_names())-1) as source:
                        self.listener.adjust_for_ambient_noise(source)
                        print("Listening....")
                        audio = self.listener.listen(source, None, 2)
                        self.command = self.listener.recognize_google(audio).lower()
                        if self.command.lower() == 'ok google' or self.command.lower() == 'hey google' or self.command.lower() == 'google':
                            self.a = True
                        if self.a:
                            if 'bye' in self.command or 'goodbye' in self.command or 'kill yourself' in self.command:
                                a = False
                            if 'tell' in self.command and 'joke' in self.command and "don't" not in self.command and 'do  not' not in self.command:
                
                                self.engine.say(self.command)
                                self.engine.endLoop()
                                #engine.endLoop()
                            if 'play' in self.command or 'youtube' in self.command:
                                self.command = self.command.replace('play', '')
                                self.command = self.command.replace('youtube', '')
                                if self.command.strip() != '':
                                    pywhatkit.playonyt(self.command)
                                else:
                                    pywhatkit.playonyt('never gonna give you up')
                            if 'open' in self.command or 'run' in self.command:
                                self.command = self.command.replace('open', '')
                                self.command = self.command.replace('run', '')
                                if 'whatsapp' in self.command or "chatsappp" in self.command:
                                    if 'in a new group' in self.command:
                                        self.newserver = True
                                    else:
                                        self.newserver = False
                                    self.run1 = True
                                    #threading.Thread(target = (chatApp.run(), )).start
                                    #threading.Condition.wait()

                except Exception as s:
                    print(s)
    def mainScreen(self):        
        
        #self.g.join()
        while self.run:
            #global a,command
            _, frame = self.webcam.read()
            frame = cv2.flip(frame, 1)
            self.window.blit(self.image, (0, 0))
            self.hand.findHands(frame)
            lmList = self.hand.findPosition(frame)
            fingerup = self.hand.fingersUp()
            self.window.blit(self.googleWidget, (20,0))
            if lmList:
                if fingerup == [0, 1, 0, 0, 0]:
                    x = lmList[8][1]/self.webcam.get(3)
                    y = lmList[8][2]/self.webcam.get(4)
                    self.select = False
                    pyg.draw.circle(self.window, (0, 0, 0), ((self.width+100)*x, (self.height+100)*y), 5)
                elif fingerup == [0, 1, 1, 0, 0]:
                    x = lmList[8][1]/self.webcam.get(3)
                    y = lmList[8][2]/self.webcam.get(4)
                    self.select = True
                    pyg.draw.circle(self.window, (255, 255, 255), ((self.width+100)*x, (self.height+100)*y), 8)
            self.cTime = time.time()
            self.fps = 1 / (self.cTime-self.pTime)
            self.pTime = self.cTime
            
            for event in pyg.event.get():
                if event.type == pyg.QUIT:
                    self.run = False
                    pyg.quit()
                    sys.exit()

            if self.select:
                if self.microphoneRect.collidepoint((self.width+100)*x, (self.height+100)*y):
                    a1 = True
                    a = True
                    self.select = False
            
            self.window.blit(self.chatsappIcon, (100, self.height//2))
            self.a1 = self.a
            if self.run1:
                print("hello")
                chatApp.run()
                    
            
            
            if self.a or self.a1:
                pyg.draw.rect(self.window, (255, 255, 255), (0, self.height/2, self.width, self.height/2), 0, 5)
                google_logo = pyg.image.load('SuryaAssets/Google_Assistant_logo.png')
                google_logo = pyg.transform.scale(google_logo, (100, 100))
                google_logo_rect = google_logo.get_rect()
                google_logo_rect.center = (self.width/2, self.height*3/4)
                self.window.blit(google_logo, google_logo_rect)
                
            buttons = pyg.Surface((self.image.get_width(), 50))
            buttons.set_alpha(100)
            buttons.fill((255, 255, 255))
            self.window.blit(buttons, (0, self.image.get_height()-50))
            pyg.display.update()
            
            #cv2.imshow("window", frame)
            

def main():
    phone = homeScreen()
    #phone.mainScreen()

if __name__ == "__main__":
    main()
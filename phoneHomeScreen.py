import pygame as pyg, sys, cv2, handDetector, time, threading
import pywhatkit, pyjokes, pyttsx3 as pyt
import speech_recognition as sr, chatApp, Final, Beatmaker, datetime, subprocess, main1

class homeScreen:
    def __init__(self):
        self.width, self.height = 400, 600
        self.window = pyg.display.set_mode((self.width, self.height))
        self.webcam = cv2.VideoCapture(0)
        self.hand = handDetector.handDetector(maxhands=1)
        self.run = True
        self.background = pyg.image.load(f"/Users/surya/Desktop/SuryaFolder/SuryaAssets/nature/Image_10.jpg")
        self.googleWidget = pyg.image.load("SuryaAssets/googleWidget.png")
        self.googleWidget = pyg.transform.smoothscale(self.googleWidget, (self.width-50, self.height*(self.width/self.googleWidget.get_width())))
        self.background = pyg.transform.smoothscale(self.background, (self.width, self.height))
        self.chatsappIcon = pyg.image.load("SuryaAssets/download-16.jpg")
        self.chatsappIcon = pyg.transform.smoothscale(self.chatsappIcon, (40, 40))
        self.calculatorIcon = pyg.image.load("HariniAssets/download.png")
        self.calculatorIcon = pyg.transform.scale(self.calculatorIcon, (40, 40))
        self.beatmakerIcon = pyg.image.load("SuryaAssets/DrumsLogo.png")
        self.beatmakerIcon = pyg.transform.scale(self.beatmakerIcon, (40, 40))
        self.GameCentreIcon = pyg.image.load("SuryaAssets/My Project.png")
        self.GameCentreIcon = pyg.transform.scale(self.GameCentreIcon, (40, 40))
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
        self.GoogleListener = True
        self.AppRects = [pyg.Rect(50, self.height//2, 40, 40),
                         pyg.Rect(100, self.height//2, 40, 40),
                         pyg.Rect(150, self.height//2, 40, 40),
                         pyg.Rect(200, self.height//2, 40, 40)]
        
        #self.g =  threading.Thread(target=(server1.function(),)).start()
        

    def function(self):
        while self.run:
            if self.GoogleListener:
                try:
                    with sr.Microphone(len(sr.Microphone.list_microphone_names())-1) as source:
                        self.listener.adjust_for_ambient_noise(source)
                        print("Listening....")
                        audio = self.listener.listen(source, None, 2)
                        self.command = self.listener.recognize_google(audio).lower()
                        if self.command.lower() == 'ok google' or self.command.lower() == 'hey google' or self.command.lower() == 'google':
                            self.a = True
                        if self.a:
                            if 'switch off the phone' in self.command or "switch off" in self.command:
                                self.GoogleListener = False
                                self.run = False
                                pyg.quit()
                                sys.exit()
                            if 'bye' in self.command or 'goodbye' in self.command or 'kill yourself' in self.command:
                                self.a = False
                            if 'tell' in self.command and 'joke' in self.command and "don't" not in self.command and 'do  not' not in self.command:
                                subprocess.call(['python3.10', 'talk.py', pyjokes.get_joke(language='en', category='neutral')])
                                #engine.endLoop()
                            if 'play' in self.command or 'youtube' in self.command:
                                self.command = self.command.replace('play', '')
                                self.command = self.command.replace('youtube', '')
                                if self.command.strip() != '':
                                    pywhatkit.playonyt(self.command)
                                else:
                                    pywhatkit.playonyt('never gonna give you up')
                            if "time" in self.command:
                                datetime.datetime.now().strftime('%I:%M %p')
                                #print("who is")
                                #pywhatkit.sendwhatmsg_instantly('+91 86103 35141', "Hey All! This is message sent not by Surya but is sent by python")
                            if 'open' in self.command or 'run' in self.command:
                                self.command = self.command.replace('open', '')
                                self.command = self.command.replace('run', '')
                                if 'whatsapp' in self.command or "chatsappp" in self.command:
                                    self.run1 = "chatApp"
                                if 'calculator' in self.command:
                                    self.run1 = "calculator"
                                if 'beat maker' in self.command:
                                    self.run1 = "beatmaker"
                                if 'game center' in self.command:
                                    self.run1 = "game center"

                except Exception as s:
                    print(s)
    def mainScreen(self):
        self.b = threading.Thread(target=self.function,).start()
        #self.c = threading.Thread(target=subprocess.call(["python", "server1.py"]),).start()
        
        while self.run:
            #global a,command
            _, frame = self.webcam.read()
            frame = cv2.flip(frame, 1)
            self.window.blit(self.background, (0, 0))
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
                    self.a1 = True
                    self.a = True
                    self.select = False
                elif self.AppRects[0].collidepoint((self.width+100)*x, (self.height+100)*y):
                    print("hello")
                    self.GoogleListener = False
                    chatApp.run()
                    self.run1 = False
                    self.GoogleListener = True
                    x = y = 0
                elif self.AppRects[1].collidepoint((self.width+100)*x, (self.height+100)*y):
                    print("hello")
                    self.GoogleListener = False
                    Final.main()
                    self.window = pyg.display.set_mode((self.width, self.height))
                    self.run1 = False
                    self.GoogleListener = True
                    x = y = 0
                elif self.AppRects[2].collidepoint((self.width+100)*x, (self.height+100)*y):
                    print("hello")
                    self.GoogleListener = False
                    Beatmaker.BeatSequencer()
                    self.window = pyg.display.set_mode((self.width, self.height))
                    self.run1 = False
                    self.GoogleListener = True
                    x = y = 0
                elif self.AppRects[3].collidepoint((self.width+100)*x, (self.height+100)*y):
                    print("hello")
                    self.GoogleListener = False
                    main1.mainMenu()
                    self.window = pyg.display.set_mode((self.width, self.height))
                    self.run1 = False
                    self.GoogleListener = True
                    x = y = 0


            self.window.blit(self.chatsappIcon, self.AppRects[0])
            self.window.blit(self.calculatorIcon, self.AppRects[1])
            pyg.draw.rect(self.window, (255, 255, 255), self.AppRects[2])
            self.window.blit(self.beatmakerIcon, self.AppRects[2])
            self.window.blit(self.GameCentreIcon, self.AppRects[3])
        
            self.a1 = self.a
            if self.run1 == "chatApp":
                print("hello")
                self.GoogleListener = False
                chatApp.run()
                self.run1 = False
                self.GoogleListener = True

            if self.run1 == "calculator":
                print("hello")
                self.GoogleListener = False
                Final.main()
                self.window = pyg.display.set_mode((self.width, self.height))
                self.run1 = False
                self.GoogleListener = True

            if self.run1 == "beatmaker":
                print("hello")
                self.GoogleListener = False
                Beatmaker.BeatSequencer()
                self.window = pyg.display.set_mode((self.width, self.height))
                self.run1 = False
                self.GoogleListener = True
            
            if self.run1 == "game centre":
                print("hello")
                self.GoogleListener = False
                main1.mainMenu()
                self.window = pyg.display.set_mode((self.width, self.height))
                self.run1 = False
                self.GoogleListener = True
            
            
            
            if self.a or self.a1:
                pyg.draw.rect(self.window, (255, 255, 255), (0, self.height/2, self.width, self.height/2), 0, 5)
                google_logo = pyg.image.load('SuryaAssets/Google_Assistant_logo.png')
                google_logo = pyg.transform.scale(google_logo, (100, 100))
                google_logo_rect = google_logo.get_rect()
                google_logo_rect.center = (self.width/2, self.height*3/4)
                self.window.blit(google_logo, google_logo_rect)
                
            buttons = pyg.Surface((self.background.get_width(), 50))
            buttons.set_alpha(100)
            buttons.fill((255, 255, 255))
            self.window.blit(buttons, (0, self.background.get_height()-50))
            pyg.display.update()
            
            #cv2.imshow("window", frame)
            

def main():
    phone = homeScreen()
    phone.mainScreen()

if __name__ == "__main__":
    main()
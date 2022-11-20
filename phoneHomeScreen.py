import pygame as pyg, sys, cv2, random, os, handDetector, time, threading
import pywhatkit, pyjokes, pyttsx3 as pyt
import speech_recognition as sr, chatApp

class homeScreen:
    def mainScreen(self):
        width, height = 400, 600
        window = pyg.display.set_mode((width, height))
        webcam = cv2.VideoCapture(0)
        hand = handDetector.handDetector(maxhands=1)
        
        run = True
        image = pyg.image.load(f"/Users/surya/Desktop/SuryaFolder/SuryaAssets/nature/Image_10.jpg")
        googleWidget = pyg.image.load("SuryaAssets/googleWidget.png")
        googleWidget = pyg.transform.smoothscale(googleWidget, (width-50, height*(width/googleWidget.get_width())))
        image = pyg.transform.smoothscale(image, (width, height))
        chatsappIcon = pyg.image.load("SuryaAssets/download-16.jpg")
        chatsappIcon = pyg.transform.smoothscale(chatsappIcon, (40, 40))

        pTime = 0
        microphoneRect = pyg.Rect(320, 52, 25, 20)
        x = y = 0
        select = False
        googleAssistant = False
        c = ''
        a1 = False
        run1 = False
        engine = pyt.Engine()
        def function():
            if threading.active_count() != 1:
                global a
                a = False
                while run:
                    global command
                    listener = sr.Recognizer()
                    try:
                        global run1
                        with sr.Microphone(len(sr.Microphone.list_microphone_names())-1) as source:
                            listener.adjust_for_ambient_noise(source)
                            print("Listening....")
                            audio = listener.listen(source, None, 2)
                            command = listener.recognize_google(audio).lower()
                            if command.lower() == 'ok google' or command.lower() == 'hey google' or command.lower() == 'google':
                                a = True
                            if a:
                                if 'bye' in command or 'goodbye' in command or 'kill yourself' in command:
                                    a = False
                                if 'tell' in command and 'joke' in command and "don't" not in command and 'do  not' not in command:
                    
                                    engine.say(command)
                                    engine.endLoop()
                                    #engine.endLoop()
                                if 'play' in command or 'youtube' in command:
                                    command = command.replace('play', '')
                                    command = command.replace('youtube', '')
                                    if command.strip() != '':
                                        pywhatkit.playonyt(command)
                                    else:
                                        pywhatkit.playonyt('never gonna give you up')
                                if 'open' in command or 'run' in command:
                                    command = command.replace('open', '')
                                    command = command.replace('run', '')
                                    if 'whatsapp' in command or "chatsappp" in command:
                                        run1 = True
                                        chatApp.run()
                                        #threading.Condition.wait()

                    except Exception as s:
                        print(s)
        b = threading.Thread(target=function,).start()
        while run:
            global a,command
            _, frame = webcam.read()
            frame = cv2.flip(frame, 1)
            window.blit(image, (0, 0))
            hand.findHands(frame)
            lmList = hand.findPosition(frame)
            fingerup = hand.fingersUp()
            window.blit(googleWidget, (20,0))
            if lmList:
                if fingerup == [0, 1, 0, 0, 0]:
                    x = lmList[8][1]/webcam.get(3)
                    y = lmList[8][2]/webcam.get(4)
                    select = False
                    pyg.draw.circle(window, (0, 0, 0), ((width+100)*x, (height+100)*y), 5)
                elif fingerup == [0, 1, 1, 0, 0]:
                    x = lmList[8][1]/webcam.get(3)
                    y = lmList[8][2]/webcam.get(4)
                    select = True
                    pyg.draw.circle(window, (255, 255, 255), ((width+100)*x, (height+100)*y), 8)
            cTime = time.time()
            fps = 1 / (cTime-pTime)
            pTime = cTime
            
            for event in pyg.event.get():
                if event.type == pyg.QUIT:
                    run = False
                    pyg.quit()
                    sys.exit()

            if select:
                if microphoneRect.collidepoint((width+100)*x, (height+100)*y):
                    a1 = True
                    a = True
                    select = False
            
            
            a1 = a
            if run1:
                print("hello")
                chatApp.run()
            
            
            
            if a or a1:
                pyg.draw.rect(window, (255, 255, 255), (0, height/2, width, height/2), 0, 5)
                google_logo = pyg.image.load('SuryaAssets/Google_Assistant_logo.png')
                google_logo = pyg.transform.scale(google_logo, (100, 100))
                google_logo_rect = google_logo.get_rect()
                google_logo_rect.center = (width/2, height*3/4)
                window.blit(google_logo, google_logo_rect)
                
            buttons = pyg.Surface((image.get_width(), 50))
            buttons.set_alpha(100)
            buttons.fill((255, 255, 255))
            window.blit(buttons, (0, image.get_height()-50))
            window.blit(chatsappIcon, (100, height//2))
            pyg.display.update()
            
            #cv2.imshow("window", frame)
            

def main():
    phone = homeScreen()
    phone.mainScreen()

if __name__ == "__main__":
    main()
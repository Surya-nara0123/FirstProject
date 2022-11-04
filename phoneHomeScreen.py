
from logging import exception
import pygame as pyg, sys, cv2, random, os, handDetector, time

import speech_recognition as sr

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
        pTime = 0
        microphoneRect = pyg.Rect(320, 52, 25, 20)
        x = y = 0
        select = False
        googleAssistant = False
        while run:
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
            buttons = pyg.Surface((image.get_width(), 50))
            buttons.set_alpha(100)
            buttons.fill((255, 255, 255))
            window.blit(buttons, (0, image.get_height()-50))
            for event in pyg.event.get():
                if event.type == pyg.QUIT:
                    run = False
                    pyg.quit()
                    sys.exit()

            if select:
                if microphoneRect.collidepoint((width+100)*x, (height+100)*y):
                    googleAssistant = True
                    select = False
            
            if googleAssistant:
                listener = sr.Recognizer()
                #print(sr.Microphone.list_microphone_names())
                try:
                    with sr.Microphone(0) as source:
                        
                        voice = listener.listen(source, None, 5)
                        command = listener.recognize_google(voice)
                        print(command)
                except Exception as m:
                    print(m)
            pyg.display.update()
            #cv2.imshow("window", frame)
            

phone = homeScreen()
phone.mainScreen()
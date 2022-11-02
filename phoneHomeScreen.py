import pygame as pyg, sys, cv2, random, os, handDetector, time

class homeScreen:
    def mainScreen(self):
        width, height = 600, 900
        window = pyg.display.set_mode((width, height))
        webcam = cv2.VideoCapture(0)
        hand = handDetector.handDetector(maxhands=1)
        images = []
        for i in os.listdir("/Users/surya/Desktop/SuryaFolder/SuryaAssets/nature"):
            images.append(pyg.image.load(f"/Users/surya/Desktop/SuryaFolder/SuryaAssets/nature/{i}"))
        run = True
        image = images[3]
        #image = random.choice(images)
        image = pyg.transform.smoothscale(image, (width, height))
        #image = pyg.transform.chop(image, (0, image.get_height()-100, image.get_width(), 100))
        pTime = 0
        while run:
            rect, frame = webcam.read()
            
            window.blit(image, (0, 0))
            hand.findHands(frame)
            lmList = hand.findPosition(frame)
            fingerup = hand.fingersUp()
            #print(lmList)
            if lmList:
                if fingerup == [0, 1, 0, 0, 0]:
                    x = lmList[8][1]/webcam.get(3)
                    y = lmList[8][2]/webcam.get(4)

                    pyg.draw.circle(window, (255, 255, 255), (width*x, height*y), 5)
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
            pyg.display.update()
            

phone = homeScreen()
phone.mainScreen()
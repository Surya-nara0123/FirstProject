import pygame as pyg, sys, cv2, random

class homeScreen:
    def mainScreen(self):
        width, height = 400, 700
        window = pyg.display.set_mode((width, height))
        images = []
        for i in range(10):
            images.append(pyg.image.load(f"/Users/surya/Desktop/SuryaFolder/SuryaAssets/nature/Image_{i+1}.jpg"))
        run = True
        image = random.choice(images)
        image = pyg.transform.smoothscale(image, (image.width, height))
        while run:
            window.blit(image, (0, 0))
            for event in pyg.event.get():
                if event.type == pyg.QUIT:
                    run = False
                    pyg.quit()
                    sys.exit()
            pyg.display.update()

phone = homeScreen()
phone.mainScreen()
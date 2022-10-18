import enum
import random


class BeatSequencer:
    def beatmakerNode(self):
        import pygame as pyg
        import sys
        icon = pyg.image.load("SuryaAssets/DrumsLogo.png")
        pyg.display.set_icon(icon)
        pyg.init()
        window = pyg.display.set_mode((800, 600))
        run = True
        rectList = [
            [],
            [],
            [],
            [],
            [],
            []
        ]
        for j, list in enumerate(rectList):
            for i in range(10):
                list.append(pyg.Rect((window.get_width()-100)/6*(i+1)-15, (window.get_height()/6)*j,(window.get_width()-100)/6, (window.get_height()/6)))
        while run:
            window.fill((0,0,0))
            pyg.draw.rect(window, (80, 80, 80), (0, 0, 100, window.get_height()))
            for i in rectList:
                for j in i:
                    pyg.draw.rect(window, (80, 80, 80), j, 4)
            for event in pyg.event.get():
                if event.type == pyg.QUIT:
                    run = False

            pyg.display.update()
    def menu(self):
        import pygame as pyg
        import sys

        pyg.init()
        window = pyg.display.set_mode((800, 600))
        background = pyg.image.load("SuryaAssets/BeatSequencerMenu.png")
        background = pyg.transform.scale(background, (800, 600))
        icon = pyg.image.load("SuryaAssets/DrumsLogo.png")
        pyg.display.set_icon(icon)
        rectList = [
            pyg.Rect(62, 254, 236, 93),
            pyg.Rect(63, 368, 235, 91),
            pyg.Rect(63, 482, 235, 91)
        ]
        run = True
        while run:
            window.fill((255,255,255))
            window.blit(background, (0, 0))
            #mixer.music.play()
            for event in pyg.event.get():
                if event.type == pyg.QUIT:
                    run = False
                    pyg.quit()
                    pyg.display.quit()
                    sys.exit()
            pyg.display.update()


newwindow = BeatSequencer()
newwindow.beatmakerNode()
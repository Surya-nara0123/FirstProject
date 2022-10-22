import random
import pygame as pyg
import sys
import mysql.connector
mydb = mysql.connector.connect(host="localhost", password="S********123")


class BeatSequencer:
    def __init__(self):
        cursor = mydb.cursor()
        cursor.execute("use BeatMakerSettings")
        cursor.execute("select * from options")
        self.options = cursor.fetchall()
    def database(self):
        cursor = mydb.cursor()
        cursor.execute("show databases")
        for x in cursor:
            print(x)
        cursor.execute("use BeatMakerSettings")
        cursor.execute("select * from options")
        for x in cursor:
            print(x)

    def beatmakerNode(self):
        icon = pyg.image.load("SuryaAssets/DrumsLogo.png")
        pyg.display.set_icon(icon)
        pyg.init()
        window = pyg.display.set_mode((800, 600))
        run = True
        flagList = [
            [False, False, False, False, False, False],
            [False, False, False, False, False, False],
            [False, False, False, False, False, False],
            [False, False, False, False, False, False],
            [False, False, False, False, False, False],
            [False, False, False, False, False, False]
        ]
        rectList = [
            [],
            [],
            [],
            [],
            [],
            []
        ]
        for j, list in enumerate(rectList):
            for i in range(6):
                list.append(pyg.Rect((window.get_width()-100)/6*(i+1)-10, (window.get_height()/6)*j+5,(window.get_width()-100)/6-5, (window.get_height()/6)-5))
        while run:
            window.fill((0,0,0))
            pyg.draw.rect(window, (80, 80, 80), (0, 0, 100, window.get_height()))
            for i in rectList:
                for j in i:
                    if flagList[rectList.index(i)][i.index(j)] == False:
                        pyg.draw.rect(window, (80, 80, 80), j, 0, 10)
                    else:
                        pyg.draw.rect(window, (80, 180, 80), j, 0, 10)
            for event in pyg.event.get():
                if event.type == pyg.QUIT:
                    run = False
                if event.type == pyg.MOUSEBUTTONDOWN:
                    for i in rectList:
                        for j in i:
                            if j.collidepoint(pyg.mouse.get_pos()):
                                if flagList[rectList.index(i)][i.index(j)] == False:
                                    flagList[rectList.index(i)][i.index(j)] = True
                                else:
                                    flagList[rectList.index(i)][i.index(j)] = False

            pyg.display.update()
    def menu(self):
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
                elif event.type == pyg.MOUSEBUTTONDOWN:
                    if rectList[0].collidepoint(pyg.mouse.get_pos()):
                        self.beatmakerNode()
                    elif rectList[1].collidepoint(pyg.mouse.get_pos()):
                        run1 = True
                        while run1:
                            pyg.draw.rect(window, (0, 0, 0, 50), (0, 0, window.get_width(), window.get_height()))
                            keys = pyg.key.get_pressed()
                            if keys[pyg.K_ESCAPE]:
                                run1 = False
                            pyg.display.update()
            pyg.display.update()


newwindow = BeatSequencer()
newwindow.menu()
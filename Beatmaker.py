import random
import pygame as pyg
import sys
import mysql.connector
mydb = mysql.connector.connect(host="localhost", password="S********123")


class BeatSequencer:
    def __init__(self):
        self.cursor = mydb.cursor()
        self.cursor.execute("use BeatMakerSettings")
        self.cursor.execute("select * from options")
        self.options = self.cursor.fetchall()
    def database(self):
        cursor = mydb.cursor()
        pyg.init()
        cursor.execute("show databases")
        for x in cursor:
            print(x)
        cursor.execute("use BeatMakerSettings")
        cursor.execute("select * from options")
        for x in cursor:
            print(x)
        font = pyg.font.SysFont("Arial Black", 50, True, False)

        print(font)

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
        run1 = False
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
                        if run1 == False:
                            self.beatmakerNode()
                    elif rectList[1].collidepoint(pyg.mouse.get_pos()):
                        if run1 == False:
                            run1 = True
                    elif rectList[2].collidepoint(pyg.mouse.get_pos()):
                        if run1 == False:
                            run = False
            if run1 == True:
                s = pyg.Surface(window.get_size())
                s.set_alpha(200)
                s.fill((0, 0, 0))
                window.blit(s, (0, 0))
                key = pyg.key.get_pressed()
                if key[pyg.K_ESCAPE]:
                    run1= False
                font = pyg.font.SysFont("Arial Black", 20, True, False)
                rectList1 = []
                for i in range(len(self.options)):
                    rectList1.append(pyg.Rect(4*window.get_width()/6, (i+2)*(window.get_height()/6), 100, 50 ))
                heading = font.render("Controls and Settings", False, (255, 255, 255))
                window.blit(heading,(window.get_width()/3, window.get_height()/6))
                heading = font.render("Back----->Escape", False, (255, 255, 255))
                window.blit(heading,(0, 0))
                for i, (name, setting) in enumerate(self.options):
                    heading = font.render(name, False, (255, 255, 255))
                    window.blit(heading,(window.get_width()/6, (i+2)*(window.get_height()/6)))
                    heading = font.render(setting, False, (255, 255, 255))
                    window.blit(heading,rectList1[i])
                for event in pyg.event.get():
                    if event.type == pyg.MOUSEBUTTONDOWN:
                        for i, rect in enumerate(rectList1):
                            if rect.collidepoint(pyg.mouse.get_pos()):
                                self.cursor.execute(f"update options set setting  = '' where optionName = '{self.options[i][0]}';")
                                self.cursor.execute("select * from options")
                                self.options = self.cursor.fetchall()
                                flag = i+1

                    
            pyg.display.update()


newwindow = BeatSequencer()
newwindow.menu()
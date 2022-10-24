import random
from typing import Text
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
        run1 = False
        flag = False
        user_text = ''
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
                    if run1 == False:
                        for i in rectList:
                            for j in i:
                                if j.collidepoint(pyg.mouse.get_pos()):
                                    if flagList[rectList.index(i)][i.index(j)] == False:
                                        flagList[rectList.index(i)][i.index(j)] = True
                                    else:
                                        flagList[rectList.index(i)][i.index(j)] = False
                    
                    elif run1:
                        for i, rect in enumerate(rectList1):
                            if rect.collidepoint(pyg.mouse.get_pos()):
                                self.cursor.execute(f"update options set setting  = '' where optionName = '{self.options[i][0]}';")
                                self.cursor.execute("select * from options")
                                self.options = self.cursor.fetchall()
                                flag = i+1
                elif event.type == pyg.KEYDOWN:
                    text = eval('pyg.K_'+self.options[-1][-1])
                    if event.key == text:
                        run1 = True
                if run1:
                    if flag:
                        if flag == 1:
                            if event.type == pyg.KEYDOWN:
                                if event.key == pyg.K_BACKSPACE:
                                    user_text = user_text[:-1]
                                elif event.key == pyg.K_RETURN:
                                    self.cursor.execute(f"update options set setting  = '{user_text}' where optionName = '{self.options[flag-1][0]}';")
                                    self.cursor.execute("select * from options")
                                    self.options = self.cursor.fetchall()
                                    user_text = ""
                                    flag = 0
                                else:
                                    user_text += event.unicode
                                    if not user_text.isalpha() and int(user_text) > 300:
                                        user_text = '299'
                        elif flag == 2:
                            if event.type == pyg.KEYDOWN:
                                if event.key == pyg.K_BACKSPACE:
                                    user_text = user_text[:-1]
                                elif event.key == pyg.K_RETURN:
                                    self.cursor.execute(f"update options set setting  = '{user_text}' where optionName = '{self.options[flag-1][0]}';")
                                    self.cursor.execute("select * from options")
                                    self.options = self.cursor.fetchall()
                                    user_text = ""
                                    flag = 0
                                else:
                                    user_text += event.unicode
                                    if int(user_text) > 20:
                                        user_text = user_text[:-1]
                        elif flag == 3:
                            if event.type == pyg.KEYDOWN:
                                if event.key == pyg.K_BACKSPACE:
                                    user_text = user_text[:-1]
                                elif event.key == pyg.K_RETURN:
                                    self.cursor.execute(f"update options set setting  = '{user_text}' where optionName = '{self.options[flag-1][0]}';")
                                    self.cursor.execute("select * from options")
                                    self.options = self.cursor.fetchall()
                                    user_text = ""
                                    flag = 0
                                else:
                                    user_text += event.unicode
                                    if len(user_text) > 1:
                                        user_text = user_text[:-1]
                                    if not user_text.isalpha() and user_text.isdigit():
                                        user_text = user_text[:-1]
                        elif flag == 4:
                            if event.type == pyg.KEYDOWN:
                                if event.key == pyg.K_BACKSPACE:
                                    user_text = user_text[:-1]
                                elif event.key == pyg.K_RETURN:
                                    self.cursor.execute(f"update options set setting  = '{user_text}' where optionName = '{self.options[flag-1][0]}';")
                                    self.cursor.execute("select * from options")
                                    self.options = self.cursor.fetchall()
                                    user_text = ""
                                    flag = 0
                                else:
                                    user_text += event.unicode
                                    if len(user_text) > 1:
                                        user_text = user_text[:-1]
                                    if not user_text.isalpha() and user_text.isdigit():
                                        user_text = user_text[:-1]

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

                if flag != 0:
                    text = font.render(user_text, True, (255, 255, 255))
                    pyg.draw.rect(window, (255, 255, 255), rectList1[flag-1], 4)
                    window.blit(text, rectList1[flag-1])

            
             
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
        flag = 0
        user_text = ''
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
                    if run1 == False:
                        if rectList[0].collidepoint(pyg.mouse.get_pos()):
                                self.beatmakerNode()
                        elif rectList[1].collidepoint(pyg.mouse.get_pos()):
                                run1 = True
                        elif rectList[2].collidepoint(pyg.mouse.get_pos()):
                                run = False

                    elif run1:
                        for i, rect in enumerate(rectList1):
                            if rect.collidepoint(pyg.mouse.get_pos()):
                                self.cursor.execute(f"update options set setting  = '' where optionName = '{self.options[i][0]}';")
                                self.cursor.execute("select * from options")
                                self.options = self.cursor.fetchall()
                                flag = i+1

                if run1:
                    if flag:
                        if flag == 1:
                            if event.type == pyg.KEYDOWN:
                                if event.key == pyg.K_BACKSPACE:
                                    user_text = user_text[:-1]
                                elif event.key == pyg.K_RETURN:
                                    self.cursor.execute(f"update options set setting  = '{user_text}' where optionName = '{self.options[flag-1][0]}';")
                                    self.cursor.execute("select * from options")
                                    self.options = self.cursor.fetchall()
                                    user_text = ""
                                    flag = 0
                                else:
                                    user_text += event.unicode
                                    if not user_text.isalpha() and int(user_text) > 300:
                                        user_text = '299'
                        elif flag == 2:
                            if event.type == pyg.KEYDOWN:
                                if event.key == pyg.K_BACKSPACE:
                                    user_text = user_text[:-1]
                                elif event.key == pyg.K_RETURN:
                                    self.cursor.execute(f"update options set setting  = '{user_text}' where optionName = '{self.options[flag-1][0]}';")
                                    self.cursor.execute("select * from options")
                                    self.options = self.cursor.fetchall()
                                    user_text = ""
                                    flag = 0
                                else:
                                    user_text += event.unicode
                                    if int(user_text) > 20:
                                        user_text = user_text[:-1]
                        elif flag == 3:
                            if event.type == pyg.KEYDOWN:
                                if event.key == pyg.K_BACKSPACE:
                                    user_text = user_text[:-1]
                                elif event.key == pyg.K_RETURN:
                                    self.cursor.execute(f"update options set setting  = '{user_text}' where optionName = '{self.options[flag-1][0]}';")
                                    self.cursor.execute("select * from options")
                                    self.options = self.cursor.fetchall()
                                    user_text = ""
                                    flag = 0
                                else:
                                    user_text += event.unicode
                                    if len(user_text) > 1:
                                        user_text = user_text[:-1]
                                    if not user_text.isalpha() and user_text.isdigit():
                                        user_text = user_text[:-1]
                        elif flag == 4:
                            if event.type == pyg.KEYDOWN:
                                if event.key == pyg.K_BACKSPACE:
                                    user_text = user_text[:-1]
                                elif event.key == pyg.K_RETURN:
                                    self.cursor.execute(f"update options set setting  = '{user_text}' where optionName = '{self.options[flag-1][0]}';")
                                    self.cursor.execute("select * from options")
                                    self.options = self.cursor.fetchall()
                                    user_text = ""
                                    flag = 0
                                else:
                                    user_text += event.unicode
                                    if len(user_text) > 1:
                                        user_text = user_text[:-1]
                                    if not user_text.isalpha() and user_text.isdigit():
                                        user_text = user_text[:-1]

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

                if flag != 0:
                    text = font.render(user_text, True, (255, 255, 255))
                    pyg.draw.rect(window, (255, 255, 255), rectList1[flag-1], 4)
                    window.blit(text, rectList1[flag-1])
                        

                    
            pyg.display.update()


newwindow = BeatSequencer()
newwindow.menu()
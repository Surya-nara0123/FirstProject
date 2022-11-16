import pygame as pyg
import sys
import mysql.connector
mydb = mysql.connector.connect(host="localhost", password="S********123")


class BeatSequencer:


    # loading the contents of the database as a constructor
    def __init__(self):
        self.cursor = mydb.cursor()
        self.cursor.execute("show databases")
        databases = self.cursor.fetchall()
        if ('BeatMakerSettings',) in databases:
            self.cursor.execute("use BeatMakerSettings")
        else:
            self.cursor.execute("create database BeatMakerSettings")
            self.cursor.execute("create table Options(OptionName varchar(50), Setting varchar(20))")
            self.cursor.execute("insert into Options('BPM',              120")
            self.cursor.execute("insert into Options('Beats Per Cycle',  6  ")
            self.cursor.execute("insert into Options('Pause/Play',       p  ")
            self.cursor.execute("insert into Options('Open Options',     o  ")
            self.cursor.execute("insert into Options('clear the screen', c  ")
            self.cursor.execute("insert into Options('save',             s  ")
        self.cursor.execute("select * from options")    
        self.options = self.cursor.fetchall()
        self.menu()
    

    # Beat Sequencer part of the app
    def beatmakerNode(self):
        #initializing the modules
        pyg.mixer.init()
        pyg.init()


        # Creating the Window and cofiguring the settings
        width = 800
        height = 600
        window = pyg.display.set_mode((width, height))
        icon = pyg.image.load("SuryaAssets/DrumsLogo.png")
        pyg.display.set_icon(icon)


        # Assigning Variables
        no_beats = int(self.options[1][-1])
        play1 = [pyg.mixer.Sound("SuryaAssets/kick.WAV"),
                 pyg.mixer.Sound("SuryaAssets/snare.WAV"),
                 pyg.mixer.Sound("SuryaAssets/hi hat.WAV"),
                 pyg.mixer.Sound("SuryaAssets/clap.WAV"),
                 pyg.mixer.Sound("SuryaAssets/crash.WAV"),
                 pyg.mixer.Sound("SuryaAssets/tom.wav")]
        run = True
        clock = pyg.time.Clock()
        
        # Button Variables and Adding initial Settings
        flagList = [
            [],
            [],
            [],
            [],
            [],
            [],
            []
        ]
        for j, list in enumerate(flagList):
            for i in range(no_beats):
                list.append(False)
        rectList = [
            [],
            [],
            [],
            [],
            [],
            [],
            []
        ]
        for j, list in enumerate(rectList):
            for i in range(no_beats):
                list.append(pyg.Rect(105 + ((width-105)/no_beats) * (i) , (height/len(play1)) * (j), width/no_beats-20, height/len(play1)-5))
        
        # Other useful variables
        run1 = False
        flag = False
        play = False
        user_text = ''
        active_length = 0
        active_beat = 0
        beat_changed = False
        counter = 0


        # Starting The main loop
        while run:
            
            # This What is drawn for every iteration of the loop
            window.fill((0,0,0))
            pyg.draw.rect(window, (80, 80, 80), (0, 0, 100, window.get_height()))
            for i in rectList:
                for j in i:
                    if flagList[rectList.index(i)][i.index(j)] == False:
                        pyg.draw.rect(window, (80, 80, 80), j, 0, 5)
                    else:
                        pyg.draw.rect(window, (0, 255, 80), j, 0, 5)
            for i in rectList:
                pyg.draw.rect(window, (0, 255, 255),i[active_beat], 5)

            
            # This what is displayed when the options window in opened
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
            clock.tick(60)
            
            
            # Controlling the beats
            if beat_changed:
                for i in range(len(flagList)):
                    if flagList[i][active_beat]:
                        play1[i].play()
                beat_changed = False

            if run1 == False:
                bmp = int(self.options[0][-1])
                beat_length = 3600//bmp 
            if play:
                if active_length < beat_length:
                    active_length += 1
                else:
                    active_length = 0
                    if active_beat < no_beats - 1:
                        active_beat += 1
                        beat_changed = True
                    else:
                        active_beat = 0
                        beat_changed = True
            

            # Event Manager
            for event in pyg.event.get():
                # Statement to Close the window when we want to
                if event.type == pyg.QUIT:
                    run = False
                # These commands are executed when we click our mouse
                if event.type == pyg.MOUSEBUTTONDOWN:
                    # If click our mouse when we are not in the options window
                    if run1 == False:
                        for i in rectList:
                            for j in i:
                                if j.collidepoint(pyg.mouse.get_pos()):
                                    if flagList[rectList.index(i)][i.index(j)] == False:
                                        flagList[rectList.index(i)][i.index(j)] = True
                                        if not play:
                                            play1[rectList.index(i)].play()
                                    else:
                                        flagList[rectList.index(i)][i.index(j)] = False
                    
                    # If click our mouse when we are in the options window                    
                    elif run1:
                        for i, rect in enumerate(rectList1):
                            if rect.collidepoint(pyg.mouse.get_pos()):
                                self.cursor.execute(f"update options set setting  = '' where optionName = '{self.options[i][0]}';")
                                self.cursor.execute("select * from options")
                                self.options = self.cursor.fetchall()
                                flag = i+1

                # If we press any thing ok our key board when the options window is not open
                elif event.type == pyg.KEYDOWN:
                    text = eval('pyg.K_'+self.options[-1][-1])
                    if event.key == text:
                        run1 = True
                    text = eval('pyg.K_'+self.options[-2][-1])
                    if event.key == text:
                        if play:
                            play = False
                        else:
                            play = True
                            beat_changed = True
                # If we press any thing ok our key board when the options window is not open
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


    def menu(self):
        pyg.init()
        width, height = 800, 600
        window = pyg.display.set_mode((width, height))
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
                            if rect[1].collidepoint(pyg.mouse.get_pos()):
                                self.cursor.execute(f"update options set setting  = '' where optionName = '{self.options[i][0]}';")
                                self.cursor.execute("select * from options")
                                self.options = self.cursor.fetchall()
                                flag = i+1

                if run1:
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
                                if not user_text.isdigit():
                                    user_text = user_text[:-1]
                                elif int(user_text) > 300:
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
                                if not user_text.isdigit():
                                    user_text = user_text[:-1]
                                elif int(user_text) > 20:
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
                    elif flag == 5:
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
                    elif flag == 6:
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
                #pyg.draw.line()
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
                    rectList1.append([pyg.Rect(width/6, (i+5)*0.75*((height-300)/len(self.options)), 100, 50 ), pyg.Rect(4*width/6, (i+5)*0.75*((height-300)/len(self.options)), 100, 50 )])
                heading = font.render("Controls and Settings", False, (255, 255, 255))
                window.blit(heading,(window.get_width()/3, window.get_height()/6))
                heading = font.render("Back----->Escape", False, (255, 255, 255))
                window.blit(heading,(0, 0))
                for i, (name, setting) in enumerate(self.options):
                    heading = font.render(name, False, (255, 255, 255))
                    window.blit(heading, rectList1[i][0])
                    heading = font.render(setting, False, (255, 255, 255))
                    window.blit(heading,rectList1[i][1])

                if flag != 0:
                    text = font.render(user_text, True, (255, 255, 255))
                    pyg.draw.rect(window, (255, 255, 255), rectList1[flag-1][1], 4)
                    window.blit(text, rectList1[flag-1][1])
                        

                    
            pyg.display.update()


if __name__ == '__main__':
    newwindow = BeatSequencer()
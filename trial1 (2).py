import random
import pygame
import datetime
from datetime import date
# creating the window
pygame.init()
WIDTH = 1000
HEIGHT = 700

FPS = 200
clock=pygame.time.Clock()
SCREEN1 = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("CALCULATOR")
bg_image = pygame.image.load("HariniAssets/im 10.jpeg").convert_alpha()
bgimage = pygame.transform.scale(bg_image, (1000,700))
SCREEN1.blit(bgimage,(0,0))
blue = (0,191,255)

#variables
action = False
h = False
DEFAULT_IMAGE_SIZE = (80, 80)

#functions

class button():
    def __init__(self,x,y,image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)
        
    def draw(self):
        action = False
        SCREEN1.blit(self.image,(self.rect.x,self.rect.y))
        return self.rect

def drawbutton(a,b,c):
    y = button(a,b,c)
    s = y.draw()
    return s

def finalbutton(x,a,b):
            aa_image = pygame.image.load(x)
            aaimage = pygame.transform.scale(aa_image, (75,75))
            n = drawbutton(a,b,aaimage)
            return n
def word(x,y,a,b):
                        font = pygame.font.Font('freesansbold.ttf', y)
                        textcd = font.render(x, True, blue)
                        
                        textRectcd = textcd.get_rect()
                        textRectcd.center = (a,b)
                        SCREEN1.blit(textcd, textRectcd)
def calc():
    run  = True
    while run:
        
        
        SCREEN1.fill((255,255,255))
        word('scientific calculator',45,500,100)
        pygame.display.update()
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    run1 = False
    
def gst():
    run  = True
    while run:       
        
        SCREEN1.fill((255,255,255))
        word('currency conversion',45,500,100)
        pygame.display.update()
        
        
        
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    run1 = False
def Time():
    run  = True
    options1 = False
    options2 = False
    open_options = pygame.image.load("HariniAssets/open_options_button.png")
    open_options = pygame.transform.smoothscale(open_options, (75,75))
    rect1 = open_options.get_rect()
    rect2 = open_options.get_rect()
    rect1.topleft = (360, 165)
    rect2.topleft = (510, 165)
    leftOption = "Year"
    rightoption = ''
    textList = []
    textList2 = []
    inputno = ''
    processno = ''
    outputno = 0
    while run:       
        
        SCREEN1.blit(bgimage,(0,0))
        word('time',45,500,100)
        pygame.draw.rect(SCREEN1,(255,255,255),pygame.Rect(300,400,300,225))
        pygame.draw.rect(SCREEN1,(255,255,255),pygame.Rect(100,150,350,100))
        pygame.draw.rect(SCREEN1,(255,255,255),pygame.Rect(500,150,350,100))
        dictList = [
            
            '1',
            '2',
            '3',
            'AC',
            '4',
            '5',
            '6',
            'back',
            '7',
            '8',
            '9',
            '0'
        ]
                
        L = ['HariniAssets/1_button_image.png','HariniAssets/2_button_image.png','HariniAssets/3_button_image.png','HariniAssets/AC_button_image.png','HariniAssets/4_button_image.png','HariniAssets/5_button_image.png','HariniAssets/6_button_image.png','HariniAssets/back_button_image.png','HariniAssets/7_button_image.png','HariniAssets/8_button_image.png','HariniAssets/9_button_image.png','HariniAssets/0_button_image.png']
        i = 0
        a = 300
        b = 400
        l2=[]
        while i<len(L):
            a2 = pygame.Rect(a, b , 75, 75)
            l2 += [a2]
            i += 1
            a += 75
            if i == 4 or i == 8 :
                a = 300
                b = b + 75
        for i in L:
            button_image = pygame.image.load(i)
            button_image = pygame.transform.smoothscale(button_image, (75,75))
            SCREEN1.blit(button_image, (l2[L.index(i)]))
        open_options = pygame.image.load("HariniAssets/open_options_button.png")
        open_options = pygame.transform.smoothscale(open_options, (75,75))
        rect1 = open_options.get_rect()
        rect2 = open_options.get_rect()
        rect1.topleft = (360, 165)
        rect2.topleft = (510, 165)
        SCREEN1.blit(open_options, rect1)
        SCREEN1.blit(open_options, rect2)
        
        
        
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    run1 = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    for i in l2:
                        if i.collidepoint(pygame.mouse.get_pos()):
                            inputno += (dictList[l2.index(i)])
                            if dictList[l2.index(i)] == 'back':
                                inputno = inputno[:-5]
                            if dictList[l2.index(i)] == 'AC':
                                inputno = ''

                    if rect1.collidepoint(pygame.mouse.get_pos()):
                        if options1 == options2 == False:
                            options1 = True
                        elif options1 == True:
                            options1 = False
                    if rect2.collidepoint(pygame.mouse.get_pos()):
                        if options1 == options2 == False:
                            options2 = True
                        elif options2 == True:
                            options2 = False
                    if options1:
                        for i, rect in enumerate(textList):
                            if rect.collidepoint(pygame.mouse.get_pos()):
                                leftOption = text[i]
                                options1 = False
                    if options2:
                        for i, rect in enumerate(textList2):
                            if rect.collidepoint(pygame.mouse.get_pos()):
                                rightoption = text[i]
                                options2 = False
        
        if options1:
            pygame.draw.rect(SCREEN1, (255, 255, 255), (50, 300, 200, 350))
            textList = [
                pygame.Rect(50, 250 + 250/4, 200, 250/4),
                pygame.Rect(50, 250 + 2*250/4, 200, 250/4),
                pygame.Rect(50, 250 + 3*250/4, 200, 250/4),
                pygame.Rect(50, 250 + 4*250/4, 200, 250/4),
                pygame.Rect(50, 250 + 5*250/4, 200, 250/4),
                pygame.Rect(50, 250 + 6*250/4, 200, 250/4)
            ]
        
            
            text = [
                "Year",
                "Day",
                'Week',
                "Hour",
                "Minute",
                "Second"
            ]
            for i in textList:
                font = pygame.font.Font('freesansbold.ttf', 30)
                textcd = font.render(text[textList.index(i)], True, blue)
                SCREEN1.blit(textcd, i)
        if options2:
            pygame.draw.rect(SCREEN1, (255, 255, 255), (800, 300, 200, 350))
            textList2 = [
                pygame.Rect(800, 250 + 250/4, 200, 250/4),
                pygame.Rect(800, 250 + 2*250/4, 200, 250/4),
                pygame.Rect(800, 250 + 3*250/4, 200, 250/4),
                pygame.Rect(800, 250 + 4*250/4, 200, 250/4),
                pygame.Rect(800,250 + 5*250/4,200,250/4),
                pygame.Rect(800,250 + 6*250/4,200,250/4)]
            for i in textList2:
                font = pygame.font.Font('freesansbold.ttf', 30)
                textcd = font.render(text[textList2.index(i)], True, blue)
                SCREEN1.blit(textcd, i)
            if leftOption == 'Year':
                processno = int(inputno) 
            elif leftOption == 'Day':
                processno = int(inputno)/365
                
            elif leftOption == 'Week':
                processno = (int(inputno)*7)/365
            elif leftOption == 'Hour':
                processno = (int(inputno)/24)/365
            elif leftOption == 'Minute':
                processno = int(inputno)/(60*7*365)
            elif leftOption == 'Second':
                processno = int(inputno)/(60*60*7*365)
            
                
            
            if rightoption == 'Year':
                outputno = processno
                
            if rightoption == 'Day':
                outputno = processno*365
            if rightoption == 'Week':
                outputno = (processno*365)/7
            if rightoption == 'Hour':
                outputno = processno*24*365
            if rightoption == 'Minute':
                outputno = processno*60*7*365
            if rightoption == 'Second':
                outputno = processno*60*60*7*365
            
            
           
                
        
        font = pygame.font.Font('freesansbold.ttf', 30)
        textcd = font.render(str(outputno), True, blue)
        SCREEN1.blit(textcd,(600,200))    
        font = pygame.font.Font('freesansbold.ttf', 30)
        textcd = font.render(inputno, True, blue)
        SCREEN1.blit(textcd,(100,150))

        pygame.display.update()
        
def bmi():
    run  = True
    while run:       
        
        SCREEN1.fill((255,255,255))
        word('BMI',45,500,100)
        pygame.display.update()
        
        
        
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    run1 = False
def data():
    run  = True
    options1 = False
    options2 = False
    open_options = pygame.image.load("HariniAssets/open_options_button.png")
    open_options = pygame.transform.smoothscale(open_options, (75,75))
    rect1 = open_options.get_rect()
    rect2 = open_options.get_rect()
    rect1.topleft = (360, 165)
    rect2.topleft = (510, 165)
    leftOption = "byte"
    rightoption = ''
    textList = []
    textList2 = []
    inputno = ''
    processno = ''
    outputno = 0
    while run:       
        
        SCREEN1.blit(bgimage,(0,0))
        word('Data conversion',45,500,100)
        pygame.draw.rect(SCREEN1,(255,255,255),pygame.Rect(300,400,300,225))
        pygame.draw.rect(SCREEN1,(255,255,255),pygame.Rect(100,150,350,100))
        pygame.draw.rect(SCREEN1,(255,255,255),pygame.Rect(500,150,350,100))
        dictList = [
            
            '1',
            '2',
            '3',
            'AC',
            '4',
            '5',
            '6',
            'back',
            '7',
            '8',
            '9',
            '0'
        ]
                
        L = ['HariniAssets/1_button_image.png','HariniAssets/2_button_image.png','HariniAssets/3_button_image.png','HariniAssets/AC_button_image.png','HariniAssets/4_button_image.png','HariniAssets/5_button_image.png','HariniAssets/6_button_image.png','HariniAssets/back_button_image.png','HariniAssets/7_button_image.png','HariniAssets/8_button_image.png','HariniAssets/9_button_image.png','HariniAssets/0_button_image.png']
        i = 0
        a = 300
        b = 400
        l2=[]
        while i<len(L):
            a2 = pygame.Rect(a, b , 75, 75)
            l2 += [a2]
            i += 1
            a += 75
            if i == 4 or i == 8 :
                a = 300
                b = b + 75
        for i in L:
            button_image = pygame.image.load(i)
            button_image = pygame.transform.smoothscale(button_image, (75,75))
            SCREEN1.blit(button_image, (l2[L.index(i)]))
        open_options = pygame.image.load("HariniAssets/open_options_button.png")
        open_options = pygame.transform.smoothscale(open_options, (75,75))
        rect1 = open_options.get_rect()
        rect2 = open_options.get_rect()
        rect1.topleft = (360, 165)
        rect2.topleft = (510, 165)
        SCREEN1.blit(open_options, rect1)
        SCREEN1.blit(open_options, rect2)
        
        
        
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    run1 = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    for i in l2:
                        if i.collidepoint(pygame.mouse.get_pos()):
                            inputno += (dictList[l2.index(i)])
                            if dictList[l2.index(i)] == 'back':
                                inputno = inputno[:-5]
                            if dictList[l2.index(i)] == 'AC':
                                inputno = ''

                    if rect1.collidepoint(pygame.mouse.get_pos()):
                        if options1 == options2 == False:
                            options1 = True
                        elif options1 == True:
                            options1 = False
                    if rect2.collidepoint(pygame.mouse.get_pos()):
                        if options1 == options2 == False:
                            options2 = True
                        elif options2 == True:
                            options2 = False
                    if options1:
                        for i, rect in enumerate(textList):
                            if rect.collidepoint(pygame.mouse.get_pos()):
                                leftOption = text[i]
                                options1 = False
                    if options2:
                        for i, rect in enumerate(textList2):
                            if rect.collidepoint(pygame.mouse.get_pos()):
                                rightoption = text[i]
                                options2 = False
        
        if options1:
            pygame.draw.rect(SCREEN1, (255, 255, 255), (50, 300, 200, 300))
            textList = [
                pygame.Rect(50, 250 + 250/4, 200, 250/4),
                pygame.Rect(50, 250 + 2*250/4, 200, 250/4),
                pygame.Rect(50, 250 + 3*250/4, 200, 250/4),
                pygame.Rect(50, 250 + 4*250/4, 200, 250/4),
                pygame.Rect(50, 250 + 5*250/4, 200, 250/4)
            ]
        
            
            text = [
                "Byte",
                "Kilobyte",
                "Megabyte",
                "Gigabyte",
                "Terabyte"
            ]
            for i in textList:
                font = pygame.font.Font('freesansbold.ttf', 30)
                textcd = font.render(text[textList.index(i)], True, blue)
                SCREEN1.blit(textcd, i)
        if options2:
            pygame.draw.rect(SCREEN1, (255, 255, 255), (800, 300, 200, 300))
            textList2 = [
                pygame.Rect(800, 250 + 250/4, 200, 250/4),
                pygame.Rect(800, 250 + 2*250/4, 200, 250/4),
                pygame.Rect(800, 250 + 3*250/4, 200, 250/4),
                pygame.Rect(800, 250 + 4*250/4, 200, 250/4),
                pygame.Rect(800,250 + 5*250/4,200,250/4)]
            for i in textList2:
                font = pygame.font.Font('freesansbold.ttf', 30)
                textcd = font.render(text[textList2.index(i)], True, blue)
                SCREEN1.blit(textcd, i)
            if leftOption == 'Byte':
                processno = int(inputno) 
            elif leftOption == 'Kilobyte':
                processno = int(inputno)*1024
                
            elif leftOption == 'Megabyte':
                processno = int(inputno)*1048576
            elif leftOption == 'Gigabyte':
                processno = int(inputno)*1073741824
            elif leftOption == 'Terabyte':
                processno = int(inputno)*1099511627776
                
            
            if rightoption == 'Byte':
                outputno = processno
                
            if rightoption == 'Kilobyte':
                outputno = processno/1024
            if rightoption == 'Megabyte':
                outputno = processno/1048576
            if rightoption == 'Gigabyte':
                outputno = processno/1073741824
            if rightoption == 'Terabyte':
                outputno = processno/1099511627776
            
            
           
                
        
        font = pygame.font.Font('freesansbold.ttf', 30)
        textcd = font.render(str(outputno), True, blue)
        SCREEN1.blit(textcd,(600,200))    
        font = pygame.font.Font('freesansbold.ttf', 30)
        textcd = font.render(inputno, True, blue)
        SCREEN1.blit(textcd,(100,150))


        pygame.display.update()
def discount():
    run  = True
           
        
    SCREEN1.blit(bgimage,(0,0))
    word('Discount',45,500,100)
    pygame.draw.rect(SCREEN1,(255,255,255),pygame.Rect(300,400,300,225))
    font = pygame.font.Font('freesansbold.ttf', 30)
    textcd = font.render('Orginal Price' ,True,(255,255,255) )
    SCREEN1.blit(textcd,(100,150))
    font = pygame.font.Font('freesansbold.ttf', 30)
    textcd = font.render('Discount(percentage 0ff)' ,True,(255,255,255) )
    SCREEN1.blit(textcd,(100,200))
    font = pygame.font.Font('freesansbold.ttf', 30)
    textcd = font.render('Discounted price' ,True,(255,255,255) )
    SCREEN1.blit(textcd,(100,250))
    
   
    
    option = 1
    inputno = ''
    dis = ''
    
    
        
    
        
    while run:   
        pygame.draw.rect(SCREEN1,(255,255,255),pygame.Rect(500,250,400,30))
        pygame.draw.rect(SCREEN1,(255,255,255),pygame.Rect(500,150,400,30))
        pygame.draw.rect(SCREEN1,(255,255,255),pygame.Rect(500,200,400,30))
        pygame.draw.rect(SCREEN1,(255,255,255),pygame.Rect(550,300,200,30))
        dictList = [
            
            '1',
            '2',
            '3',
            'AC',
            '4',
            '5',
            '6',
            'back',
            '7',
            '8',
            '9',
            '0'
        ]
                
        L = ['HariniAssets/1_button_image.png','HariniAssets/2_button_image.png','HariniAssets/3_button_image.png','HariniAssets/AC_button_image.png','HariniAssets/4_button_image.png','HariniAssets/5_button_image.png','HariniAssets/6_button_image.png','HariniAssets/back_button_image.png','HariniAssets/7_button_image.png','HariniAssets/8_button_image.png','HariniAssets/9_button_image.png','HariniAssets/0_button_image.png']
        i = 0
        a = 300
        b = 400
        l2=[]
        while i<len(L):
            a2 = pygame.Rect(a, b , 75, 75)
            l2 += [a2]
            i += 1
            a += 75
            if i == 4 or i == 8 :
                a = 300
                b = b + 75
        for i in L:
            button_image = pygame.image.load(i)
            button_image = pygame.transform.smoothscale(button_image, (75,75))
            SCREEN1.blit(button_image, (l2[L.index(i)]))
        
        
        
        for event in pygame.event.get():
                
                    
                if event.type == pygame.QUIT:
                    run = False
                    run1 = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if pygame.Rect(500,200,400,30).collidepoint(pygame.mouse.get_pos()):
                        option = 0
                    if option:     
                        for i in l2: 
                            if i.collidepoint(pygame.mouse.get_pos()):
                                

                                inputno += (dictList[l2.index(i)])
                                if dictList[l2.index(i)] == 'back':
                                    inputno = inputno[:-5]
                                if dictList[l2.index(i)] == 'AC':
                                    inputno = ''
                    if not option:
                        for i in l2: 
                            if i.collidepoint(pygame.mouse.get_pos()):
                                

                                dis += (dictList[l2.index(i)])
                                if dictList[l2.index(i)] == 'back':
                                    dis = dis[:-5]
                                if dictList[l2.index(i)] == 'AC':
                                    dis = ''
        if inputno != ''and dis != '':
            processno = (int(inputno))*(int(dis)/100)
            finalamt = int(inputno) - processno            
            font = pygame.font.Font('freesansbold.ttf', 30)
            textcd = font.render(str(finalamt), True, blue)
            SCREEN1.blit(textcd,(600,250)) 
                
            font = pygame.font.Font('freesansbold.ttf', 30)
            textcd = font.render('You save', True, (255,255,255))
            SCREEN1.blit(textcd,(400,300)) 
            font = pygame.font.Font('freesansbold.ttf', 30)
            textcd = font.render(str(processno), True,blue)
            SCREEN1.blit(textcd,(550,300))      
                                
                   
                                                     
                
        font = pygame.font.Font('freesansbold.ttf', 30)
        textcd = font.render(inputno, True, blue)
        SCREEN1.blit(textcd,(600,150)) 
                
        font = pygame.font.Font('freesansbold.ttf', 30)
        textcd = font.render(dis, True, blue)
        SCREEN1.blit(textcd,(600,200)) 
        


        pygame.display.update()  
                
                
                
                
                    

                    
                                    
                        
            
        
def equation():
    run  = True
    while run:       
        
        SCREEN1.fill((255,255,255))
        word('Equation solver',45,500,100)
        pygame.display.update()
        
        
        
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    run1 = False
def age():
    run  = True
    
    
    inputno = ''
    processno = ''
    month = [ 31, 28, 31, 30, 31, 30,
                    31, 31, 30, 31, 30, 31]
    while run:
                SCREEN1.blit(bgimage,(0,0))
                word('Know your age!',45,500,100)
                word('Date of birth',25,350,200)
                word('current date',25,350,250)
                today = date.today()
                pygame.draw.rect(SCREEN1,(255,255,255),pygame.Rect(470,170,300,35))
                
                
                curdate= today.strftime('%d/%m/%y')
                cyear = int(today.strftime("%y"))+2000
                cmonth = int(today.strftime("%m"))
                cdate = int(today.strftime("%d"))
                
                word(curdate,25,650,250)
                
                dictList = [
                    '1',
                    '2',
                    '3',
                    'AC',
                    '4',
                    '5',
                    '6',
                    'back',
                    '7',
                    '8',
                    '9',
                    '0']
                
                L = ['HariniAssets/1_button_image.png','HariniAssets/2_button_image.png','HariniAssets/3_button_image.png','HariniAssets/AC_button_image.png','HariniAssets/4_button_image.png','HariniAssets/5_button_image.png','HariniAssets/6_button_image.png','HariniAssets/back_button_image.png','HariniAssets/7_button_image.png','HariniAssets/8_button_image.png','HariniAssets/9_button_image.png','HariniAssets/0_button_image.png']
                i = 0
                a = 300
                b = 400
                l2=[]
                while i<len(L):
                    a2 = pygame.Rect(a, b , 75, 75)
                    l2 += [a2]
                    i += 1
                    a += 75
                    if i == 4 or i == 8 :
                        a = 300
                        b = b + 75
                for i in L:
                    button_image = pygame.image.load(i)
                    button_image = pygame.transform.smoothscale(button_image, (75,75))
                    SCREEN1.blit(button_image, (l2[L.index(i)])) 
                for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            run = False
                              
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            for i in l2:
                                if i.collidepoint(pygame.mouse.get_pos()):
                                    
                                    
                                    inputno += dictList[l2.index(i)]
                                    
                                    if dictList[l2.index(i)] == 'back':
                                        inputno = inputno[:-5]
                                    if dictList[l2.index(i)] == 'AC':
                                        inputno = ''
                                pygame.display.update()
                if len(inputno)<3:
                    processno = inputno
                if len(inputno)<5 and len(inputno)>2:
                    processno = inputno[:2]+'/'+inputno[2:]
                if len(inputno)<9 and len(inputno)>4:
                    processno = inputno[:2]+'/'+inputno[2:4]+'/'+inputno[4:]
                if len(inputno)==8:
                    
                    birthyear = int(processno[6:])
                    birthmonth = int(processno[3:5])
                    birthdate = int(processno[:2])
                    nextbday = datetime.date(cyear+1,birthmonth,birthdate)
                    nextbday_week = nextbday.strftime('%A')
                    if birthdate<cdate:
                        calc2month = cmonth - birthmonth - 1
                        calc2date = month[birthmonth-1]-(cdate - birthdate)
                    else:
                        calc2month = cmonth-birthmonth
                        calc2date = birthdate - cdate
                    
                    if birthdate>cdate:
                        cdate = cdate+month[birthmonth-1]
                        cmonth = cmonth - 1
                    if birthmonth>cmonth:
                        cmonth += 12
                        cyear = cyear - 1
                    calcdate = cdate - birthdate
                    calcmonth = cmonth - birthmonth
                    calcyear = cyear - birthyear
                    
                    output = (calcdate,calcmonth,calcyear,calc2date,calc2month,nextbday_week)

                    def result(output):
                
                        run2 = True
                        while run2:
                            SCREEN1.blit(bgimage,(0,0))
                            pygame.draw.rect(SCREEN1,(255,255,255),pygame.Rect(250,100,500,300))
                            word('You are',45,450,150)
                            word('years',15,450,200)
                            word('Months',15,550,200)
                            word('Days',15,650,200)
                            word(str(output[2]),30,400,200)
                            word(str(output[1]),25,500,200)
                            word(str(output[0]),20,600,200)
                            word(str(output[4]),25,400,300)
                            word(str(output[3]),20,500,300)
                            word(str(output[5]),20,330,300)
                            word('Months',15,450,300)
                            word('Days',15,550,300)

                            word('Next Birthday',45,450,250)
                            

                            pygame.display.update()
                            for event in pygame.event.get():
                                if event.type == pygame.QUIT:
                                    run = False
                                    run2 = False
                    if finalbutton('HariniAssets/GO_button_image.png',400,400):
                        result(output)  
                        pygame.display.update  
                    pygame.display.update

                
                            
                font = pygame.font.Font('freesansbold.ttf', 30)
                textcd = font.render(processno, True, blue)
                SCREEN1.blit(textcd,(470,170))    

        
            
                





        
                pygame.display.update()
                
                            
                
                                    
                
        
               
        

def base():
    word('Base convertor',45,500,100)
    run  = True
    options1 = False
    options2 = False
    open_options = pygame.image.load("HariniAssets/open_options_button.png")
    open_options = pygame.transform.smoothscale(open_options, (75,75))
    rect1 = open_options.get_rect()
    rect2 = open_options.get_rect()
    rect1.topleft = (360, 165)
    rect2.topleft = (510, 165)
    leftOption = "Hexadecimal"
    rightoption = ''
    textList = []
    textList2 = []
    inputno = ''
    processno = 0
    outputno = 0
    while run:
        SCREEN1.blit(bgimage,(0,0))
        pygame.draw.rect(SCREEN1,(255,255,255),pygame.Rect(100,150,350,100))
        pygame.draw.rect(SCREEN1,(255,255,255),pygame.Rect(500,150,350,100))
        pygame.draw.rect(SCREEN1,(255,255,255),pygame.Rect(300,350,450,225))
        L = ['HariniAssets/A_button_image.png',
             'HariniAssets/B_button_image.png',
             'HariniAssets/1_button_image.png',
             'HariniAssets/2_button_image.png',
             'HariniAssets/3_button_image.png',
             'HariniAssets/AC_button_image.png',
             'HariniAssets/C_button_image.png',
             'HariniAssets/D_button_image.png',
             'HariniAssets/4_button_image.png',
             'HariniAssets/5_button_image.png',
             'HariniAssets/6_button_image.png',
             'HariniAssets/back_button_image.png',
             'HariniAssets/E_button_image.png',
             'HariniAssets/F_button_image.png',
             'HariniAssets/7_button_image.png',
             'HariniAssets/8_button_image.png',
             'HariniAssets/9_button_image.png',
             'HariniAssets/0_button_image.png'
             ]

        dictList = [
            'A',
            'B',
            '1',
            '2',
            '3',
            'AC',
            'C',
            'D',
            '4',
            '5',
            '6',
            'back',
            'E',
            'F',
            '7',
            '8',
            '9',
            '0'
        ]
        
        i = 0
        a = 300
        b = 350
        l2 = []
        
        while i<len(L):
            a2 = pygame.Rect(a, b , 75, 75)
            l2 += [a2]
            i += 1
            a += 75
            if i == 6 or i == 12 :
                a = 300
                b = b + 75
        for i in L:
            button_image = pygame.image.load(i)
            button_image = pygame.transform.smoothscale(button_image, (75,75))
            SCREEN1.blit(button_image, (l2[L.index(i)]))

        open_options = pygame.image.load("HariniAssets/open_options_button.png")
        open_options = pygame.transform.smoothscale(open_options, (75,75))
        rect1 = open_options.get_rect()
        rect2 = open_options.get_rect()
        rect1.topleft = (360, 165)
        rect2.topleft = (510, 165)
        SCREEN1.blit(open_options, rect1)
        SCREEN1.blit(open_options, rect2)
        
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    for i in l2:
                        if i.collidepoint(pygame.mouse.get_pos()):
                             
                            if leftOption == 'Hexadecimal':
                                inputno += (dictList[l2.index(i)])

                            elif leftOption == 'Binary':
                                if dictList[l2.index(i)] == '0' or dictList[l2.index(i)] == '1':
                                    inputno += (dictList[l2.index(i)])
                            elif leftOption == 'Decimal':
                                if dictList[l2.index(i)] == 'A' or dictList[l2.index(i)] == 'B' or dictList[l2.index(i)] == 'C' or dictList[l2.index(i)] == 'D'or dictList[l2.index(i)] == 'E' or dictList[l2.index(i)] == 'F':
                                    pass
                                else:
                                    inputno += (dictList[l2.index(i)])
                            elif leftOption == 'Octal':
                                if dictList[l2.index(i)] == '1' or dictList[l2.index(i)] == '2' or dictList[l2.index(i)] == '3' or dictList[l2.index(i)] == '4'or dictList[l2.index(i)] == '5' or dictList[l2.index(i)] == '6' or dictList[l2.index(i)] == '7':
                                    inputno += (dictList[l2.index(i)])
                            if dictList[l2.index(i)] == 'back':
                                inputno = inputno[:-5]
                            if dictList[l2.index(i)] == 'AC':
                                inputno = ''
                                
                    if rect1.collidepoint(pygame.mouse.get_pos()):
                        if options1 == options2 == False:
                            options1 = True
                        elif options1 == True:
                            options1 = False
                    if rect2.collidepoint(pygame.mouse.get_pos()):
                        if options1 == options2 == False:
                            options2 = True
                        elif options2 == True:
                            options2 = False
                    if options1:
                        for i, rect in enumerate(textList):
                            if rect.collidepoint(pygame.mouse.get_pos()):
                                leftOption = text[i]
                                options1 = False
                    if options2:
                        for i, rect in enumerate(textList2):
                            if rect.collidepoint(pygame.mouse.get_pos()):
                                rightoption = text[i]
                                options2 = False
        
        if options1:
            pygame.draw.rect(SCREEN1, (255, 255, 255), (50, 300, 200, 250))
            textList = [
                pygame.Rect(50, 250 + 250/4, 200, 250/4),
                pygame.Rect(50, 250 + 2*250/4, 200, 250/4),
                pygame.Rect(50, 250 + 3*250/4, 200, 250/4),
                pygame.Rect(50, 250 + 4*250/4, 200, 250/4)
            ]
        
            
            text = [
                "Hexadecimal",
                "Binary",
                "Decimal",
                "Octal"
            ]
            for i in textList:
                font = pygame.font.Font('freesansbold.ttf', 30)
                textcd = font.render(text[textList.index(i)], True, blue)
                SCREEN1.blit(textcd, i)
           

        font = pygame.font.Font('freesansbold.ttf', 30)
        textcd = font.render(inputno, True, blue)
        SCREEN1.blit(textcd,(100,150))
        if options2:
            pygame.draw.rect(SCREEN1, (255, 255, 255), (800, 300, 200, 250))
            textList2 = [
                pygame.Rect(800, 250 + 250/4, 200, 250/4),
                pygame.Rect(800, 250 + 2*250/4, 200, 250/4),
                pygame.Rect(800, 250 + 3*250/4, 200, 250/4),
                pygame.Rect(800, 250 + 4*250/4, 200, 250/4)]
            for i in textList2:
                font = pygame.font.Font('freesansbold.ttf', 30)
                textcd = font.render(text[textList2.index(i)], True, blue)
                SCREEN1.blit(textcd, i)

            if leftOption == 'Decimal':
                processno = int(inputno) 
            elif leftOption == 'Binary':
                processno = int(inputno,2)
                
            elif leftOption == 'Hexadecimal':
                processno = int(inputno,16)
            elif leftOption == 'Octal':
                processno = int(inputno,8)
            
            if rightoption == 'Decimal':
                outputno = processno
                
            if rightoption == 'Binary':
                outputno = bin(processno)[2:]
            if rightoption == 'Octal':
                outputno = oct(processno)[2:]
            if rightoption == 'Hexadecimal':
           
                outputno = hex(processno)[2:]
        
        font = pygame.font.Font('freesansbold.ttf', 30)
        textcd = font.render(str(outputno), True, blue)
        SCREEN1.blit(textcd,(600,200))    

        
            
                





        pygame.display.update()
        
functionCalls = [
    gst,
    calc,
    age,
    Time,
    base,
    data,
    discount,
    bmi,
    equation,
]
def main():
    run1  = True
    while run1:
        SCREEN1.blit(bgimage,(0,0))
        #button
        buttonList = [
                        finalbutton('HariniAssets/im3.png',250,200),
                        finalbutton('HariniAssets/im 1.png',450,200),
                        finalbutton('HariniAssets/im2.jpeg',650,200),
                        
                        finalbutton('HariniAssets/im 4.jfif',250,350),
                        finalbutton('HariniAssets/im 5.png',450,350),
                        finalbutton('HariniAssets/im 6.png',650,350),

                        finalbutton('HariniAssets/im 7.png',250,500),
                        finalbutton('HariniAssets/im 8.png',450,500),
                        finalbutton('HariniAssets/im 9.png',650,500)
                      ]
        #text
        word('Calculator',55,500,100)
        word('GST',15,280,300)
        word('scientific calculator',15,500,300)
        word('Age',15,700,300)
        word('Time',15,280,450)
        word('Base conversions',15,500,450)
        word('Data conversion',15,700,450)
        word('Discount',15,300,600)
        word('BMI',15,470,600)
        word('Equation solver',15,700,600)
        
           
        pygame.display.update()
        
        
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run1 = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                for rect in range(len(buttonList)):
                    if buttonList[rect].collidepoint(pygame.mouse.get_pos()):
                        functionCalls[rect]()

        
    pygame.quit()
main()

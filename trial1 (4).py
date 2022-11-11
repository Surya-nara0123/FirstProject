import random
import pygame
import math
import datetime
from datetime import date
import pyttsx3

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
class stack:
    def __init__(self, size = None):
        self.s = []
        self.top = None
        self.size = size
    def push(self, value : any):
        if self.top == None:
            self.top = 0
            self.s.append(value)
        else:
            if self.size != None and self.size != None and self.top < self.size:
                self.top += 1
                self.s.append(value)
            elif self.size == None:
                self.top += 1
                self.s.append(value)
    def pull(self):
        if self.top != None:
            if self.top == 0:
                self.top = None
                return self.s.pop()
            else:
                self.top -= 1
                return self.s.pop()
    def peak(self):
        if self.top != None:
            return self.s[self.top]

def drawbutton(a,b,c):
    y = button(a,b,c)
    s = y.draw()
    return s

def finalbutton(x,a,b):
            aa_image = pygame.image.load(x)
            aaimage = pygame.transform.scale(aa_image, (125,125))
            n = drawbutton(a,b,aaimage)
            return n
def word(x,y,a,b):
                        font = pygame.font.Font('burnstown.ttf', y)
                        textcd = font.render(x, True, (255,255,255))
                        
                        textRectcd = textcd.get_rect()
                        textRectcd.center = (a,b)
                        SCREEN1.blit(textcd, textRectcd)
def calc():
    run  = True
    SCREEN1.blit(bgimage,(0,0))
    pygame.draw.rect(SCREEN1,blue,pygame.Rect(50,180,440,150))
    pygame.draw.rect(SCREEN1,blue,pygame.Rect(500,180,440,150))
    inputno = ''
    outputno = 0
    processno = ''
    flag = False
    evaluatingStack = stack()
    tempStack = stack()
    operators ='^/*+-'
    while run:
        
        
        
        pygame.draw.rect(SCREEN1,(255,255,255),pygame.Rect(70,200,400,110))
        pygame.draw.rect(SCREEN1,(255,255,255),pygame.Rect(520,200,400,110))
        word('scientific calculator',75,500,100)
        dictList = [
            
            '1',
            '2',
            '3',
            'AC',
            '+',
            '*',
            'e',
            '^(-1)',
            '^',
            'Sin(',
            'sin inv(',
            '.',
            '4',
            '5',
            '6',
            'back',
            '-',
            '=',
            'ln(',
            '!',
            '(',
            'Tan(',
            'tan inv(',
            '^2',
            '7',
            '8',
            '9',
            '0',
            '/',
            'π',
            'lg(',
            '^(1/2)',
            ')',
            'Cos(',
            'cos inv(',
            '%'
        ]
                
        L = ['HariniAssets/1_button_image.png','HariniAssets/2_button_image.png','HariniAssets/3_button_image.png',
        'HariniAssets/AC_button_image.png','HariniAssets/+.png','HariniAssets/multi.png',
        'HariniAssets/e.png','HariniAssets/one by x.png','HariniAssets/x pow y.png',
        'HariniAssets/sin.png','HariniAssets/sin inv.png','HariniAssets/point.png',
        'HariniAssets/4_button_image.png','HariniAssets/5_button_image.png','HariniAssets/6_button_image.png','HariniAssets/back_button_image.png',
        'HariniAssets/minus.png','HariniAssets/equals.png','HariniAssets/ln.png',
        'HariniAssets/fact.png','HariniAssets/(.png','HariniAssets/tan.png',
        'HariniAssets/tan inv.png','HariniAssets/x sq.png','HariniAssets/7_button_image.png',
        'HariniAssets/8_button_image.png','HariniAssets/9_button_image.png','HariniAssets/0_button_image.png',
        'HariniAssets/div.png','HariniAssets/pi.png','HariniAssets/lg.png',
        'HariniAssets/sqrt.png','HariniAssets/).png','HariniAssets/cos.png','HariniAssets/cos inv.png',
        'HariniAssets/per.png']
        i = 0
        a = 50
        b = 400
        l2=[]
        while i<len(L):
            a2 = pygame.Rect(a, b , 75, 75)
            l2 += [a2]
            i += 1
            a += 75
            if i == 12 or i == 24 :
                a = 50
                b = b + 75
        for i in L:
            button_image = pygame.image.load(i)
            button_image = pygame.transform.smoothscale(button_image, (75,75))
            SCREEN1.blit(button_image, (l2[L.index(i)]))
        
        
        pygame.display.update()
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                
                    run = False
                    run1 = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    for i in l2:
                        if i.collidepoint(pygame.mouse.get_pos()):
                            inputno += (dictList[l2.index(i)])
                           
                            if dictList[l2.index(i)] == '=':
                                inputno = inputno[:-1]
                                flag = True
                            if dictList[l2.index(i)] == 'back':
                                inputno = inputno[:-5]
                            if dictList[l2.index(i)] == 'AC':
                                inputno = ''
                            if dictList[l2.index(i)] == '%':
                                try:
                                    inputno = inputno[:-3] + str(inputno[-3:-1]/100)
                                except:
                                    inputno = inputno[:-2] + str(int(inputno[-2])/100)
        
        if inputno != '' and flag == True:
            for i in inputno:
                s = inputno.index(i)
                if i == 'e':
                    processno = inputno[:s]+'2.71828'+ inputno[s+1:]
                
                
                if i == 'π':
                    processno = inputno[:s]+'3.14159'+ inputno[s+1:]
            
                if i == ' ':
                    processno = inputno[:s-3]+'a'+inputno[s-3:s]+inputno[s+4:]
                else:
                    processno = inputno    
                
            processno2 = ''
            
           
            for i in processno:
                
                s = processno.index(i)
                
                
                    
                if i == 'l'and processno[s+1] =='n':
                    f = processno.index(')',s)
                    k = math.log[int(processno[s+3:f])]
                    processno2 = processno[:s]+str(k)+processno[f+1:]
                if i == 'l'and processno[s+1] =='g':
                    f = processno.index(')',s)
                    k = math.log[int(processno[s+3:f]),10]
                    processno2 = processno[:s]+str(k)+processno[f+1:]
                if i == '!':
                    if processno2[s-2].isnumeric():

                        k = math.factorial(int(processno[s-2:s]))
                    processno2 = processno[:s]+str(k)+processno[s+1:]
                if i=='a' and processno[s+1] == 's':
                    s = processno.index(i)
                    f = processno.index(')',s)
                    k = math.asin(int(processno[s+5:f]))
                    processno2 = processno[:s]+str(k)+processno[f+1:]
                if i=='a' and processno[s+1] == 'c':
                    f = processno.index(')',s)
                    k = math.acos(int(processno[s+5:f]))
                    processno2 = processno[:s]+str(k)+processno[f+1:]
                if i=='a' and processno[s+1] == 't':
                    f = processno.index(')',s)
                    k = math.atan(int(processno[s+5:f]))
                    processno2 = processno[:s]+str(k)+processno[f+1:]
                if i=='S':
                    
                    f = processno.index(')',s)
                    k = math.sin(int(processno[s+4:f]))
                    
                    processno2 = processno[:s]+str(k)+processno[f+1:]
                if i=='C':
                    f = processno.index(')',s)
                    k = math.cos(int(processno[s+4:f]))
                    processno2 = processno[:s]+str(k)+processno[f+1:]
                if i=='T':
                    f = processno.index(')',s)
                    k = math.tan(int(processno[s+4:f]))
                    processno2 = processno[:s]+str(k)+processno[f+1:]
            evalString  =  processno2 
            
            for i in evalString:
                if i == ' ':
                    continue
                elif i not in operators and i not in "()":
                    evaluatingStack.push(i)
                else:
                    if i == "(":
                        tempStack.push(i)
            
            
                    elif i == ")":
                        if tempStack.top != None:
                            while tempStack.peak() != "(":
                                evaluatingStack.push(tempStack.pull())
                            tempStack.pull()
                    else:
                        if tempStack.top != None:
                            if tempStack.peak() in operators and  operators.index(tempStack.peak()) >= operators.index(i):
                                tempStack.push(i)
                            elif tempStack.peak() in operators:
                                evaluatingStack.push(tempStack.pull())
                                tempStack.push(i)
                            else:
                                tempStack.push(i)
            st = ''
            for i in evaluatingStack.s:
                st += i
            
            outputStack = stack()
            for i in st:
                if i not in operators:
                    outputStack.push(i)
        
                else:
                    value2 = outputStack.pull()
                    value1 = outputStack.pull()
                    outputStack.push(str(eval(value1+ i+ value2)))
            run = True
            while run:
                value = evaluatingStack.pull()
                if value not in operators:
                     evaluatingStack.push(value)
       
                else:
                    value2 = evaluatingStack.pull()
                    value1 = evaluatingStack.pull()
                    evaluatingStack.push(str(value1+value+value2))
                if value == None:
                    run = False 

            
            
                

                    

        font = pygame.font.Font('freesansbold.ttf', 30)
        textcd = font.render(inputno, True, blue)
        SCREEN1.blit(textcd,(90,200))
        font = pygame.font.Font('freesansbold.ttf', 30)
        textcd = font.render(str(evaluatingStack.s), True, blue)
        SCREEN1.blit(textcd,(540,200))
        pygame.display.update()


    
def gst():
    run  = True
           
        
    SCREEN1.blit(bgimage,(0,0))
    word('GST',75,500,100)
    pygame.draw.rect(SCREEN1,(255,255,255),pygame.Rect(300,400,300,225))
    font = pygame.font.Font('freesansbold.ttf', 30)
    textcd = font.render('Original Price' ,True,(255,255,255) )
    SCREEN1.blit(textcd,(100,150))
    font = pygame.font.Font('freesansbold.ttf', 30)
    textcd = font.render('GST%' ,True,(255,255,255) )
    SCREEN1.blit(textcd,(100,200))
    font = pygame.font.Font('freesansbold.ttf', 30)
    textcd = font.render('Final Price' ,True,(255,255,255) )
    SCREEN1.blit(textcd,(100,250))
    pygame.draw.rect(SCREEN1,blue,pygame.Rect(495,245,410,40))
    pygame.draw.rect(SCREEN1,blue,pygame.Rect(495,145,410,40))
    pygame.draw.rect(SCREEN1,blue,pygame.Rect(495,195,410,40))
    pygame.draw.rect(SCREEN1,blue,pygame.Rect(290,390,320,245))
    
    option = 1
    inputno = ''
    dis = ''
    
    
        
    
        
    while run:   
        pygame.draw.rect(SCREEN1,(255,255,255),pygame.Rect(500,250,400,30))
        pygame.draw.rect(SCREEN1,(255,255,255),pygame.Rect(500,150,400,30))
        pygame.draw.rect(SCREEN1,(255,255,255),pygame.Rect(500,200,400,30))
        
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
        pygame.display.update()
        
        
        
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
            finalamt = int(inputno) + processno            
            font = pygame.font.Font('freesansbold.ttf', 30)
            textcd = font.render(str(finalamt), True, blue)
            SCREEN1.blit(textcd,(600,250)) 
                
                   
                                
                   
                                                     
                
        font = pygame.font.Font('freesansbold.ttf', 30)
        textcd = font.render(inputno, True, blue)
        SCREEN1.blit(textcd,(600,150)) 
                
        font = pygame.font.Font('freesansbold.ttf', 30)
        textcd = font.render(dis, True, blue)
        SCREEN1.blit(textcd,(600,200)) 
        


        pygame.display.update()
def Time():
    run  = True
    SCREEN1.blit(bgimage,(0,0))
    options1 = False
    options2 = False
    open_options = pygame.image.load("HariniAssets/open_options_button.png")
    open_options = pygame.transform.smoothscale(open_options, (75,75))
    pygame.draw.rect(SCREEN1,blue,pygame.Rect(290,390,320,245))
    pygame.draw.rect(SCREEN1,blue,pygame.Rect(90,140,370,120))
    pygame.draw.rect(SCREEN1,blue,pygame.Rect(490,140,370,120))
    leftOption = "Year"
    rightoption = ''
    textList = []
    textList2 = []
    inputno = ''
    processno = ''
    outputno = 0
    while run:       
        
        
        word('Time',75,500,100)
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
        open_options = pygame.transform.smoothscale(open_options, (25,25))
        rect1 = open_options.get_rect()
        rect2 = open_options.get_rect()
        rect1.topleft = (420, 220)
        rect2.topleft = (820, 220)
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
            if inputno!='':
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
    
    SCREEN1.blit(bgimage,(0,0))
    word('BMI',75,500,100)
    word('Weight(kg)',45,250,170)
    word('Height(cm)',45,250,280)
    option = 1
    weight = ''
    height = ''
    output = ''
    pygame.draw.rect(SCREEN1,blue,pygame.Rect(495,245,410,60))
    pygame.draw.rect(SCREEN1,blue,pygame.Rect(495,145,410,60))
    pygame.draw.rect(SCREEN1,blue,pygame.Rect(290,390,320,245))
    
    
    while run:       
        pygame.draw.rect(SCREEN1,(255,255,255),pygame.Rect(500,250,400,50))
        pygame.draw.rect(SCREEN1,(255,255,255),pygame.Rect(500,150,400,50))
    
        
        
        
        
        
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
        
        pygame.display.update()
       
        
        
        
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    run1 = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if pygame.Rect(500,250,400,50).collidepoint(pygame.mouse.get_pos()):
                        option = 0
                    if pygame.Rect(500,150,400,50).collidepoint(pygame.mouse.get_pos()):
                        option = 1    
                    if option:     
                        for i in l2: 
                            if i.collidepoint(pygame.mouse.get_pos()):
                                

                                weight += (dictList[l2.index(i)])
                                if dictList[l2.index(i)] == 'back':
                                    weight = weight[:-5]
                                if dictList[l2.index(i)] == 'AC':
                                    weight = ''
                                pygame.display.update()
                    if not option:
                        for i in l2: 
                            if i.collidepoint(pygame.mouse.get_pos()):
                                

                                height += (dictList[l2.index(i)])
                                if dictList[l2.index(i)] == 'back':
                                    height = height[:-5]
                                if dictList[l2.index(i)] == 'AC':
                                    height = ''
                    if rect1.collidepoint(pygame.mouse.get_pos()):
                        result(output)
        def result(output):
                
                        run2 = True
                        while run2:
                            SCREEN1.blit(bgimage,(0,0))
                            pygame.draw.rect(SCREEN1,blue,pygame.Rect(250,100,500,200))
                            word('BMI',45,450,150)
                            word(str(output),30,450,200)
                            word(message,45,450,250)
                            x = pygame.image.load('HariniAssets/BMI.png')
                            x = pygame.transform.smoothscale(x, (500,500))
                            SCREEN1.blit(x,(250,300))
                            
                            pygame.display.update()
                        
                            engine = pyttsx3.init()
                            for i in range(1):
                                engine.say('Your BMI is')
                                engine.say(str(output))
                                engine.say(message)
                                engine.runAndWait()

                            pygame.display.update()
                            for event in pygame.event.get():
                                if event.type == pygame.QUIT:
                                    run = False
                                    run2 = False  
                                
                                
                                
        if height != '' and weight != '':
            output = (int(weight)/int(height)**2)*10000
            if output < 18.5:
                message = 'Underweight'
            elif output < 24.9:
                message = 'Normal'
            elif output < 30:
                message = 'Overweight'
            else:
                message = 'Obese'
        go_option = pygame.image.load("HariniAssets/GO_button_image.png")
        go_option = pygame.transform.smoothscale(go_option, (75,75))
        rect1 = go_option.get_rect()
        
        rect1.topleft = (700, 500)
        
        SCREEN1.blit(go_option, rect1)
        
        font = pygame.font.Font('freesansbold.ttf', 30)
        textcd = font.render(weight, True, blue)
        SCREEN1.blit(textcd,(600,150)) 
                
        font = pygame.font.Font('freesansbold.ttf', 30)
        textcd = font.render(height, True, blue)
        SCREEN1.blit(textcd,(600,250))
        pygame.display.update()
        
def data():
    run  = True
    SCREEN1.blit(bgimage,(0,0))
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
    pygame.draw.rect(SCREEN1,blue,pygame.Rect(290,390,320,245))
    pygame.draw.rect(SCREEN1,blue,pygame.Rect(90,140,370,120))
    pygame.draw.rect(SCREEN1,blue,pygame.Rect(490,140,370,120))
    while run:       
        
        
        word('Data conversion',75,500,100)
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
        open_options = pygame.transform.smoothscale(open_options, (25,25))
        rect1 = open_options.get_rect()
        rect2 = open_options.get_rect()
        rect1.topleft = (420, 220)
        rect2.topleft = (820, 220)
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
            if inputno == '':

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
    word('Discount',75,500,100)
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
    pygame.draw.rect(SCREEN1,blue,pygame.Rect(495,245,410,40))
    pygame.draw.rect(SCREEN1,blue,pygame.Rect(495,145,410,40))
    pygame.draw.rect(SCREEN1,blue,pygame.Rect(495,195,410,40))
    pygame.draw.rect(SCREEN1,blue,pygame.Rect(290,390,320,245))
   
    
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
        pygame.display.update()
        
        
        
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
            pygame.display.update()        
                                
                   
                                                     
                
        font = pygame.font.Font('freesansbold.ttf', 30)
        textcd = font.render(inputno, True, blue)
        SCREEN1.blit(textcd,(600,150)) 
                
        font = pygame.font.Font('freesansbold.ttf', 30)
        textcd = font.render(dis, True, blue)
        SCREEN1.blit(textcd,(600,200)) 
        


        pygame.display.update()  
def equation():
    run  = True
    option = 0
    A = ''
    B = ''
    C = ''
    SCREEN1.blit(bgimage,(0,0))
    word('Equation solver',75,500,100)
    pygame.draw.rect(SCREEN1,(255,255,255),pygame.Rect(195,145,100,110))
    pygame.draw.rect(SCREEN1,(255,255,255),pygame.Rect(495,145,100,110))
    pygame.draw.rect(SCREEN1,(255,255,255),pygame.Rect(795,145,100,110))
    while run:  
        pygame.draw.rect(SCREEN1,blue,pygame.Rect(200,150,90,100))
        pygame.draw.rect(SCREEN1,blue,pygame.Rect(500,150,90,100))
        pygame.draw.rect(SCREEN1,blue,pygame.Rect(800,150,90,100))
        xsq = pygame.image.load('HariniAssets/X square.png')
        xsq = pygame.transform.smoothscale(xsq, (100,100))
        x = pygame.image.load('HariniAssets/x.png')
        x = pygame.transform.smoothscale(x, (100,100))
        SCREEN1.blit(xsq,(300,150))
        SCREEN1.blit(x,(600,150))
        word('+',100,450,200)
        word('+',100,750,200)
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
            '0',
            '-'
        ]
                
        L = ['HariniAssets/1_button_image.png','HariniAssets/2_button_image.png','HariniAssets/3_button_image.png','HariniAssets/AC_button_image.png','HariniAssets/4_button_image.png','HariniAssets/5_button_image.png','HariniAssets/6_button_image.png','HariniAssets/back_button_image.png','HariniAssets/7_button_image.png','HariniAssets/8_button_image.png','HariniAssets/9_button_image.png','HariniAssets/0_button_image.png','HariniAssets/minus.png']
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
        
        
        
        pygame.display.update()
        
        
        
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    run1 = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if pygame.Rect(200,150,90,100).collidepoint(pygame.mouse.get_pos()):
                        option = 1
                    if pygame.Rect(500,150,90,100).collidepoint(pygame.mouse.get_pos()):
                        option = 2
                    if pygame.Rect(800,150,90,100).collidepoint(pygame.mouse.get_pos()):
                        option = 3
                    if option == 1:     
                        for i in l2: 
                            if i.collidepoint(pygame.mouse.get_pos()):
                                

                                A += (dictList[l2.index(i)])
                                if dictList[l2.index(i)] == 'back':
                                    A = A[:-5]
                                if dictList[l2.index(i)] == 'AC':
                                    A = ''
                    if  option == 2:
                        for i in l2: 
                            if i.collidepoint(pygame.mouse.get_pos()):
                                

                                B += (dictList[l2.index(i)])
                                if dictList[l2.index(i)] == 'back':
                                    B = B[:-5]
                                if dictList[l2.index(i)] == 'AC':
                                    B = ''
                    if  option == 3:
                        for i in l2: 
                            if i.collidepoint(pygame.mouse.get_pos()):
                                

                                C += (dictList[l2.index(i)])
                                if dictList[l2.index(i)] == 'back':
                                    C = C[:-5]
                                if dictList[l2.index(i)] == 'AC':
                                    C = ''
        if A != '' and B != '' and C != '':
            Aa = int(A)
            Bb = int(B)
            Cc = int(C)
            if Aa == 0:
                ans1 = ans2 = -Cc/Bb
            else:
                disc = pow(Bb,2)-4*Aa*Cc
                if disc>0:

                    ans1 = (-Bb + pow(disc,0.5))/(2*Aa)
                    ans2 = (-Bb - pow((pow(Bb,2)-4*Aa*Cc),0.5))/(2*Aa)
                elif disc<0:
                    ans1 = 'complex roots'
                    ans2 = ''
                else:
                    ans1 = ans2 = -Bb/(2*Aa)
            word('ANS :',45,350,300)
            word(str(ans1),45,600,300)
            word(str(ans2),45,600,350)
        word(A,45,250,200)
        word(B,45,550,200)
        word(C,45,840,200)
        
        pygame.display.update()
        

def age():
    run  = True
    
    flag = True
    inputno = ''
    processno = ''
    month = [ 31, 28, 31, 30, 31, 30,
                    31, 31, 30, 31, 30, 31]
    output = ()
    SCREEN1.blit(bgimage,(0,0))
    pygame.draw.rect(SCREEN1,blue,pygame.Rect(290,390,320,245))
    pygame.draw.rect(SCREEN1,blue,pygame.Rect(500,180,320,55))
    
    while run:
                def result(output):
                
                        run2 = True
                        while run2:
                            SCREEN1.blit(bgimage,(0,0))
                            pygame.draw.rect(SCREEN1,blue,pygame.Rect(250,100,500,300))
                            word('You are',75,450,150)
                            word('years',45,370,200)
                            word('Months',45,550,200)
                            word('Days',45,700,200)
                            word(str(output[2]),45,300,200)
                            word(str(output[1]),35,460,200)
                            word(str(output[0]),25,640,200)
                            word(str(output[4]),45,300,300)
                            word(str(output[3]),35,500,300)
                            word(str(output[5]),35,450,350)
                            word('Months',45,400,300)
                            word('Days',45,570,300)

                            word('Next Birthday',75,470,250)
                            engine = pyttsx3.init()
                            pygame.display.update()
                            for i in range(1):
                                engine.say('Your are'+ str(output[2])+'years'+str(output[1])+'Months'+str(output[0])+'Days old')
                                
                                engine.say('Next Birthday will be on a'+str(output[5])+'It will be coming in'+str(output[4])+'Months'+str(output[3])+'Days')
                                
                                
                                engine.runAndWait()
                            for event in pygame.event.get():
                                if event.type == pygame.QUIT:
                                    run = False
                                    run2 = False
                                    print(run2,run)
                            
                
                word('Know your age!',75,500,100)
                word('Date of birth',55,350,200)
                word('current date',55,350,250)
                today = date.today()
                pygame.draw.rect(SCREEN1,(255,255,255),pygame.Rect(510,190,300,35))
                
                
                curdate= today.strftime('%d/%m/%y')
                cyear = int(today.strftime("%y"))+2000
                cmonth = int(today.strftime("%m"))
                cdate = int(today.strftime("%d"))
                
                word(curdate,55,650,250)
                
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
                go_option = pygame.image.load("HariniAssets/GO_button_image.png")
                go_option = pygame.transform.smoothscale(go_option, (75,75))
                rect1 = go_option.get_rect()
                rect1.topleft = (700, 500)
        
                SCREEN1.blit(go_option, rect1)
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
                            if rect1.collidepoint(pygame.mouse.get_pos()):
                                result(output)
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
                        calc2month = 12-(cmonth - birthmonth - 1)
                        calc2date = month[birthmonth-1]-(cdate - birthdate)
                    else:
                        
                        calc2date = birthdate - cdate
                        if birthmonth>cmonth:
                            calc2month = (birthmonth-cmonth)
                        else:
                            calc2month = 12 -(cmonth-birthmonth)
                    
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
                    

                    
                
                            

                            
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        run = False
                        run2 = False
                        
                    
                      
                pygame.display.update()        

                
                            
                font = pygame.font.Font('freesansbold.ttf', 30)
                textcd = font.render(processno, True, blue)
                SCREEN1.blit(textcd,(510,190))  
                  

        
            
                





        
                pygame.display.update()
                
                            
                
                                    
                
        
               
        

def base():
    
    run  = True
    options1 = False
    options2 = False
    open_options = pygame.image.load("HariniAssets/open_options_button.png")
    open_options = pygame.transform.smoothscale(open_options, (25,25))
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
    SCREEN1.blit(bgimage,(0,0))
    pygame.draw.rect(SCREEN1,blue,pygame.Rect(90,140,370,120))
    pygame.draw.rect(SCREEN1,blue,pygame.Rect(490,140,370,120))
    pygame.draw.rect(SCREEN1,blue,pygame.Rect(290,340,470,245))
    while run:
        
        word('Base convertor',75,500,100)
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
        open_options = pygame.transform.smoothscale(open_options, (25,25))
        rect1 = open_options.get_rect()
        rect2 = open_options.get_rect()
        rect1.topleft = (420, 220)
        rect2.topleft = (820, 220)
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
            if inputno != '':

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
                        finalbutton('HariniAssets/2.png',250,200),
                        #finalbutton('HariniAssets/im 1.png',450,200),
                        #finalbutton('HariniAssets/im2.png',650,200),
                        
                        #finalbutton('HariniAssets/im 4.png',250,350),
                        #finalbutton('HariniAssets/im 5.png',450,350),
                        finalbutton('HariniAssets/3.png',650,350),

                        #finalbutton('HariniAssets/im 7.png',250,500),
                        finalbutton('HariniAssets/BMI.png',450,500),
                        finalbutton('HariniAssets/4.png',650,500)
                      ]
      
        word('CALCULATOR',95,500,100)
        
        
           
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

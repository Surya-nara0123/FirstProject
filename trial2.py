import random
import pygame
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
    
def currency():
    run  = True
    while run:       
        
        SCREEN1.fill((255,255,255))
        word('currency conversion',45,500,100)
        pygame.display.update()
        
        
        
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    run1 = False
def time():
    run  = True
    while run:       
        
        SCREEN1.fill((255,255,255))
        word('time',45,500,100)
        pygame.display.update()
        
        
        
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    run1 = False
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
    while run:       
        
        SCREEN1.fill((255,255,255))
        word('Data conversion',45,500,100)
        pygame.display.update()
        
        
        
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    run1 = False
def unit():
    run  = True
    while run:       
        
        SCREEN1.fill((255,255,255))
        word('Unit conversion',45,500,100)
        pygame.display.update()
        
        
        
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    run1 = False
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
    while run:
        def result():
                
                run2 = True
                while run2:
                    SCREEN1.fill((255,255,255))
                    word('Age',45,450,150)
                    word('Next Birthday',45,450,450)
                    finalbutton('HariniAssets/im2.jpeg',300,500)

                    pygame.display.update()
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            
                            run2 = False
        
                SCREEN1.fill((255,255,255))
                word('Know your age!',45,500,100)
                word('Date of birth',25,350,200)
                word('current date',25,350,250)
                pygame.draw.rect(SCREEN1,(255,255,255),pygame.Rect(300,300,325,225))
                
                L = ['HariniAssets/2_button_image.png','HariniAssets/3_button_image.png','HariniAssets/AC_button_image.png','HariniAssets/4_button_image.png','HariniAssets/5_button_image.png','HariniAssets/6_button_image.png','HariniAssets/back_button_image.png','HariniAssets/7_button_image.png','HariniAssets/8_button_image.png','HariniAssets/9_button_image.png','HariniAssets/0_button_image.png']
                i = 0
                a = 300
                b = 300
                l2 = []           #to store the return values
                while i<len(L):
                    a2 = finalbutton(L[i],a,b)
                    l2 += [a2]
                    i += 1
                    a += 75
                    if i == 4 or i == 8 :
                        a = 300
                        b = b + 75
                
                
                
                            
                
                                    
                if finalbutton('HariniAssets/30.png',700,400):
                    result()
        
                pygame.display.update()
                
                
                dob = []
                for event in pygame.event.get():
                        if event.type == pygame.MOUSEMOTION:
                            rectpos = event.pos
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            if l2[0]:
                                dob += ['1']
                                
                                
                            if (l2[1]):
                                dob += ['2']
                                
                            if (l2[2]):
                                
                                dob += ['3']
                            if (l2[4]):
                                dob += ['4']
                            if (l2[5]):
                                dob += ['5']
                            if (l2[6]):
                                dob += ['6']
                            if (l2[8]):
                                dob += ['7']
                            if (l2[9]):
                                dob += ['8']
                            if (l2[10]):
                                dob += ['9']
                            if (l2[11]):
                                dob += ['0']
                            if (l2[3]):
                                dob =[]
                            if (l2[7]):
                                del dob[-1]
                            
                            if len(dob) == 8:            # to print the date after getting it from the user
                                s = ''
                                for i in dob:
                                    if i == 2 or i == 4:
                                        s += '/'
                                    s += i
                                word(s,25,600,170)
                                pygame.display.update()
                            
                                    
                                    
                        
                        

                        if event.type == pygame.QUIT:
                                    
                            run = False
                            run1 = False

def base():
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
    textList = []
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
                "decimal",
                "octal"
            ]
            for i in textList:
                font = pygame.font.Font('freesansbold.ttf', 30)
                textcd = font.render(text[textList.index(i)], True, blue)
                SCREEN1.blit(textcd, i)

        
        pygame.display.update()
        
functionCalls = [
    currency,
    calc,
    age,
    time,
    base,
    unit,
    data,
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
                        finalbutton('HariniAssets/im 5.jpeg',450,350),
                        finalbutton('HariniAssets/im 6.png',650,350),

                        finalbutton('HariniAssets/im 7.png',250,500),
                        finalbutton('HariniAssets/im 8.png',450,500),
                        finalbutton('HariniAssets/im 9.png',650,500)
                      ]
        #text
        word('Calculator',55,500,100)
        word('Currency',15,280,300)
        word('scientific calculator',15,500,300)
        word('Age',15,700,300)
        word('Time',15,280,450)
        word('Base conversions',15,500,450)
        word('Data conversion',15,700,450)
        word('Unit conversion',15,300,600)
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

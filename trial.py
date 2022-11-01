import pygame
# creating the window
pygame.init()
WIDTH = 1000
HEIGHT = 700

FPS = 100
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
        pos  = pygame.mouse.get_pos()
        global h
        if self.rect.collidepoint(pos):
            
            if pygame.mouse.get_pressed()[0]==1 and h == False:
                
                h = True
                action = True
            if pygame.mouse.get_pressed()[0]==0 and h == True:
                h = False
        return action

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
        
        L = ['HariniAssets/one.png','HariniAssets/10.png','HariniAssets/12.png','HariniAssets/8.png','HariniAssets/13.png','HariniAssets/14.png','HariniAssets/15.png','HariniAssets/9.png','HariniAssets/16.png','HariniAssets/17.png','HariniAssets/18.png','HariniAssets/19.png']
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
    while run:
        
        
        SCREEN1.blit(bgimage,(0,0))
        word('Base conversion',45,500,100)
        
        pygame.draw.rect(SCREEN1,(255,255,255),pygame.Rect(100,150,350,100))
        pygame.draw.rect(SCREEN1,(255,255,255),pygame.Rect(500,150,350,100))
        pygame.draw.rect(SCREEN1,(255,255,255),pygame.Rect(300,350,450,225))
        L = ['HariniAssets/20.png','HariniAssets/21.png','HariniAssets/one.png','HariniAssets/10.png','HariniAssets/12.png','HariniAssets/8.png','HariniAssets/22.png','HariniAssets/23.png','HariniAssets/13.png','HariniAssets/14.png','HariniAssets/15.png','HariniAssets/9.png','HariniAssets/24.png','HariniAssets/25.png','HariniAssets/16.png','HariniAssets/17.png','HariniAssets/18.png','HariniAssets/19.png']
        i = 0
        a = 300
        b = 350
        l2 = []           #to store the return values
        while i<len(L):
            
            
            a2 = finalbutton(L[i],a,b)
            l2 += [a2]
            i += 1
            a += 75
            if i == 6 or i == 12 :
                a = 300
                b = b + 75
        
        
        
        pygame.display.update()
        
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    run1 = False
def main():
    run1  = True
    while run1:
        SCREEN1.blit(bgimage,(0,0))
        #button
        if finalbutton('HariniAssets/im 1.png',450,200):
            calc()
        if finalbutton('HariniAssets/im2.jpeg',650,200):
            age()
        if finalbutton('HariniAssets/im3.png',250,200):
            currency()
        if finalbutton('HariniAssets/im 4.jfif',250,350):
            time()
        
        if finalbutton('HariniAssets/im 5.jpeg',450,350):
            base()
        
        if finalbutton('HariniAssets/im 6.png',650,350):
            data()
        if finalbutton('HariniAssets/im 7.png',250,500):
            unit()
        if finalbutton('HariniAssets/im 8.png',450,500):
            bmi()
        if finalbutton('HariniAssets/im 9.png',650,500):
            equation()
        
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

        
    pygame.quit()
main()

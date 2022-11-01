import pygame
import os
pygame.init()
WIDTH = 1000
HEIGHT = 700
action = False
FPS = 30
clock=pygame.time.Clock()
SCREEN1 = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("CALCULATOR")
bg_image = pygame.image.load("HariniAssets/im 10.jpg").convert_alpha()
bgimage = pygame.transform.scale(bg_image, (1000,700))
SCREEN1.blit(bgimage,(0,0))
blue = (0,191,255)
font = pygame.font.SysFont('Cooper Black', 55)
text = font.render('CALCULATOR', True,(255,255,255))
h = False
#text
textRect = text.get_rect()
textRect.center = (500, 100)
font = pygame.font.Font('freesansbold.ttf', 15)
text2 = font.render('Currency', True, (255,255,255))
textRect2 = text.get_rect()
textRect2.center = (450, 330)

text3 = font.render('scientific calculator', True, (255,255,255))
textRect3 = text.get_rect()
textRect3.center = (600, 330)

text4 = font.render('Age', True, (255,255,255))
textRect4 = text.get_rect()
textRect4.center = (870, 330)

text5 = font.render('Time', True, (255,255,255))
textRect5 = text.get_rect()
textRect5.center = (470, 480)

text6 = font.render('Base conversions', True, (255,255,255))
textRect6 = text.get_rect()
textRect6.center = (620, 480)

text7 = font.render('Data conversion', True, (255,255,255))
textRect7 = text.get_rect()
textRect7.center = (840, 480)

text8 = font.render('Unit conversion', True, (255,255,255))
textRect8 = text.get_rect()
textRect8.center = (430, 630)

text9 = font.render('BMI', True,(255,255,255))
textRect9 = text.get_rect()
textRect9.center = (670, 630)

text10 = font.render('Equation solver', True, (255,255,255))
textRect10 = text.get_rect()
textRect10.center = (830, 630)
#image

DEFAULT_IMAGE_SIZE = (80, 80)

calc_image = pygame.image.load("HariniAssets/im 1.png").convert_alpha()
calcimage = pygame.transform.scale(calc_image, DEFAULT_IMAGE_SIZE)
bc_image = pygame.image.load("HariniAssets/im2.jpg").convert_alpha()
bcimage = pygame.transform.scale(bc_image, DEFAULT_IMAGE_SIZE)
cc_image = pygame.image.load("HariniAssets/im3.png").convert_alpha()
ccimage = pygame.transform.scale(cc_image, DEFAULT_IMAGE_SIZE)
dc_image = pygame.image.load("HariniAssets/im 4.jfif").convert_alpha()
dcimage = pygame.transform.scale(dc_image, DEFAULT_IMAGE_SIZE)
ec_image = pygame.image.load("HariniAssets/im 5.jpg").convert_alpha()
ecimage = pygame.transform.scale(ec_image, DEFAULT_IMAGE_SIZE)
fc_image = pygame.image.load("HariniAssets/im 6.png").convert_alpha()
fcimage = pygame.transform.scale(fc_image, DEFAULT_IMAGE_SIZE)
gc_image = pygame.image.load("HariniAssets/im 7.png").convert_alpha()
gcimage = pygame.transform.scale(gc_image, DEFAULT_IMAGE_SIZE)
hc_image = pygame.image.load("HariniAssets/im 8.png").convert_alpha()
hcimage = pygame.transform.scale(hc_image, DEFAULT_IMAGE_SIZE)
ic_image = pygame.image.load("HariniAssets/im 9.png").convert_alpha()
icimage = pygame.transform.scale(ic_image, DEFAULT_IMAGE_SIZE)
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
def my(a,b,c):
    y = button(a,b,c)
    s = y.draw()
    return s

def base():
    run  = True
    while run:
        
        
        SCREEN1.blit(bgimage,(0,0))
        font = pygame.font.SysFont('Cooper Black', 45)
        text21 = font.render('Base conversion', True,  (255,255,255))
        pygame.draw.rect(SCREEN1,(255,255,255),pygame.Rect(100,150,350,100))
        pygame.draw.rect(SCREEN1,(255,255,255),pygame.Rect(500,150,350,100))
        pygame.draw.rect(SCREEN1,(255,255,255),pygame.Rect(300,350,475,225))
        aa_image = pygame.image.load("HariniAssets/one.png").convert_alpha()
        aaimage = pygame.transform.scale(aa_image, (75,75))
        ab_image = pygame.image.load("HariniAssets/10.png").convert_alpha()
        abimage = pygame.transform.scale(ab_image, (75,75))
        ac_image = pygame.image.load("HariniAssets/12.png").convert_alpha()
        acimage = pygame.transform.scale(ac_image, (75,75))
        ad_image = pygame.image.load("HariniAssets/8.png").convert_alpha()
        adimage = pygame.transform.scale(ad_image, (100,75))
        ae_image = pygame.image.load("HariniAssets/13.png").convert_alpha()
        aeimage = pygame.transform.scale(ae_image, (75,75))
        af_image = pygame.image.load("HariniAssets/14.png").convert_alpha()
        afimage = pygame.transform.scale(af_image, (75,75))
        ag_image = pygame.image.load("HariniAssets/15.png").convert_alpha()
        agimage = pygame.transform.scale(ag_image, (75,75))
        ah_image = pygame.image.load("HariniAssets/9.png").convert_alpha()
        ahimage = pygame.transform.scale(ah_image, (100,75))
        ai_image = pygame.image.load("HariniAssets/16.png").convert_alpha()
        aiimage = pygame.transform.scale(ai_image, (75,75))
        aj_image = pygame.image.load("HariniAssets/17.png").convert_alpha()
        ajimage = pygame.transform.scale(aj_image, (75,75))
        ak_image = pygame.image.load("HariniAssets/18.png").convert_alpha()
        akimage = pygame.transform.scale(ak_image, (75,75))
        al_image = pygame.image.load("HariniAssets/19.png").convert_alpha()
        alimage = pygame.transform.scale(al_image, (100,75))
        am_image = pygame.image.load("HariniAssets/20.png").convert_alpha()
        amimage = pygame.transform.scale(am_image, (75,75))
        an_image = pygame.image.load("HariniAssets/21.png").convert_alpha()
        animage = pygame.transform.scale(an_image, (75,75))
        ao_image = pygame.image.load("HariniAssets/22.png").convert_alpha()
        aoimage = pygame.transform.scale(ao_image, (75,75))
        ap_image = pygame.image.load("HariniAssets/23.png").convert_alpha()
        apimage = pygame.transform.scale(ap_image, (75,75))
        aq_image = pygame.image.load("HariniAssets/24.png").convert_alpha()
        aqimage = pygame.transform.scale(aq_image, (75,75))
        as_image = pygame.image.load("HariniAssets/25.png").convert_alpha()
        asimage = pygame.transform.scale(as_image, (75,75))
        ar_image = pygame.image.load("HariniAssets/im 11.png").convert_alpha()
        arimage = pygame.transform.scale(ar_image, (25,25))
                        
                
                
                
                
        my(450,350,aaimage)
        my(525,350,abimage)
        my(600,350,acimage)
        my(675,350,adimage)
        my(450,425,aeimage)
        my(525,425,afimage)
        my(600,425,agimage)
        my(675,425,ahimage)
        my(450,500,aiimage)
        my(525,500,ajimage)
        my(600,500,akimage)
        my(675,500,alimage)
        my(300,350,amimage)
        my(300,425,animage)
        my(300,500,aoimage)
        my(375,350,apimage)
        my(375,425,aqimage)
        my(375,500,asimage)
        textRect21 = text.get_rect()
        textRect21.center = (500, 100)
        SCREEN1.blit(text21, textRect21)
        
        if my(815,220,arimage):
            text23 = font.render('Base conversion', True,  (255,255,255))
            textRect23 = text.get_rect()
            textRect23.center = (715, 300)
            SCREEN1.blit(text23, textRect23)
        
        if my(415,220,arimage):
            pygame.display.update()
            flag = True
            
            
        pygame.display.update()
        for event in pygame.event.get():
                
                    if my(415,220,arimage):
                        pygame.display.update()
                        
                        font = pygame.font.Font('freesansbold.ttf', 35)
                        pygame.draw.rect(SCREEN1,(255,255,255),pygame.Rect(25,300,250,200))
                        text24 = font.render('Hexadecimal', True,  blue,(255,255,255))
                        textRect24 = text.get_rect()
                        textRect24.center = (250, 350)
                        SCREEN1.blit(text24, textRect24)
                        text25 = font.render('decimal', True,blue,(255,255,255))
                        textRect25 = text.get_rect()
                        textRect25.center = (250, 400)
                        SCREEN1.blit(text25, textRect25)
                        text26 = font.render('Octal', True, blue,(255,255,255))
                        textRect26 = text.get_rect()
                        textRect26.center = (250, 450)
                        SCREEN1.blit(text26, textRect26)
                        text27 = font.render('Binary', True,blue)
                        textRect27 = text.get_rect()
                        textRect27.center = (250, 500)
                        SCREEN1.blit(text27, textRect27)
                        pygame.display.update()
                        pos  = pygame.mouse.get_pos()
                
                        global h
                        h = True
                        if textRect24.collidepoint(pos):
                                
                                if pygame.mouse.get_pressed()[0]==1  and h == False:
                
                                    h = True
                                    print('yes')
                                    
                                if pygame.mouse.get_pressed()[0]==0 and h == True :
                                    h = False
               
                

                    if event.type == pygame.QUIT:
        

                        run = False
                        run1 = False
def calc():
    run  = True
    while run:
        
        
        SCREEN1.fill((255,255,255))
        font = pygame.font.Font('freesansbold.ttf', 45)
        text21 = font.render('Scientific calculator', True, blue, (255,255,255))
        textRect21 = text.get_rect()
        textRect21.center = (500, 100)
        SCREEN1.blit(text21, textRect21)
        pygame.display.update()
        
        
        
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    run1 = False
def age():
    run  = True
    while run:
        
        
        SCREEN1.fill((255,255,255))
        
        font = pygame.font.Font('freesansbold.ttf', 45)
        text21 = font.render('Know your age!', True, blue, (255,255,255))
        textRect21 = text.get_rect()
        textRect21.center = (500, 100)
        SCREEN1.blit(text21, textRect21)
        font = pygame.font.Font('freesansbold.ttf', 25)
        textdob = font.render('Date of birth', True, blue, (255,255,255))
        textRectdob = text.get_rect()
        textRectdob.center = (350,200)
        SCREEN1.blit(textdob, textRectdob)
        textcd = font.render('current date', True, blue, (255,255,255))
        textRectcd = text.get_rect()
        textRectcd.center = (350,250)
        SCREEN1.blit(textcd, textRectcd)
        pygame.draw.rect(SCREEN1,(255,255,255),pygame.Rect(300,300,325,225))
        def simple(x,a,b):
            aa_image = pygame.image.load(x).convert_alpha()
            aaimage = pygame.transform.scale(aa_image, (75,75))
            n = my(a,b,aaimage)
            return n
        L = ['HariniAssets/one.png','HariniAssets/10.png','HariniAssets/12.png','HariniAssets/8.png','HariniAssets/13.png','HariniAssets/14.png','HariniAssets/15.png','HariniAssets/9.png','HariniAssets/16.png','HariniAssets/17.png','HariniAssets/18.png','HariniAssets/19.png']
        i = 0
        a = 300
        b = 300
        l2 = []
        while i<len(L):
            
            
            a2 = simple(L[i],a,b)
            l2 += [a2]
            i += 1
            a += 75
            if i == 4 or i == 8 :
                a = 300
                b = b + 75
        
        
        def word(x,y,a,b):
                        font = pygame.font.Font('freesansbold.ttf', y)
                        textcd = font.render(x, True, blue, (255,255,255))
                        textRectcd = text.get_rect()
                        textRectcd.center = (a,b)
                        SCREEN1.blit(textcd, textRectcd)
                    
        def result():
                
                run2 = True
                while run2:
                    SCREEN1.fill((255,255,255))
                    word('Age',45,450,150)
                    word('Next Birthday',45,450,450)
                    my(300,500,bcimage)

                    pygame.display.update()
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            
                            run2 = False
                            
        if simple('HariniAssets/30.png',700,400):
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
                    if len(dob) == 8:
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
        
def currency():
    run  = True
    while run:       
        
        SCREEN1.fill((255,255,255))
        font = pygame.font.Font('freesansbold.ttf', 45)
        text21 = font.render('Currency conversion', True, blue, (255,255,255))
        textRect21 = text.get_rect()
        textRect21.center = (500, 100)
        SCREEN1.blit(text21, textRect21)
        pygame.display.update()
        
        
        
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    run1 = False
def time():
    run  = True
    while run:
        
        
        SCREEN1.fill((255,255,255))
        font = pygame.font.Font('freesansbold.ttf', 45)
        text21 = font.render('Know your time!', True, blue, (255,255,255))
        textRect21 = text.get_rect()
        textRect21.center = (500, 100)
        SCREEN1.blit(text21, textRect21)
        pygame.display.update()
        
        
        
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    run1 = False
def data():
    run  = True
    while run:
        
        global h
        SCREEN1.fill((255,255,255))
        font = pygame.font.Font('freesansbold.ttf', 45)
        text21 = font.render('Data conversion', True, blue, (255,255,255))
        textRect21 = text.get_rect()
        textRect21.center = (500, 100)
        SCREEN1.blit(text21, textRect21)
        pygame.display.update()
        pos  = pygame.mouse.get_pos()
        if textRect21.collidepoint(pos):
                    flag = False
                    if pygame.mouse.get_pressed()[0]==1  and h == False:
                
                        h = True
                        print('yes')
                        flag = False
                    if pygame.mouse.get_pressed()[0]==0 and h == True :
                        h = False
        
        
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    run1 = False
def unit():
    run  = True
    while run:
        
        
        SCREEN1.fill((255,255,255))
        font = pygame.font.Font('freesansbold.ttf', 45)
        text21 = font.render('Units conversion', True, blue, (255,255,255))
        textRect21 = text.get_rect()
        textRect21.center = (500, 100)
        SCREEN1.blit(text21, textRect21)
        pygame.display.update()
        
        
        
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    run1 = False
def equation():
    run  = True
    while run:
        
        
        SCREEN1.fill((255,255,255))
        font = pygame.font.Font('freesansbold.ttf', 45)
        text21 = font.render('Equation solver', True, blue, (255,255,255))
        textRect21 = text.get_rect()
        textRect21.center = (500, 100)
        SCREEN1.blit(text21, textRect21)
        pygame.display.update()
        
        
        
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    run1 = False
def bmi():
    run  = True
    while run:
        
        
        SCREEN1.fill((255,255,255))
        font = pygame.font.Font('freesansbold.ttf', 45)
        text21 = font.render('Body mass index', True, blue, (255,255,255))
        textRect21 = text.get_rect()
        textRect21.center = (500, 100)
        SCREEN1.blit(text21, textRect21)
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
        if my(450,200,calcimage):
            calc()
        if my(650,200,bcimage):
            age()
        if my(250,200,ccimage):
            currency()
        if my(250,350,dcimage):
            time()
        
        if my(450,350,ecimage):
            base()
        
        if my(650,350,fcimage):
            data()
        if my(250,500,gcimage):
            unit()
        if my(450,500,hcimage):
            bmi()
        if my(650,500,icimage):
            equation()
        
        #text
        SCREEN1.blit(text, textRect)
        SCREEN1.blit(text2, textRect2)
        SCREEN1.blit(text3, textRect3)
        SCREEN1.blit(text4, textRect4)
        SCREEN1.blit(text5, textRect5)
        SCREEN1.blit(text6, textRect6)
        SCREEN1.blit(text7, textRect7)
        SCREEN1.blit(text8, textRect8)
        SCREEN1.blit(text9, textRect9)
        SCREEN1.blit(text10, textRect10)
        
           
        pygame.display.update()
        
        
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run1 = False

        
    pygame.quit()
main()



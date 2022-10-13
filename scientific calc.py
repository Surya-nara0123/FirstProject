import pygame
import os
pygame.init()
WIDTH = 1000
HEIGHT = 700
SCREEN1 = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("CALCULATOR")
SCREEN1.fill((255,245,238))
blue = (0,191,255)
font = pygame.font.Font('freesansbold.ttf', 55)
text = font.render('CALCULATOR', True, blue, (255,245,238))
#text
textRect = text.get_rect()
textRect.center = (500, 100)
font = pygame.font.Font('freesansbold.ttf', 15)
text2 = font.render('Currency', True, blue, (255,245,238))
textRect2 = text.get_rect()
textRect2.center = (450, 330)

text3 = font.render('scientific calculator', True, blue, (255,245,238))
textRect3 = text.get_rect()
textRect3.center = (600, 330)

text4 = font.render('Age', True, blue, (255,245,238))
textRect4 = text.get_rect()
textRect4.center = (870, 330)

text5 = font.render('Time', True, blue, (255,245,238))
textRect5 = text.get_rect()
textRect5.center = (470, 480)

text6 = font.render('Base conversions', True, blue, (255,245,238))
textRect6 = text.get_rect()
textRect6.center = (620, 480)

text7 = font.render('Data conversion', True, blue, (255,245,238))
textRect7 = text.get_rect()
textRect7.center = (840, 480)

text8 = font.render('Unit conversion', True, blue, (255,245,238))
textRect8 = text.get_rect()
textRect8.center = (430, 630)

text9 = font.render('BMI', True, blue, (255,245,238))
textRect9 = text.get_rect()
textRect9.center = (670, 630)

text10 = font.render('Equation solver', True, blue, (255,245,238))
textRect10 = text.get_rect()
textRect10.center = (830, 630)
#image

DEFAULT_IMAGE_SIZE = (80, 80)

calc_image = pygame.image.load("C:\\Users\laksh\Downloads\Images\im 1.png").convert_alpha()
calcimage = pygame.transform.scale(calc_image, DEFAULT_IMAGE_SIZE)
bc_image = pygame.image.load("C:\\Users\laksh\Downloads\Images\im2.jpg").convert_alpha()
bcimage = pygame.transform.scale(bc_image, DEFAULT_IMAGE_SIZE)
cc_image = pygame.image.load("C:\\Users\laksh\Downloads\Images\im3.png").convert_alpha()
ccimage = pygame.transform.scale(cc_image, DEFAULT_IMAGE_SIZE)
dc_image = pygame.image.load("C:\\Users\laksh\Downloads\Images\im 4.jfif").convert_alpha()
dcimage = pygame.transform.scale(dc_image, DEFAULT_IMAGE_SIZE)
ec_image = pygame.image.load("C:\\Users\laksh\Downloads\Images\im 5.jpg").convert_alpha()
ecimage = pygame.transform.scale(ec_image, DEFAULT_IMAGE_SIZE)
fc_image = pygame.image.load("C:\\Users\laksh\Downloads\Images\im 6.png").convert_alpha()
fcimage = pygame.transform.scale(fc_image, DEFAULT_IMAGE_SIZE)
gc_image = pygame.image.load("C:\\Users\laksh\Downloads\Images\im 7.png").convert_alpha()
gcimage = pygame.transform.scale(gc_image, DEFAULT_IMAGE_SIZE)
hc_image = pygame.image.load("C:\\Users\laksh\Downloads\Images\im 8.png").convert_alpha()
hcimage = pygame.transform.scale(hc_image, DEFAULT_IMAGE_SIZE)
ic_image = pygame.image.load("C:\\Users\laksh\Downloads\Images\im 9.png").convert_alpha()
icimage = pygame.transform.scale(ic_image, DEFAULT_IMAGE_SIZE)
class button():
    def __init__(self,x,y,image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)
    def draw(self):
        SCREEN1.blit(self.image,(self.rect.x,self.rect.y))
calc_button = button(450,200,calcimage)
#buttons
bc_button = button(650,200,bcimage)
cc_button = button(250,200,ccimage)
dc_button = button(250,350,dcimage)
ec_button = button(450,350,ecimage)
fc_button = button(650,350,fcimage)
gc_button = button(250,500,gcimage)
hc_button = button(450,500,hcimage)
ic_button = button(650,500,icimage)
def main():
    run  = True
    while run:
        #button
        calc_button.draw()
        bc_button.draw()
        cc_button.draw()
        dc_button.draw()
        ec_button.draw()
        fc_button.draw()
        gc_button.draw()
        hc_button.draw()
        ic_button.draw()
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
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
    pygame.quit()
main()


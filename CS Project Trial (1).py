import pygame
import os
import lock_screen
import CS_project_clock
from datetime import datetime
clock=pygame.time.Clock()
pygame.font.init()
FONT=pygame.font.SysFont('comicsans',30)
WIDTH,HEIGHT=600,775
SCREEN=pygame.display.set_mode((WIDTH,HEIGHT))
FPS=60
BLACK=(0,0,0)
WHITE=(255,255,255)
WALLPAPER=pygame.image.load("image.jpeg")
WALLPAPER=pygame.transform.scale(WALLPAPER,(WIDTH,HEIGHT))
t=datetime.now()
TIME_DATE=pygame.font.SysFont('comicsans',15)
#1st screen
"""
probably just a black screen and when eneter is pressed moves on to screen2"
"""
draw_window=False
def draw_window1():
    global draw_window
    SCREEN.fill(BLACK)
    keys_pressed=pygame.key.get_pressed()
    if keys_pressed[pygame.K_LCTRL]:
        draw_window=True
    if draw_window:
        draw_window2()
#2nd screen
'''
Typical lockscreen with text "press enter to unlock", some wallaper, time and date
'''
    
def draw_window2():
    SCREEN.fill(BLACK)
    SCREEN.blit(WALLPAPER,(0,0))
    TEXT=FONT.render("Press enter to unlock",1,WHITE)
    SCREEN.blit(TEXT,(150,650))
    CS_project_clock.drawclock(SCREEN,WIDTH,HEIGHT)
    pygame.display.update()
#3rd screen
"""
A screen with pic lock and need to work on the password setting function and then unlock
to get to the hme screen
"""
def main():
    run=True
    while run:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                run=False
        draw_window1()
        keys_pressed=pygame.key.get_pressed()
        if keys_pressed[pygame.K_F5]:
            lock_screen.main()
        pygame.display.update()
    pygame.quit()
    clock.tick(20)
if __name__ == "__main__":
    main()
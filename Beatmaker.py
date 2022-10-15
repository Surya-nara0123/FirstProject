import pygame as pyg
import sys
pyg.init()
window = pyg.display.set_mode((800, 600))
background = pyg.image.load("SuryaAssets/BeatSequencerMenu.png")
background = pyg.transform.scale(background, (800, 600))
icon = pyg.image.load("SuryaAssets/DrumsLogo.png")
pyg.display.set_icon(icon)
rectList = [
    pyg.Rect(62, 254, 236, 93),
    pyg.Rect(63, 368, 235, 91)
]
run = True
while run:
    window.fill((255,255,255))
    window.blit(background, (0, 0))
    
    for event in pyg.event.get():
        if event.type == pyg.QUIT:
            run = False
            pyg.quit()
            pyg.display.quit()
            sys.exit()
    pyg.display.update()

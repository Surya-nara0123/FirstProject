import pygame as pyg
import sys
from dinoAI import game as g1
from dino import game as g2
from FlappyBird import game as g3
from FlappyBirdAI import game as g4
from tictactoe import game

pyg.init()
SCREEN_HEIGHT = 900
SCREEN_WIDTH = 900
WINDOW = pyg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pyg.display.set_caption('Main Menu')

FONT = pyg.font.Font('freesansbold.ttf', 20)


def mainMenu():
    global WINDOW
    clock = pyg.time.Clock()
    global run
    run = True
    rect = [pyg.Rect(100, 50, 200, 100),
            pyg.Rect(500, 50, 200, 100),
            pyg.Rect(100, 350, 200, 100),
            pyg.Rect(500, 350, 200, 100),
            pyg.Rect(300, 650, 200, 200)
            ]

    pic = []
    for j, box in enumerate(rect):
        if j < 2:
            pic.append(pyg.transform.scale(pyg.image.load('dinoPic.png'), box.size))
        elif j < 4:
            pic.append(pyg.transform.scale(pyg.image.load('flappyPic.png'), box.size))
        else:
            pic.append(pyg.transform.scale(pyg.image.load('tictactoePic.png'), box.size))
    while run:

        WINDOW.fill((220, 255, 220))

        text = [FONT.render('Watch An AI destroy the Trex game', True, (0, 0, 0)),
                FONT.render('Do you want to take on the Trex game yourself', True, (0, 0, 0)),
                FONT.render('Watch An AI destroy the Flappy Bird', True, (0, 0, 0)),
                FONT.render('Do you want to take on the Flappy Bird yourself', True, (0, 0, 0)),
                FONT.render('Win against The computer in tictactoe if you can', True, (0, 0, 0))
                ]

        for j, i in enumerate(rect):
            WINDOW.blit(pic[j], i)
            # pyg.draw.rect(WINDOW, (255, 0, 0), i)
            WINDOW.blit(text[j], (i.midleft[0]-80, i.midleft[1]+100))
        WINDOW.scroll(5000, 5000)

        for event in pyg.event.get():
            if event.type == pyg.QUIT:
                run = False
                pyg.quit()
                sys.exit()

            elif event.type == pyg.MOUSEBUTTONDOWN:
                for j, i in enumerate(rect):
                    if i.collidepoint(pyg.mouse.get_pos()):
                        if j == 0:
                            g1.main()
                            WINDOW = pyg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
                            pyg.display.set_caption('Main Menu')
                        elif j == 1:
                            g2.eval_genomes()
                            WINDOW = pyg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
                            pyg.display.set_caption('Main Menu')
                        elif j == 2:
                            g4.main()
                            WINDOW = pyg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
                            pyg.display.set_caption('Main Menu')
                        elif j == 3:
                            g3.evalGenomes()
                            WINDOW = pyg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
                            pyg.display.set_caption('Main Menu')
                        elif j == 4:
                            game()
                            WINDOW = pyg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
                            pyg.display.set_caption('Main Menu')

        clock.tick(30)
        pyg.display.update()


mainMenu()

import pygame as pyg
import neat
import sys
import math
import os
import random


def init():
    global SCREEN_HEIGHT, SCREEN_WIDTH, SCREEN, FONT, Bird, Pipe
    pyg.init()
    SCREEN_HEIGHT = 600
    SCREEN_WIDTH = 800
    SCREEN = pyg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pyg.display.set_caption('FlappyBird')

    FONT = pyg.font.Font('freesansbold.ttf', 20)


    class Bird:
        X_POS = 80
        Y_POS = 310

        def __init__(self):
            self.x = self.X_POS+25/2
            self.y = self.Y_POS+25/2
            self.gravity = 0.03*3*2*5
            self.velocity = 0
            self.lift = -2
            self.rect = pyg.Rect(self.X_POS, self.Y_POS, 25, 25)

        def update(self):
            self.velocity += self.gravity
            self.y += self.velocity
            if self.y >= 600-25/2:
                self.y = 600-25/2
                self.velocity = 0
            if self.y <= 0:
                self.y = 0
                self.velocity = 0
            self.rect = pyg.Rect(self.x-25/2, self.y-25/2, 25, 25)
            # pyg.draw.rect(SCREEN, (255, 0, 0), self.rect, 2)

        def draw(self):
            pyg.draw.circle(SCREEN, (0, 0, 0), (self.x, self.y), 25/2)

        def jump(self):
            self.velocity += self.lift


    class Pipe:
        def __init__(self):
            self.height = SCREEN_HEIGHT
            self.width = SCREEN_WIDTH
            self.x = self.width
            self.top = random.random() * (self.height/2)
            self.bottom = self.top+200
            self.rect1 = pyg.Rect(self.x, 0, 50, self.top)
            self.rect2 = pyg.Rect(self.x, self.bottom, 50, self.height - self.bottom)

        def show(self):
            pyg.draw.rect(SCREEN, (0, 0, 0), self.rect1)
            pyg.draw.rect(SCREEN, (0, 0, 0), self.rect2)

        def update(self):
            self.x -= gameSpeed
            self.rect1 = pyg.Rect(self.x, 0, 50, self.top)
            self.rect2 = pyg.Rect(self.x, self.bottom, 50,  self.height - self.bottom)
            if self.rect1.x < -self.rect1.width:
                pipes.pop()


def remove(index):
    birds.pop(index)


def distance(pos_a, pos_b):
    dx = pos_a[0]-pos_b[0]
    dy = pos_a[1]-pos_b[1]
    return math.sqrt(dx**2+dy**2)


highScore = 0


def evalGenomes():
    global birds, pipes, gameSpeed, points, highScore
    init()
    clock = pyg.time.Clock()
    points = 0
    birds = [Bird()]
    pipes = []
    gameSpeed = 5

    def score():
        global points, gameSpeed
        points += 1
        if points % 250 == 0:
            gameSpeed += 1
        text = FONT.render(f'Points:  {str(points)}', True, (0, 0, 0))
        SCREEN.blit(text, (650, 50))
        text = FONT.render(f'HighScore:  {str(highScore)}', True, (0, 0, 0))
        SCREEN.blit(text, (450, 50))

    def statistics():
        global birds, gameSpeed
        text_3 = FONT.render(f'Game Speed:  {str(gameSpeed)}', True, (0, 0, 0))

        SCREEN.blit(text_3, (50, 510))

    global run
    run = True
    while run:
        for event in pyg.event.get():
            if event.type == pyg.QUIT:
                run = False

        SCREEN.fill((255, 255, 255))

        for bird in birds:
            bird.update()
            bird.draw()

        if len(birds) == 0:
            break

        if len(pipes) == 0:
            pipes.append(Pipe())

        for pipe in pipes:
            pipe.show()
            pipe.update()
            for i, bird in enumerate(birds):
                if bird.rect.colliderect(pipe.rect1) or bird.rect.colliderect(pipe.rect2):
                    remove(i)

        for i, bird in enumerate(birds):
            keys = pyg.key.get_pressed()
            if keys[pyg.K_SPACE]:
                bird.jump()

        statistics()
        score()
        highScore = max(highScore, points)

        clock.tick(30)
        pyg.display.update()


if __name__ == '__main__':
    evalGenomes()

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
    pyg.display.set_caption('FlappyBirdAI')

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
    ge.pop(index)
    nets.pop(index)


def distance(pos_a, pos_b):
    dx = pos_a[0]-pos_b[0]
    dy = pos_a[1]-pos_b[1]
    return math.sqrt(dx**2+dy**2)

highScore = 0
def evalGenomes(genomes, config):
    global birds, pipes, ge, nets, gameSpeed, points, highScore
    init()
    clock = pyg.time.Clock()
    points = 0
    birds = []
    pipes = []
    ge = []
    nets = []
    gameSpeed = 5

    for genome_id, genome in genomes:
        birds.append(Bird())
        ge.append(genome)
        net = neat.nn.FeedForwardNetwork.create(genome, config)
        nets.append(net)
        genome.fitness = 0

    def score():
        global points, gameSpeed
        points += 1
        text = FONT.render(f'Points:  {str(points)}', True, (0, 0, 0))
        SCREEN.blit(text, (650, 50))
        text = FONT.render(f'HighScore:  {str(highScore)}', True, (0, 0, 0))
        SCREEN.blit(text, (450, 50))


    def statistics():
        global birds, gameSpeed, ge
        text_1 = FONT.render(f'Birds Alive:  {str(len(birds))}', True, (0, 0, 0))
        text_2 = FONT.render(f'Generation:  {pop.generation+1}', True, (0, 0, 0))
        text_3 = FONT.render(f'Game Speed:  {str(gameSpeed)}', True, (0, 0, 0))

        SCREEN.blit(text_1, (50, 450))
        SCREEN.blit(text_2, (50, 480))
        SCREEN.blit(text_3, (50, 510))

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
                    ge[i].fitness -= 1
                    remove(i)
                #   if bird.y == 600-15 or bird.y ==0:
                #       ge[i].fitness -= 1
                #       remove(i)

        for i, bird in enumerate(birds):
            output = nets[i].activate((bird.y, distance((bird.x, bird.y),  pipe.rect1.midbottom), distance((bird.x, bird.y),  pipe.rect2.midtop), distance((bird.x, bird.y),  pipe.rect1.midtop), distance((bird.x, bird.y),  pipe.rect2.midbottom)))
            if output[0] > 0.8:
                bird.jump()

        # if pipes and birds:
        #     pyg.draw.line(SCREEN, (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)), birds[0].rect.midright, pipe.rect1.midbottom)
        #     pyg.draw.line(SCREEN, (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)), birds[0].rect.midright, pipe.rect2.midtop)
        #     pyg.draw.line(SCREEN, (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)), birds[0].rect.midright, pipe.rect1.midtop)
        #     pyg.draw.line(SCREEN, (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)), birds[0].rect.midright, pipe.rect2.midbottom)

        statistics()
        score()
        highScore = max(highScore, points)

        clock.tick(30)
        pyg.display.update()


def run(config_path):
    global pop
    config = neat.config.Config(
        neat.DefaultGenome,
        neat.DefaultReproduction,
        neat.DefaultSpeciesSet,
        neat.DefaultStagnation,
        config_path
    )

    pop = neat.Population(config)
    pop.run(evalGenomes, 50)


def main():
    local_dir = os.path.dirname(__file__)
    # print(local_dir)
    config_path = os.path.join(local_dir, 'requirements.txt')
    run(config_path)


if __name__ == '__main__':
    main()

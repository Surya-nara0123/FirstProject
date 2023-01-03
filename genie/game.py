import sys,math
import pygame as pyg
from AlladinCharacter import *
from JafarCharacter import *

class AlladinRun:
    def __init__(self):
        self.width = self.height = 600
        self.window = pyg.display.set_mode((self.width, self.height))
        self.run = True
        self.move = False
        self.move1 = False
        self.updateKey = None
        self.updateKeyJafar = None
        self.clock = pyg.time.Clock()
        self.status = 'Idle'
        self.status1 = 'Idle'
        self.sprite = Alladin()
        self.sprite1 = Jafar()
        self.mainLoop()

    def mainLoop(self):
        while self.run:
            self.clock.tick(30)
            for event in pyg.event.get():
                if event.type == pyg.QUIT:
                    self.run = False
                    pyg.quit()
                    sys.exit()

            keys = pyg.key.get_pressed()
            if not(self.status == 'Jumping') or not(self.status == 'JumpingRight') or not(self.status == 'JumpingLeft') or not(self.status == 'ThrowRight') or not (self.updateKey != 1):
                if keys[pyg.K_d]:
                    self.status = 'RunningRight'
                    self.move = True
                if keys[pyg.K_a]:
                    self.status = 'RunningLeft'
                    self.move = True
                if keys[pyg.K_w]:
                    self.status = 'Jumping'
                    self.move = False
                if not (keys[pyg.K_d] or keys[pyg.K_w] or keys[pyg.K_a] or keys[pyg.K_SPACE]):
                    self.status = 'Idle'
                    self.move = False
                if (keys[pyg.K_d] and keys[pyg.K_w]):
                    self.status = 'JumpingRight'
                    self.move = True
                if (keys[pyg.K_a] and keys[pyg.K_w]):
                    self.status = 'JumpingLeft'
                    self.move = True
                if keys[pyg.K_SPACE]:
                    self.status = 'ThrowRight'
            if keys[pyg.K_RIGHT]:
                self.status1 = 'RunningRight'
                self.move1 = True
            if keys[pyg.K_LEFT]:
                self.status1 = 'RunningLeft'
                self.move1 = True
            if not (keys[pyg.K_RIGHT] or  keys[pyg.K_LEFT]):
                self.status1 = 'Idle'
                self.move1 = False
            self.window.fill((255, 255, 255))
            self.window.blit(self.sprite.currentFrame, self.sprite.currentFrameRect)
            self.window.blit(self.sprite1.currentFrame, self.sprite1.currentFrameRect)
            pyg.draw.rect(self.window, (255, 100, 100), (0, 400, self.width, self.height))
            self.updateKey = self.sprite.update(self.status, self.updateKey)
            self.updateKeyJafar = self.sprite1.update(self.status1, self.updateKeyJafar)
            self.sprite.move(self.move)
            self.sprite1.move(self.move1)
            if (self.sprite1.currentFrameRect.center[0] - 20  - pyg.mouse.get_pos()[0]):
                self.angle = math.atan((self.sprite1.currentFrameRect.center[1] - 20  - pyg.mouse.get_pos()[1])/ (self.sprite1.currentFrameRect.center[0] - 20  - pyg.mouse.get_pos()[0]))
            self.radius = 50
            if (self.sprite1.currentFrameRect.center[0] - 20  - pyg.mouse.get_pos()[0]) > 0:
                self.point = self.sprite1.currentFrameRect.center[0] - 20  + (self.radius* math.cos(self.angle)), self.sprite1.currentFrameRect.center[1] - 20  + (self.radius* math.sin(self.angle))
            else:
                self.point = self.sprite1.currentFrameRect.center[0] - 20  - (self.radius* math.cos(self.angle)), self.sprite1.currentFrameRect.center[1] - 20  - (self.radius* math.sin(self.angle))
            pyg.draw.line(self.window, (255, 0, 100), (self.sprite1.currentFrameRect.center[0] - 20 , self.sprite1.currentFrameRect.center[1] - 20 - 20 ), self.point)
            pyg.display.update()

if __name__ == "__main__":
    AlladinRun()
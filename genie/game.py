import sys
import pygame as pyg


class Alladin:
    def __init__(self):
        self.spriteSheet = pyg.image.load("genie/Assets/spriteSheet.gif")
        self.currentDirection = "Right"
        self.standingFrames = [
            pyg.image.load("genie/Assets/spriteSheet copy 3.png"),
            pyg.image.load("genie/Assets/spriteSheet copy 3.png"),
            pyg.image.load("genie/Assets/spriteSheet copy 3.png"),
            pyg.image.load("genie/Assets/spriteSheet copy 3.png"),
            pyg.image.load("genie/Assets/spriteSheet copy 3.png"),
            pyg.image.load("genie/Assets/spriteSheet copy 3.png"),
            pyg.image.load("genie/Assets/spriteSheet copy 3.png"),
            pyg.image.load("genie/Assets/spriteSheet copy 3.png"),
            pyg.image.load("genie/Assets/spriteSheet copy 4.png"),
            pyg.image.load("genie/Assets/spriteSheet copy 4.png"),
            pyg.image.load("genie/Assets/spriteSheet copy 4.png"),
            pyg.image.load("genie/Assets/spriteSheet copy 4.png"),
            pyg.image.load("genie/Assets/spriteSheet copy 4.png"),
            pyg.image.load("genie/Assets/spriteSheet copy 4.png"),
            pyg.image.load("genie/Assets/spriteSheet copy 4.png"),
            pyg.image.load("genie/Assets/spriteSheet copy 4.png"),
            pyg.image.load("genie/Assets/spriteSheet copy 4.png")
        ]
        self.standingFramesRects = []
        for i in self.standingFrames:
            rect = i.get_rect()
            rect.centerx, rect.bottom = 100, 300
            self.standingFramesRects.append(rect)
        self.runningFrames = [
            pyg.image.load("genie/Assets/spriteSheet copy 8.png"),
            pyg.image.load("genie/Assets/spriteSheet copy 8.png"),
            pyg.image.load("genie/Assets/spriteSheet copy 10.png"),
            pyg.image.load("genie/Assets/spriteSheet copy 10.png"),
            pyg.image.load("genie/Assets/spriteSheet copy 9.png"),
            pyg.image.load("genie/Assets/spriteSheet copy 9.png"),
            pyg.image.load("genie/Assets/spriteSheet copy 2.png"),
            pyg.image.load("genie/Assets/spriteSheet copy 2.png"),
            pyg.image.load("genie/Assets/spriteSheet copy 6.png"),
            pyg.image.load("genie/Assets/spriteSheet copy 6.png"),
            pyg.image.load("genie/Assets/spriteSheet copy 5.png"),
            pyg.image.load("genie/Assets/spriteSheet copy 5.png"),
            pyg.image.load("genie/Assets/spriteSheet copy 7.png"),
            pyg.image.load("genie/Assets/spriteSheet copy 7.png"),
            pyg.image.load("genie/Assets/spriteSheet copy 11.png"),
            pyg.image.load("genie/Assets/spriteSheet copy 11.png")
        ]
        self.runningFramesRects = []
        for i in self.runningFrames:
            rect = i.get_rect()
            rect.centerx, rect.bottom = 100, 300
            self.runningFramesRects.append(rect)
        self.jumpingFrames = [
            pyg.image.load("genie/Assets/spriteSheet copy 12.png"),
            pyg.image.load("genie/Assets/spriteSheet copy 12.png"),
            pyg.image.load("genie/Assets/spriteSheet copy 13.png"),
            pyg.image.load("genie/Assets/spriteSheet copy 13.png"),
            pyg.image.load("genie/Assets/spriteSheet copy 14.png"),
            pyg.image.load("genie/Assets/spriteSheet copy 14.png"),
            pyg.image.load("genie/Assets/spriteSheet copy 15.png"),
            pyg.image.load("genie/Assets/spriteSheet copy 15.png"),
            pyg.image.load("genie/Assets/spriteSheet copy 16.png"),
            pyg.image.load("genie/Assets/spriteSheet copy 16.png"),
            pyg.image.load("genie/Assets/spriteSheet copy 17.png"),
            pyg.image.load("genie/Assets/spriteSheet copy 17.png"),
            pyg.image.load("genie/Assets/spriteSheet copy 18.png"),
            pyg.image.load("genie/Assets/spriteSheet copy 18.png"),
            pyg.image.load("genie/Assets/spriteSheet copy 19.png"),
            pyg.image.load("genie/Assets/spriteSheet copy 19.png"),

        ]
        self.jumpingFramesRects = []
        for j, i in enumerate(self.jumpingFrames):
            rect = i.get_rect()
            if  j == 0 or j == 1:
                rect.centerx, rect.bottom = 100, (300 - 0)
            if  j == 2 or j == 3:
                rect.centerx, rect.bottom = 100, (300 - 25)
            if  j == 4 or j == 5:
                rect.centerx, rect.bottom = 100, (300 - 50)
            if  j == 6 or j == 7:
                rect.centerx, rect.bottom = 100, (300 - 75)
            if  j == 8 or j == 9:
                rect.centerx, rect.bottom = 100, (300 - 75)
            if  j == 10 or j == 11:
                rect.centerx, rect.bottom = 100, (300 - 50)
            if  j == 12 or j == 13:
                rect.centerx, rect.bottom = 100, (300 - 25)
            if  j == 14 or j == 15:
                rect.centerx, rect.bottom = 100, (300 - 0)
            
            self.jumpingFramesRects.append(rect)
        self.currentFrame = self.standingFrames[1]
        self.currentFrameRect = self.standingFramesRects[1]

    def update(self, status, updateKey=None):
        if status == 'Idle':
            if updateKey == None:
                self.currentFrame = self.standingFrames[0]
                self.currentFrameRect = self.standingFramesRects[0]
                updateKey = 1
            else:
                if updateKey >= len(self.standingFrames):
                    updateKey = 1
                else:
                    updateKey += 1
                self.currentFrame = self.standingFrames[updateKey-1]
                self.currentFrameRect = self.standingFramesRects[updateKey-1]
        if status == 'RunningRight':
            if self.currentDirection != "Right":
                for i in self.jumpingFrames:
                    j = pyg.transform.flip(i, True, False)
                    self.jumpingFrames[self.jumpingFrames.index(i)] = j
                    self.currentDirection = 'Right'
                for i in self.runningFrames:
                    j = pyg.transform.flip(i, True, False)
                    self.runningFrames[self.runningFrames.index(i)] = j
                    self.currentDirection = 'Right'
                for i in self.standingFrames:
                    j = pyg.transform.flip(i, True, False)
                    self.standingFrames[self.standingFrames.index(i)] = j
                    self.currentDirection = 'Right'
            if updateKey == None:
                self.currentFrame = self.runningFrames[0]
                self.currentFrameRect = self.runningFramesRects[0]
                updateKey = 1
            else:
                if updateKey >= len(self.runningFrames):
                    updateKey = 1
                else:
                    updateKey += 1
                self.currentFrame = self.runningFrames[updateKey-1]
                self.currentFrameRect = self.runningFramesRects[updateKey-1]
        if status == 'Jumping':
            if updateKey == None:
                self.currentFrame = self.jumpingFrames[0]
                self.currentFrameRect = self.jumpingFramesRects[0]
                updateKey = 1
            else:
                if updateKey >= len(self.jumpingFrames):
                    updateKey = 1
                else:
                    updateKey += 1
                self.currentFrame = self.jumpingFrames[updateKey-1]
                self.currentFrameRect = self.jumpingFramesRects[updateKey-1]
        if status == 'RunningLeft':
            if self.currentDirection != "left":
                for i in self.jumpingFrames:
                    j = pyg.transform.flip(i, True, False)
                    self.jumpingFrames[self.jumpingFrames.index(i)] = j
                    self.currentDirection = 'left'
                for i in self.runningFrames:
                    j = pyg.transform.flip(i, True, False)
                    self.runningFrames[self.runningFrames.index(i)] = j
                    self.currentDirection = 'left'
                for i in self.standingFrames:
                    j = pyg.transform.flip(i, True, False)
                    self.standingFrames[self.standingFrames.index(i)] = j
                    self.currentDirection = 'left'
            if updateKey == None:
                self.currentFrame = self.runningFrames[0]
                self.currentFrameRect = self.runningFramesRects[0]
                updateKey = 1
            else:
                if updateKey >= len(self.runningFrames):
                    updateKey = 1
                else:
                    updateKey += 1
                self.currentFrame = self.runningFrames[updateKey-1]
                self.currentFrameRect = self.runningFramesRects[updateKey-1]
        return updateKey


class AlladinRun:
    def __init__(self):
        self.width = self.height = 600
        self.window = pyg.display.set_mode((self.width, self.height))
        self.run = True
        self.updateKey = None
        self.clock = pyg.time.Clock()
        self.status = 'Idle'
        self.sprite = Alladin()
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
            if not(self.status == 'Jumping') or not (self.updateKey != 1):
                if keys[pyg.K_RIGHT]:
                    self.status = 'RunningRight'
                    self.move = True
                if keys[pyg.K_LEFT]:
                    self.status = 'RunningLeft'
                    self.move = True
                if keys[pyg.K_UP]:
                    self.status = 'Jumping'
                    self.moeve = False
                if not (keys[pyg.K_RIGHT] or keys[pyg.K_UP] or keys[pyg.K_LEFT]):
                    self.status = 'Idle'
                    self.move = False
                if ((keys[pyg.K_RIGHT] or keys[pyg.K_LEFT]) and keys[pyg.K_UP]):
                    self.status = 'Jumping'
                    self.move = True
            self.window.fill((255, 255, 255))
            self.window.blit(self.sprite.currentFrame, self.sprite.currentFrameRect)
            pyg.draw.rect(self.window, (255, 100, 100), (0, 300, self.width, self.height))
            self.updateKey = self.sprite.update(self.status, self.updateKey)
            pyg.display.update()

if __name__ == "__main__":
    AlladinRun()
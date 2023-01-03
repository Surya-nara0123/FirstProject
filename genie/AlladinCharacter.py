import pygame as pyg


class Alladin:
    def __init__(self):
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
            rect.centerx, rect.bottom = 100, 400
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
            rect.centerx, rect.bottom = 100, 400
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
                rect.centerx, rect.bottom = 100, (400 - 0)
            if  j == 2 or j == 3:
                rect.centerx, rect.bottom = 100, (400 - 40)
            if  j == 4 or j == 5:
                rect.centerx, rect.bottom = 100, (400 - 40- 40)
            if  j == 6 or j == 7:
                rect.centerx, rect.bottom = 100, (400 - 40- 40- 40)
            if  j == 8 or j == 9:
                rect.centerx, rect.bottom = 100, (400 - 40- 40- 40)
            if  j == 10 or j == 11:
                rect.centerx, rect.bottom = 100, (400 - 40- 40)
            if  j == 12 or j == 13:
                rect.centerx, rect.bottom = 100, (400 - 40)
            if  j == 14 or j == 15:
                rect.centerx, rect.bottom = 100, (400 - 0)
            
            self.jumpingFramesRects.append(rect)
        
        self.throwingFrames = [
            pyg.image.load("genie/Assets/throwing Alladin 1.png"),
            pyg.image.load("genie/Assets/throwing Alladin 1.png"),
            pyg.image.load("genie/Assets/throwing Alladin 2.png"),
            pyg.image.load("genie/Assets/throwing Alladin 2.png"),
            pyg.image.load("genie/Assets/throwing Alladin 3.png"),
            pyg.image.load("genie/Assets/throwing Alladin 3.png"),
            pyg.image.load("genie/Assets/throwing Alladin 4.png"),
            pyg.image.load("genie/Assets/throwing Alladin 4.png"),

        ]
        self.throwingFramesRects = []
        for i in self.throwingFrames:
            rect = i.get_rect()
            rect.centerx, rect.bottom = 100, 400
            self.throwingFramesRects.append(rect)
        self.currentFrame = self.standingFrames[1]
        self.currentFrameRect = self.standingFramesRects[1]

    def update(self, status, updateKey=None):
        if status == 'ThrowRight':
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
                for i in self.throwingFrames:
                    j = pyg.transform.flip(i, True, False)
                    self.throwingFrames[self.throwingFrames.index(i)] = j
                    self.currentDirection = 'Right'
            if updateKey == None:
                self.currentFrame = self.throwingFrames[0]
                self.currentFrameRect = self.throwingFramesRects[0]
                updateKey = 1
            else:
                if updateKey >= len(self.throwingFrames):
                    updateKey = 1
                else:
                    updateKey += 1
                self.currentFrame = self.throwingFrames[updateKey-1]
                self.currentFrameRect = self.throwingFramesRects[updateKey-1]
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
                for i in self.throwingFrames:
                    j = pyg.transform.flip(i, True, False)
                    self.throwingFrames[self.throwingFrames.index(i)] = j
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
                for i in self.throwingFrames:
                    j = pyg.transform.flip(i, True, False)
                    self.throwingFrames[self.throwingFrames.index(i)] = j
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
        if status == 'JumpingLeft':
            
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
        if status == 'JumpingRight':
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
        return updateKey
    def move(self, moveStatus):
        if moveStatus:
            for i in self.standingFramesRects:
                rect = i.copy()
                if self.currentDirection == 'Right':
                    rect.x += 6
                else:
                    rect.x -= 6
                self.standingFramesRects[self.standingFramesRects.index(i)] = rect
            for i in self.throwingFramesRects:
                rect = i.copy()
                if self.currentDirection == 'Right':
                    rect.x += 6
                else:
                    rect.x -= 6
                self.throwingFramesRects[self.throwingFramesRects.index(i)] = rect
            for i in self.jumpingFramesRects:
                rect = i.copy()
                if self.currentDirection == 'Right':
                    rect.x += 6
                else:
                    rect.x -= 6
                self.jumpingFramesRects[self.jumpingFramesRects.index(i)] = rect
            for i in self.runningFramesRects:
                rect = i.copy()
                if self.currentDirection == 'Right':
                    rect.x += 6
                else:
                    rect.x -= 6
                self.runningFramesRects[self.runningFramesRects.index(i)] = rect
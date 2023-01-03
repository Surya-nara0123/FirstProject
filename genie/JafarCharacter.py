import pygame as pyg


class Jafar:
    def __init__(self):
        self.standingFrames = [
            pyg.transform.flip(pyg.image.load("genie/Assets/jafar.png"), True, False),
            pyg.transform.flip(pyg.image.load("genie/Assets/jafar.png"), True, False),
            pyg.transform.flip(pyg.image.load("genie/Assets/jafar.png"), True, False),
            pyg.transform.flip(pyg.image.load("genie/Assets/jafar.png"), True, False),
            pyg.transform.flip(pyg.image.load("genie/Assets/jafar.png"), True, False),
            pyg.transform.flip(pyg.image.load("genie/Assets/jafar.png"), True, False),
            pyg.transform.flip(pyg.image.load("genie/Assets/jafar 2.png"), True, False),
            pyg.transform.flip(pyg.image.load("genie/Assets/jafar 2.png"), True, False),
            pyg.transform.flip(pyg.image.load("genie/Assets/jafar 2.png"), True, False),
            pyg.transform.flip(pyg.image.load("genie/Assets/jafar 2.png"), True, False),
            pyg.transform.flip(pyg.image.load("genie/Assets/jafar 2.png"), True, False),
            pyg.transform.flip(pyg.image.load("genie/Assets/jafar 2.png"), True, False),
        ]
        self.currentDirection = 'left'
        self.standingFramesRects = []
        for i in self.standingFrames:
            rect = i.get_rect()
            rect.centerx, rect.bottom = 400, 400
            self.standingFramesRects.append(rect)
        self.currentFrameRect = self.standingFramesRects[0]
        self.currentFrame = self.standingFrames[0]
    def update(self, status, updateKey=None):
        if status == 'Idle':
            if updateKey == None:
                self.currentFrame = self.standingFrames[0]
                self.currentFrameRect = self.standingFramesRects[0]
                updateKey = 1
            else:
                if updateKey >= 6:
                    updateKey = 1
                else:
                    updateKey += 1
                self.currentFrame = self.standingFrames[updateKey-1]
                self.currentFrameRect = self.standingFramesRects[updateKey-1]
        if status == 'RunningLeft':
            if self.currentDirection != "left":
                for i in self.standingFrames:
                    j = pyg.transform.flip(i, True, False)
                    self.standingFrames[self.standingFrames.index(i)] = j
                    self.currentDirection = 'left'
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
                for i in self.standingFrames:
                    j = pyg.transform.flip(i, True, False)
                    self.standingFrames[self.standingFrames.index(i)] = j
                    self.currentDirection = 'Right'
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
                self.currentFrame = self.standingFrames[updateKey-1]
                self.currentFrameRect = self.standingFramesRects[updateKey-1]
        
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
            
    
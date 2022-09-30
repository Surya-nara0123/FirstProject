import math
import pygame as pyg

qwerty = 0
class Game:
    def __init__(self, WIDTH, HEIGHT):
        self.board = [
            ['', '', ''],
            ['', '', ''],
            ['', '', '']
        ]
        self.l = WIDTH / 3
        self.h = HEIGHT / 3
        self.offset = self.l / 4
        self.positions = [
            [
                pyg.rect.Rect(0, 0, self.l-10, self.h-10),
                pyg.rect.Rect(self.l, 0, self.l-10, self.h-10),
                pyg.rect.Rect(self.l*2, 0, self.l-10, self.h-10)
            ],
            [
                pyg.rect.Rect(0, self.h, self.l-10, self.h-10),
                pyg.rect.Rect(self.l, self.h, self.l-10, self.h-10),
                pyg.rect.Rect(self.l*2, self.h, self.l-10, self.h-10)
            ],
            [
                pyg.rect.Rect(0, self.h*2, self.l-10, self.h-10),
                pyg.rect.Rect(self.l, self.h*2, self.l-10, self.h-10),
                pyg.rect.Rect(self.l*2, self.h*2, self.l-10, self.h-10)
            ]
        ]

    def checkWin(self, arr):
        winner = None
        loop = True
        for i in range(3):
            if arr[i][0] == arr[i][1] == arr[i][2] and arr[i][0] != '':
                winner = arr[i][0]
                loop = False
        for i in range(3):
            if arr[0][i] == arr[1][i] == arr[2][i] and arr[0][i] != '':
                winner = arr[0][i]
                loop = False
        if arr[0][0] == arr[1][1] == arr[2][2] and arr[0][0] != '':
            winner = arr[0][0]
        elif arr[0][2] == arr[1][1] == arr[2][0] and arr[0][2] != '':
            winner = arr[0][2]
        elif self.getAvailable(arr) == 0 and loop:
            winner = 'Tie'
        if winner is not None:
            return winner

    @staticmethod
    def getAvailable(arr):
        available = 0
        for i in range(3):
            for j in range(3):
                if arr[i][j] == '':
                    available += 1
        return available

    def drawBoard(self):
        window.fill((0, 0, 0))
        for i in range(3):
            for j in range(3):
                pyg.draw.rect(window, (255, 255, 255), self.positions[i][j], 0, 4)

    def drawPieces(self):
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == 'X':
                    pyg.draw.line(window, (0, 0, 0), (self.l * j + self.offset, self.h * i + self.offset),
                                  (self.l * (j + 1) - self.offset, self.h * (i + 1) - self.offset), 5)
                    pyg.draw.line(window, (0, 0, 0), (self.l * (j + 1) - self.offset, self.h * i + self.offset),
                                  (self.l * j + self.offset, self.h * (i + 1) - self.offset), 5)
                elif self.board[i][j] == 'O':
                    pyg.draw.circle(window, (0, 0, 0), ((self.l * j + self.offset + self.l * (j + 1) - self.offset) / 2, (self.h * i + self.offset + self.h * (i + 1) - self.offset) / 2), self.l / 2 - self.offset + 5, 4)

    def getMove(self):
        bestMove = None
        bestScore = math.inf
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == '':
                    self.board[i][j] = 'O'
                    score = self.minimax(self.board, -math.inf, math.inf, 0, True)
                    self.board[i][j] = ''
                    if score < bestScore:
                        bestScore = score
                        bestMove = {'i': i, 'j': j}
        self.board[bestMove['i']][bestMove['j']] = 'O'

    def minimax(self, arr, a, b, depth, maximising):
        global qwerty
    
        result = self.checkWin(arr)
        if result:
            d = {'X': +1, 'O': -1, 'Tie': 0}
            return d[result]
        if maximising is True:
            bestScore = -math.inf
            for i in range(3):
                for j in range(3):
                    if arr[i][j] == '':
                        arr[i][j] = 'X'
                        qwerty += 1
                        score = self.minimax(arr, a, b, depth + 1, False)
                        print(qwerty, end="  ")
                        arr[i][j] = ''
                        bestScore = max((score, bestScore))
                        a = max((a, score))
                        if b <= a:
                            break
            return bestScore
        else:
            bestScore = math.inf
            for i in range(3):
                for j in range(3):
                    if arr[i][j] == '':
                        arr[i][j] = 'O'
                        qwerty += 1
                        score = self.minimax(arr, a, b, depth+1, True)
                        print(qwerty, end="  ")
                        arr[i][j] = ''
                        bestScore = min((score, bestScore))
                        a = max((a, score))
                        if b <= a:
                            break
            return bestScore

    def main(self):
        self.run = True
        while self.run:
            for event in pyg.event.get():
                if event.type == pyg.QUIT:
                    self.run = False
                if event.type == pyg.MOUSEBUTTONDOWN:
                    for i in range(3):
                        for j in range(3):
                            if self.positions[i][j].collidepoint(pyg.mouse.get_pos()):
                                if self.board[i][j] == '':
                                    if self.checkWin(self.board) is None:
                                        self.board[i][j] = 'X'
                                        if self.checkWin(self.board) is None:
                                            self.getMove()
                                            print(qwerty)
                                    else:
                                        print(self.checkWin(self.board))

            if self.checkWin(self.board):
                print(self.checkWin(self.board))
                self.run = False
                pyg.quit()
                sys.quit()

            self.drawBoard()
            self.drawPieces()
            pyg.display.update()


def game():
    global window
    pyg.init()
    window = pyg.display.set_mode((600, 600))
    pyg.display.set_caption('TicTacToe')
    newGame = Game(600, 600)
    newGame.main()
game()

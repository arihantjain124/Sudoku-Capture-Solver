import numpy as np
from sudokuread import puzzlereader
import cv2


class cell:
    def __init__(self, row, col, number):
        self.solved = True if number > 0 else False
        self.known = True if number > 0 else False
        self.number = number
        self.col = col
        self.row = row
        self.possiblenumber = list((range(1, 10))) if not self.solved else[]
        if self.solved == False:
            self.possiblenumber = self.getpossiblenumber()
        self.indexpossible = 0
        self.back = [row, col]
        if col == 0 and row == 0:
            self.back[0] = 9
            self.back[1] = 9
        elif col == 0:
            self.back[1] = 8
            self.back[0] -= 1
        else:
            self.back[1] -= 1

        self.forward = [row, col]
        if col == 8 and row == 8:
            self.forward[0] = 9
            self.forward[1] = 9
        elif col == 8:
            self.forward[0] += 1
            self.forward[1] = 0
        else:
            self.forward[1] += 1
        self.indexlen = len(self.possiblenumber)

    def changenumber(self, number):
        self.number = number
        puzzle[self.row][self.col] = self.number

    def getboxcoor(self, row, col):
        if row in [0, 1, 2]:
            row = 0
        elif row in [3, 4, 5]:
            row = 3
        else:
            row = 6
        if col in [0, 1, 2]:
            col = 0
        elif col in [3, 4, 5]:
            col = 3
        else:
            col = 6
        return row, col

    def getboxnumber(self):
        boxnum = []
        row, col = self.getboxcoor(self.row, self.col)
        for i in range(3):
            for j in range(3):
                boxnum.append(puzzle[row+i][col+j])
        return boxnum

    def colrowboxnumber(self):
        colnumber = np.array(puzzle)
        colnumber = list(colnumber[:, self.col])
        return puzzle[self.row] + colnumber + self.getboxnumber()

    def isvalid(self, x):
        if x not in self.colrowboxnumber():
            return True
        else:
            return False

    def getpossiblenumber(self):
        for i in self.colrowboxnumber():
            if i in self.possiblenumber:
                self.possiblenumber.remove((i))
        return self.possiblenumber

    def solvecell(self):

        if self.known == True:
            return self.forward, 1
        elif self.solved == False or self.known == False:
            while(self.indexpossible < self.indexlen):
                if self.isvalid(self.possiblenumber[self.indexpossible]):
                    self.changenumber(self.possiblenumber[self.indexpossible])
                    self.indexpossible += 1
                    self.solved = True
                    return self.forward, 2
                self.indexpossible += 1
            self.indexpossible = 0
            self.changenumber(0)
            return self.back, 0


class sudoku():
    def __init__(self, puzzle):
        puzzle = puzzle
        self.cells = []
        self.coor = [0, 0]
        self.solvedcell = []
        self.Flag = 1

    def initialzecells(self):
        temp = []
        for i in range(9):
            for j in range(9):
                temp.append(
                    cell(i, j, puzzle[i][j]))
            self.cells.append(temp)
            temp = []

    def solve(self):
        while (self.coor[0] != 9):
            temp = self.coor[:]
            self.coor, self.Flag = self.cells[self.coor[0]
                                              ][self.coor[1]].solvecell()
            if self.Flag == 2:
                self.solvedcell.append(temp)
            elif self.Flag == 0:
                self.coor = self.solvedcell.pop()

    def printpuzzle(self):
        for i in range(9):
            print(puzzle[i], "\n")


def sudokusolve(puzzle):
    game = sudoku(puzzle)
    game.initialzecells()
    game.solve()
    game.printpuzzle()


img = cv2.imread("Test_Images/2.png")
puzzle = puzzlereader(img)
sudokusolve(puzzle)

class cell:
    def __init__(self, row, col, number, puzzle):
        self.solved = True if number > 0 else False
        self.number = number
        self.col = col
        self.row = row
        self.puzzle = puzzle
        self.possiblenumber = list((range(1, 10))) if not self.solved else[]
        self.indexvalid = 0
        if not self.solved:
            self.getpossiblenumber()

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
                boxnum.append(self.puzzle[row+i][col+j])
        return boxnum

    def isvalid():
        pass

    def getpossiblenumber(self):
        for i in self.puzzle[self.row] + self.puzzle[self.col] + self.getboxnumber():
            if i in self.possiblenumber:
                self.possiblenumber.remove((i))


class sudoku():
    def __init__(self, puzzle):
        self.puzzle = puzzle
        self.cells = []

    def initialzecells(self):
        temp = []
        for i in range(9):
            for j in range(9):
                temp.append(cell(i, j, self.puzzle[i][j], self.puzzle))
            self.cells.append(temp)
            temp = []

    def readpossiblecell(self, row, col):
        x = self.cells[row][col]
        print(x.possiblenumber)

    def solve(self):
        for i in range()


puzzle = [[3, 0, 6, 5, 0, 8, 4, 0, 0],
          [5, 2, 0, 0, 0, 0, 0, 0, 0],
          [0, 8, 7, 0, 0, 0, 0, 3, 1],
          [0, 0, 3, 0, 1, 0, 0, 8, 0],
          [9, 0, 0, 8, 6, 3, 0, 0, 5],
          [0, 5, 0, 0, 9, 0, 6, 0, 0],
          [1, 3, 0, 0, 0, 0, 2, 5, 0],
          [0, 0, 0, 0, 0, 0, 0, 7, 4],
          [0, 0, 5, 2, 0, 6, 3, 0, 0]]
game = sudoku(puzzle)
game.initialzecells()

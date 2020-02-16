import tkinter
from tkinter import constants
import random

import sudokus


class MainWindow(tkinter.Frame):

    def __init__(self, master=None, cnf={}, **kw):
        super().__init__(master=master, cnf=cnf, **kw)
        self.Sudoku = None
        self.sudokuSetup()
        self.printBoard()
        self.pack(fill="both", expand=True)

    def pack(self, **kw):
        super().pack(**kw)

    def sudokuSetup(self):
        self.Sudoku = sudokus.make_board(3)
        self.hideBoard()

    def printBoard(self):
        for row in self.Sudoku:
            numtext = ""
            for col in row:
                numtext += str(col)
                numtext += " "
            print(numtext)

    def hideBoard(self):
        randomlistrow = [0, 1, 2, 3, 4, 5, 6, 7, 8]
        randomlistcol = [0, 1, 2, 3, 4, 5, 6, 7, 8]
        random.shuffle(randomlistcol)
        random.shuffle(randomlistrow)
        for row in randomlistrow:
            for col in randomlistcol:
                possibles = 0
                old = self.Sudoku[row][col]
                self.Sudoku[row][col] = 0
                for n in range(1, 10):
                    if self.possible(col, row, n):
                        possibles += 1
                if possibles != 1:
                    self.Sudoku[row][col] = old

    def possible(self, x, y, n):
        for row in range(0, 9):
            if self.Sudoku[row][x] == n:
                return False
        for col in range(0, 9):
            if self.Sudoku[y][col] == n:
                return False
        xsq = (x // 3) * 3
        ysq = (y // 3) * 3
        for i in range(0, 3):
            for j in range(0, 3):
                if self.Sudoku[ysq+i][xsq+j] == n:
                    return False
        return True

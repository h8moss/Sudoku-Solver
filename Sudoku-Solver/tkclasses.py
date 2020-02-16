from tkinter import *


class MainWindow(Frame):

    def __init__(self, master=None, cnf={}, **kw):
        super().__init__(master=master, cnf=cnf, **kw)
        self.sudokuSetup()
        self.pack(fill=BOTH, expand=YES)

    def pack(self, **kw):
        super().pack(**kw)

    def sudokuSetup(self):
        pass

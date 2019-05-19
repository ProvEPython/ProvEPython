import tkinter as tk
from dependencies import GUI
import os
import frames.StartPage as StartPage
from tkinter import ttk
import sys

LARGE_FONT = ("Verdana", 12)

class SetUp(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)


        self.label = ttk.Label(self, text="Choose storage place of the directory", font=LARGE_FONT)
        self.label.grid(columnspan=2)

        self.ent = GUI.Ent(self, text="Place:")
        self.ent.grid(column=1, sticky='w')

        self.btn = GUI.Btn(self, text="OK")
        self.btn.grid(row=2, sticky="e")
        self.btn.coms(lambda: self.change())

        self.btn2 = GUI.Btn(self, text="BACK")
        self.btn2.grid(row=2, sticky="w", column=1)
        self.btn2.coms(lambda: controller.show_frame(StartPage.StartPage))

        for col in range(self.grid_size()[0]):
            self.grid_columnconfigure(col, weight=1, uniform=self.ent)
        for row in range(self.grid_size()[1]):
            self.grid_rowconfigure(row, weight=1)

    def change(self):
        with open("dependencies/path.py", 'r') as f:
            a = f.read()
        with open("dependencies/path.py", 'w') as path:
            if os.path.isdir(self.ent.get()):
                path.write('import os\nSUB_DIR = os.path.abspath("' + self.ent.get() + '")')
                global SUB_DIR
                SUB_DIR = self.ent.get()

            else:
                GUI.Error(self, messege="Can't find the search path")
                path.write(a)

        self.ent.delete(0, 'end')




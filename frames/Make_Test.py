import tkinter as tk
from dependencies import GUI
import frames.StartPage as StartPage
import os
import subprocess
import random as r
from dependencies import path

LARGE_FONT = ("Verdana", 12)

SUB_DIR = path.SUB_DIR


class MakeTest(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.cats = []

        self.label = tk.Label(self, text="Choose subject", font=LARGE_FONT)
        self.label.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

        self.ent = GUI.Ent(self, text="Test Name:", width=18)
        self.ent.grid(column=1, row=1, pady=5)

        self.sub_var = tk.StringVar()
        self.sub = GUI.Cb(self, text="Subject:", textvar=self.sub_var, values=os.listdir(SUB_DIR), width=15)
        self.sub.grid(column=1, row=2, pady=5, padx=10)
        self.sub_var.trace('w', lambda a, b, c: self.callback())

        self.btn1 = GUI.Btn(self, text="OK")
        self.btn1.coms(lambda: self.mk_test())

        self.btn2 = GUI.Btn(self, text="BACK")
        self.btn2.coms(lambda: controller.show_frame(StartPage.StartPage))

        self.btn1.grid(row=self.grid_size()[1], column=0, sticky='e')
        self.btn2.grid(row=self.grid_size()[1] - 1, column=1, sticky='w')

        for col in range(self.grid_size()[0]):
            self.grid_columnconfigure(col, weight=1, uniform=self.ent)
        for row in range(self.grid_size()[1]):
            self.grid_rowconfigure(row, weight=1)

    def callback(self):
        self.btn1.grid_remove()
        for cat in self.cats:
            cat.label.destroy()
            cat.destroy()
        self.i = False
        for dirr in os.listdir(SUB_DIR + '/' + self.sub.get()):
            if os.path.isfile(SUB_DIR + '/' + self.sub.get() + '/' + dirr):
                self.i = True
            elif len(os.listdir(SUB_DIR + '/' + self.sub.get() + '/' + dirr)):
                self.cats.append(GUI.Sb(self, text=dirr, width=3, values=tuple(
                    range(0, len(os.listdir(SUB_DIR + '/' + self.sub.get() + '/' + dirr)) + 1))))
                self.cats[-1].grid(column=1)
        if self.i:
            count = 0
            for each in os.listdir(SUB_DIR + '/' + self.sub.get()):
                if os.path.isfile(SUB_DIR + '/' + self.sub.get() + '/' + each):
                    count += 1


        self.cats[-1].grid(column=1)
        self.btn1.grid(row=self.grid_size()[1], column=0, sticky='e', pady=5)
        self.btn2.grid(row=self.grid_size()[1] - 1, column=1, sticky='w', pady=5)

    def mk_test(self):
        q = {}
        for cat in self.cats:

            if int(cat.get()):
                questions = r.sample(range(0, len(os.listdir(SUB_DIR + '/' + self.sub.get() + '/' + cat.label['text']))),
                                     int(cat.get()))
                q[cat] = questions

        with open("./dependencies/Template.tex", "r") as f:
            content = f.readlines()

            for line in content:
                if line == "\\title{}\n":

                    o_line = line[:line.find('}')] + self.ent.get() + line[line.find('}'):]
                    content.insert(5, o_line)
                    del content[6]


            ind = content.index('\pointsinrightmargin\n') + 1

            for cat in q:


                dirr = SUB_DIR + '/' + self.sub.get() + '/' + cat.label['text'] + '/'


                for question in q[cat]:

                    with open(dirr + os.listdir(dirr)[question], "r") as file:
                        i = ind
                        for line in file:
                            content.insert(i, line)
                            i += 1

        with open("Compile.tex", "w") as f:
            for line in content:
                f.write(line)

        subprocess.call(['pdflatex', "Compile.tex"])
        os.remove("Compile.aux")
        os.remove("Compile.log")
        os.remove("Compile.tex")
        os.rename("Compile.pdf", "prov/" + self.ent.get() + ".pdf")
        quit()

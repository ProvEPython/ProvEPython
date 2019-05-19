import tkinter as tk
from tkinter import ttk
import frames.StartPage as StartPage
from dependencies import GUI
import os
import frames.Add_SubQ as EnterSubQ
from dependencies.path import SUB_DIR as SUB_DIR

LARGE_FONT = ("Verdana", 12)



dirr = None
count = 0

class EnterQ(tk.Frame):

    cb1 = None
    cb2 = None

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)



        self.label = ttk.Label(self, text="Add a question", font=LARGE_FONT)
        self.label.grid(columnspan=1, row=0, column=1, pady=10)



        self.box_var1 = tk.StringVar()
        self.cb1 = GUI.Cb(self, text="Subject:", textvariable=self.box_var1, values=os.listdir(SUB_DIR))
        self.cb1.grid(columnspan=2, column=1, sticky='w', pady=5)
        self.box_var1.trace('w', lambda a, b, c: self.callback())

        self.box_var2 = tk.StringVar()
        self.cb2 = GUI.Cb(self, text="Category:", textvariable=self.box_var2)
        self.cb2.grid(columnspan=2, column=1, sticky='w', pady=5)
        self.box_var2.trace('w', lambda a, b, c: self.callback())



        self.ent = GUI.Text(self, text="Question:", height=4, width=20)
        self.ent.grid(row=self.grid_size()[1], column=1, sticky="w", pady=5)

        self.sb1 = GUI.Sb(self, text="Points:", values=tuple(range(0, 50)), width=3)
        self.sb1.grid(row=self.grid_size()[1], column=1, sticky="w")

        self.sb2 = GUI.Sb(self, text="Nr of Sub questions:", values=tuple(range(2, 50)), width=3)
        self.sb2.grid(row=self.grid_size()[1], column=1, sticky="w")
        self.sb2.delete(0, "end")
        self.sb2.insert(0, 2)
        self.sb2.config(state='disabled')


        self.c = GUI.CheckBox(self, text="Sub questions?")
        self.c.grid(row=self.grid_size()[1], column=1, sticky="w")
        self.c.set_coms(lambda: self.sb2.config(state='normal'), lambda: self.toggle_func(self.c.var),
                        state=True)
        self.c.set_coms(lambda: self.sb2.config(state='disabled'), lambda: self.toggle_func(self.c.var),
                        state=False)
        self.c.config()

        self.btn1 = GUI.Btn(self, text="OK", state='disabled')
        self.btn1.grid(row=self.grid_size()[1], column=0, sticky="e")
        self.btn1.coms(lambda: self.err(lambda: self.add_q(), lambda: self.ent.delete("1.0", "end-1c")))

        self.btn2 = GUI.Btn(self, text="Back")
        self.btn2.grid(row=self.grid_size()[1] - 1, column=1, sticky="w")
        self.btn2.coms(lambda: controller.show_frame(StartPage.StartPage))

        for col in range(self.grid_size()[0]):
            self.grid_columnconfigure(col, weight=1, uniform=self.ent)
        for row in range(self.grid_size()[1]):
            self.grid_rowconfigure(row, weight=1)

    def toggle_func(self, v):
        if v:
            self.btn1.coms(lambda: self.err(
                           lambda: self.add_q(),
                           lambda: self.runTl(int(self.sb2.get()))),
                           lambda: self.ent.delete("1.0", 'end'))

        else:
            self.btn1.coms( lambda: self.err(lambda: self.toggle_func(self.c.var),
                                             lambda: self.add_q()),
                                             lambda: self.ent.delete("1.0", 'end'))

    def callback(self):
        if self.cb1.get() and self.cb2.get():
            self.btn1.config(state='normal')
        else:
            self.btn1.config(state='disabled')

        vals = []

        for each in os.listdir(SUB_DIR + '/' + self.cb1.get()):
            vals.append(each)


        self.cb2.config(values=vals)

    def err(self, *funcs):
        if not self.ent.get("1.0", "end-1c"):
            self.error = GUI.Error(self, messege="Please write the question!")
        else:
            for f in funcs:
                f()


    def add_q(self):



        global dirr
        dirr = SUB_DIR + '/' + self.cb1.get() + '/' + self.cb2.get() + '/' + str(len(os.listdir(SUB_DIR + '/' + self.cb1.get() + '/' + self.cb2.get()))) + '.' + self.ent.get("1.0", "1.5")[0:-1] + ".txt"
        with open(dirr, "a") as f:
            f.write("\\question[" + self.sb1.get() + "]\n")
            f.write(self.ent.get("1.0", "end-1c") + "\n")


    def runTl(self, count):

        for each in range(0, count):
            if not each:
                tl = GUI.Tl(self, EnterSubQ.EnterSubQ, first=True)
            elif each == count - 1:
                tl = GUI.Tl(self, EnterSubQ.EnterSubQ, last=True)
            else:
                tl = GUI.Tl(self, EnterSubQ.EnterSubQ)



            self.wait_window(tl)







import tkinter as tk
from dependencies import GUI
import frames.Add_Question as EnterQ


LARGE_FONT = ("Verdana", 12)

class EnterSubQ(tk.Frame):
    def __init__(self, parent, controller, first=False, last=False):
        tk.Frame.__init__(self, parent)


        self.index = 1


        label = tk.Label(self, text="Sub question", font=LARGE_FONT)
        label.grid(pady=10, columnspan=2)

        
        self.ent = GUI.Text(self, text="Question:", height=4, width=20)
        self.ent.grid(row=2, column=1, sticky='w', pady=5)
        
        self.sb1 = GUI.Sb(self, text="Points:", from_=1, to=10)
        self.sb1.grid(row=3, column=1, sticky='w', pady=5)

        self.btn = GUI.Btn(self, text="OK")
        self.btn.coms(lambda: self.err(
                      lambda: self.add_subq(EnterQ.dirr, self.ent.get("1.0", "end-1c"), self.sb1.get(), first, last),
                      lambda: controller.destroy()))
        self.btn.grid(row=4, columnspan=2, pady=5)



        for col in range(self.grid_size()[0]):
            self.grid_columnconfigure(col, weight=1, uniform=self.ent)
        for row in range(self.grid_size()[1]):
            self.grid_rowconfigure(row, weight=1)




    def err(self, *funcs):
        if not self.ent.get("1.0", "end-1c"):
            self.error = GUI.Error(self, messege="Please write the question!")
        else:
            for f in funcs:
                f()
    
    def add_subq(self, dirr, subq, p, first, last):
        file = ""
        if first:
            file += "\\begin{parts}\n"
        file += "\part[" + p + "]\n"
        file += subq + "\n"
        if last:
            file += "\end{parts}\n"

        with open(dirr, "a+t") as f:
            f.write(file)



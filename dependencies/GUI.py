import tkinter as tk
from tkinter import ttk


def combine(*funcs):
    for f in funcs:
        f()


class Window(tk.Tk):

    def __init__(self, frames, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        tk.Tk.wm_title(self, "Prov Skapare")
        self.container = tk.Frame(self)
        self.container.pack(fill="both", expand=True)
        self.container.columnconfigure(0, weight=1)
        self.container.rowconfigure(0, weight=1)

        self.frames = {}

        for F in frames:
            frame = F(self.container, self)
            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(frames[0])

    def show_frame(self, cont):
        self.update_frame(cont)


        for frame in self.frames.values():
            frame.grid_remove()
        frame = self.frames[cont]
        frame.grid()

    def update_frame(self, cont):
        self.frames.update({cont: cont(self.container, self)})
        frame = self.frames[cont]
        frame.grid(row=0, column=0, sticky="nsew")


class Btn(ttk.Button):
    def __init__(self, parent, **kwargs):
        ttk.Button.__init__(self, parent, **kwargs)

    def coms(self, *commands):
        self.config(command=lambda: combine(*commands))



class Rb(ttk.Radiobutton):
    def __init__(self, parent, **kwargs):
        ttk.Radiobutton.__init__(self, parent, **kwargs)


class Sb(ttk.Spinbox):
    def __init__(self, parent, text="", **kwargs):
        ttk.Spinbox.__init__(self, parent, **kwargs)
        self.label = ttk.Label(parent, text=text)
        ttk.Spinbox.insert(self, tk.END, "1")

    def grid(self, **kwargs):
        ttk.Spinbox.grid(self, **kwargs)
        self.label.grid(row=self.grid_info()['row'], column=self.grid_info()['column'] - 1, sticky="e")

class Cb(ttk.Combobox):
    def __init__(self, parent,text="", **kwargs):
        self.label = ttk.Label(parent, text=text)
        ttk.Combobox.__init__(self, parent, **kwargs)

    def grid(self, **kwargs):
        ttk.Combobox.grid(self, **kwargs)
        self.label.grid(row=self.grid_info()['row'], column=self.grid_info()['column'] - 1, sticky="e")

class Ent(ttk.Entry):
    def __init__(self, parent, text="", **kwargs):
        ttk.Entry.__init__(self, parent, **kwargs)
        self.label = tk.Label(parent, text=text)

    def grid(self, **kwargs):
        ttk.Entry.grid(self, **kwargs)
        self.label.grid(row=self.grid_info()['row'], column=self.grid_info()['column'] - 1, sticky="e")


class CheckBox(tk.Checkbutton):
    def __init__(self, parent, text=""):
        self.var = tk.BooleanVar()
        self.t_coms = []
        self.f_coms = []
        tk.Checkbutton.__init__(self, parent, text=text, variable=self.var)

    def set_coms(self, *commands, state):

        if state:
            self.f_coms.append(lambda: self.config())
            for each in commands:
                self.f_coms.append(each)
        else:
            self.t_coms.append(lambda: self.config())
            for each in commands:
                self.t_coms.append(each)

    def config(self):
        if self.var.get():
            super().config(self, command=lambda: combine(*self.t_coms))
        else:
            super().config(self, command=lambda: combine(*self.f_coms))

class Error(tk.Toplevel):
    def __init__(self, parent, messege=""):
        tk.Toplevel.__init__(self, parent)

        photo = tk.PhotoImage(file="./dependencies/Error.ppm")
        self.image = tk.Label(self, image=photo)
        self.image.image = photo
        self.image.grid()

        self.labelT = ttk.Label(self, text=messege)
        self.labelT.grid(row=0, column=1)

        self.btn = Btn(self, text="OK", command=lambda: self.destroy())
        self.btn.grid(columnspan=2, row=1)


class Text(tk.Text):
    def __init__(self, parent, text="", **kwargs):
        tk.Text.__init__(self, parent, **kwargs)
        self.label = tk.Label(parent, text=text)

    def grid(self, **kwargs):
        ttk.Entry.grid(self, **kwargs)
        self.label.grid(row=self.grid_info()['row'], column=self.grid_info()['column'] - 1, sticky="e")

class Tl(tk.Toplevel):
    def __init__(self, parent, frame, **kwargs):
        tk.Toplevel.__init__(self, parent)

        self.container = tk.Frame(self)
        self.container.pack(fill="both", expand=True)
        self.container.columnconfigure(0, weight=1)
        self.container.rowconfigure(0, weight=1)

        f = frame(self.container, self, **kwargs)
        f.pack()






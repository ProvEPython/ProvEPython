import tkinter as tk
from dependencies import GUI
import frames.Make_Test as Make_Test
import frames.Add_Question as EnterQ
import frames.Settings as Settings
LARGE_FONT = ("Verdana", 12)


class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.config(height=100)
        self.config(width=200)
        label = tk.Label(self, text="Start Page", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        btn1 = GUI.Btn(self, text="Add questions")
        btn1.coms(lambda: controller.show_frame(EnterQ.EnterQ))
        btn1.pack()
        btn2 = GUI.Btn(self, text="   Create Test   ")
        btn2.coms(lambda: controller.show_frame(Make_Test.MakeTest))
        btn2.pack()
        btn3 = GUI.Btn(self, text="Change settings")
        btn3.coms(lambda: controller.show_frame(Settings.SetUp))
        btn3.pack()


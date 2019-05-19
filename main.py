
import frames.StartPage as StartPage

from dependencies import GUI

FRAMES = [StartPage.StartPage]

def main():
    root = GUI.Window(FRAMES)
    root.mainloop()

main()
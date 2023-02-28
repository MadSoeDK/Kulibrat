from tkinter import *

from src.Controller.GameController import GameController


@staticmethod
def launch():
    width = 1000
    height = 900

    gameController = GameController()
    window = Tk()
    window.title("Kulibrat")
    window.minsize(width, height)
    window.resizable(False, False)

    b = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
    ]

    for i in range(4):
        for j in range(3):
            background= "white" if (i*3+j) % 2 == 0 else "black"
            b[i][j] = Button(
                height=8, width=16,
                background=background,
                command=lambda: gameController.click(i*3+j)
            )
            b[i][j].grid(row=i, column=j)

    mainloop()



def callback(e):
    if e.x > 20 & e.x < 600 & e.y > 20 & e.y < 820:
        print("within")
    print("x=%d, y=%d", e.x, e.y)


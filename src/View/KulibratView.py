import tkinter as tk

from src.Controller.GameController import GameController


@staticmethod
def launch():
    width = 500
    height = 500


    gameController = GameController()
    window = tk.Tk()
    window.minsize(width, height)
    window.resizable(False, False)

    grid = tk.Canvas

    window.mainloop()

